"""DAG-driven generation; per-skill result files on disk act as the resume cache."""

import asyncio
import json
from pathlib import Path
from typing import Any

from pydantic import ValidationError

from .config import Settings
from .models import SkillRecord
from .prompts import PromptSet, render_user_prompt
from .outputs import write_skill_output


def result_path(settings: Settings, skill: SkillRecord) -> Path:
    """Per-skill results live under results/skills/<owner>/<repo>/<slug>/ (id-based,
    mirroring the upstream data/skills/ layout)."""
    return settings.workdir / "results" / "skills" / skill.id.replace(":", "_") / "result.json"


async def run_prompt(
    llm, settings: Settings, prompts: PromptSet, spec, skill: SkillRecord, deps: dict
) -> Any:
    user = render_user_prompt(spec, skill, deps)
    return await llm.create(
        model=settings.model,
        response_model=spec.output_model,
        messages=[
            {"role": "system", "content": prompts.system_prompt},
            {"role": "user", "content": user},
        ],
        max_retries=settings.max_retries,
    )


def _persist(settings: Settings, skill: SkillRecord, record: dict) -> None:
    path = result_path(settings, skill)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(record, ensure_ascii=False), encoding="utf-8")
    write_skill_output(settings, record)


async def run_one(
    llm, settings: Settings, prompts: PromptSet, skill: SkillRecord,
    force: bool = False, only: set[str] | None = None,
) -> tuple[dict, bool]:
    """Generate one skill's intros; returns (record, reused).

    Cache rules are identical for full runs and `only` runs: an existing
    result.json is trusted as-is (sync prunes artifacts whose upstream content
    changed), but every reused output must still validate against its current
    schema — missing or invalid prompts are regenerated, and prompts outside
    the selection are carried over from disk. Use force to regenerate the
    whole selection regardless of cache.
    """
    path = result_path(settings, skill)
    stored: dict[str, Any] = {}
    if path.exists():
        stored = json.loads(path.read_text(encoding="utf-8"))["intros"]

    targets = prompts.closure_ids(only) if only is not None else set(prompts.by_id)
    outputs: dict[str, Any] = {}
    generated = False
    for spec_id in prompts.ordered_ids():
        if spec_id not in targets:
            continue
        spec = prompts.by_id[spec_id]
        deps = {d: outputs[d] for d in spec.depends_on}
        if not force and spec_id in stored:
            try:
                outputs[spec_id] = spec.output_model.model_validate(stored[spec_id])
                continue
            except ValidationError:
                # stored output predates a schema/enum change: treat as missing
                pass
        generated = True
        outputs[spec_id] = await run_prompt(llm, settings, prompts, spec, skill, deps)

    if not generated:
        # nothing to do: every requested prompt is already cached and valid
        return {"skill": skill.to_dict(), "intros": stored}, True
    intros = {pid: out for pid, out in stored.items() if pid not in targets}
    intros.update({pid: out.model_dump(mode="json") for pid, out in outputs.items()})
    record = {"skill": skill.to_dict(), "intros": intros}
    _persist(settings, skill, record)
    return record, False


async def run_all(
    llm,
    settings: Settings,
    skills: list[SkillRecord],
    prompts: PromptSet,
    on_skill_done=None,
    force: bool = False,
    only: set[str] | None = None,
) -> list[dict]:
    """Generate intros for all skills concurrently, bounded by a semaphore.

    Skills with a complete, schema-valid result.json are skipped unless force
    is set; `only` narrows work to a subset of prompts (see run_one).
    """
    sem = asyncio.Semaphore(settings.concurrency)

    async def _one(skill: SkillRecord) -> dict:
        async with sem:
            record, reused = await run_one(llm, settings, prompts, skill, force, only)
        if on_skill_done:
            on_skill_done(skill, record, reused)
        return record

    return await asyncio.gather(*(_one(s) for s in skills))


def load_results(settings: Settings) -> list[dict]:
    """Load all per-skill result files, sorted by skill id."""
    root = settings.workdir / "results" / "skills"
    return [
        json.loads(p.read_text(encoding="utf-8")) for p in sorted(root.rglob("result.json"))
    ]
