"""DAG-driven generation; per-prompt files on disk act as the resume cache."""

import asyncio
import json
import logging
import sys
from pathlib import Path
from typing import Any, Callable

from pydantic import ValidationError

from .config import Settings
from .data import read_skill_md
from .models import SkillRecord
from .outputs import (
    load_hashes,
    prompt_result_path,
    skill_result_dir,
    write_hashes,
    write_prompt_output,
)
from .prompts import PromptSet, PromptSpec, render_user_prompt

logger = logging.getLogger(__name__)


def _dump_messages(skill: SkillRecord, spec, messages: list[dict]) -> None:
    print(f"\n===== debug {skill.id} / {spec.id} =====", file=sys.stderr)
    for message in messages:
        print(f"----- {message['role']} -----", file=sys.stderr)
        print(message["content"], file=sys.stderr)


def _read_prompt_output(settings: Settings, skill_id: str, prompt_id: str) -> Any:
    """One prompt's stored output dict, or None if absent or unreadable."""
    path = prompt_result_path(settings, skill_id, prompt_id)
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def _dump(outputs: dict[str, Any]) -> dict[str, Any]:
    """Every prompt output as a plain dict, keyed by prompt id."""
    return {pid: out.model_dump(mode="json") for pid, out in outputs.items()}


async def run_prompt(
    llm, settings: Settings, prompts: PromptSet, spec: PromptSpec, skill: SkillRecord, deps: dict,
    debug: bool = False,
) -> Any:
    messages = [
        {"role": "system", "content": prompts.render_system_prompt(skill)},
        {"role": "user", "content": render_user_prompt(spec, deps)},
    ]
    if debug:
        _dump_messages(skill, spec, messages)
    return await llm.create(
        model=settings.model,
        response_model=spec.output_model,
        messages=messages,
        max_retries=settings.max_retries,
    )


async def run_one(
    llm, settings: Settings, prompts: PromptSet, skill: SkillRecord,
    only: set[str] | None = None, debug: bool = False,
) -> tuple[dict, bool]:
    """Generate one skill's intros; returns (record, reused).

    Storage: each prompt's output is its own <prompt_id>.json under the skill's
    artifact dir, committed (json + md/ copy) right after it is generated, so a
    crash keeps every completed prompt. `run_all` records the content hash of
    the skills that generated something in hashes.json, the record `sync` prunes
    against — a fully cached run leaves the disk untouched.

    Cache rule: an existing per-prompt json is trusted as-is (invalidation is
    `sync`'s and `invalidate`'s job), but every reused output must still
    validate against its current schema — missing or invalid prompts are
    regenerated, and prompts outside the selection (`only`, plus the closure of
    their dependencies) are simply not touched.

    The skill's SKILL.md is read from the local snapshot only once something has
    to be generated, so a fully cached skill reads nothing at all.
    """
    targets = prompts.closure_ids(only) if only is not None else set(prompts.by_id)
    skill_dir = skill_result_dir(settings, skill.id)

    outputs: dict[str, Any] = {}
    generated: list[str] = []
    for spec_id in prompts.ordered_ids():
        if spec_id not in targets:
            continue
        spec = prompts.by_id[spec_id]
        stored = _read_prompt_output(settings, skill.id, spec_id)
        if stored is not None:
            try:
                outputs[spec_id] = spec.output_model.model_validate(stored)
                continue
            except ValidationError:
                pass  # schema-stale: treat as missing
        generated.append(spec_id)

    if not generated:
        return {"skill": skill.model_dump(), "intros": _dump(outputs)}, True

    skill_md = read_skill_md(settings, skill)
    if skill_md is None:
        logger.warning("%s: no SKILL.md in the snapshot - skipped", skill.id)
        return {"skill": skill.model_dump(), "intros": _dump(outputs)}, True
    skill = skill.model_copy(update={"skill_md": skill_md})

    for spec_id in generated:
        spec = prompts.by_id[spec_id]
        deps = {d: outputs[d] for d in spec.depends_on}
        outputs[spec_id] = await run_prompt(llm, settings, prompts, spec, skill, deps, debug=debug)
        write_prompt_output(settings, skill.id, spec_id, outputs[spec_id].model_dump(mode="json"))

    # a legacy single-file record has no meaning next to the per-prompt layout
    legacy = skill_dir / "result.json"
    if legacy.exists():
        legacy.unlink()

    return {"skill": skill.model_dump(), "intros": _dump(outputs), "generated": generated}, False


async def run_all(
    llm,
    settings: Settings,
    skills: list[SkillRecord],
    prompts: PromptSet,
    on_skill_done: Callable[[SkillRecord, dict, bool], None] | None = None,
    only: set[str] | None = None,
    debug: bool = False,
) -> list[dict]:
    """Generate intros for all skills concurrently, bounded by a semaphore.

    Skills whose every requested prompt is already cached and valid are
    skipped; `only` narrows work to a subset of prompts (see run_one). When
    anything was generated, hashes.json is updated once, at the end.
    """
    sem = asyncio.Semaphore(settings.concurrency)

    async def _one(skill: SkillRecord) -> dict:
        async with sem:
            record, reused = await run_one(llm, settings, prompts, skill, only, debug)
        if on_skill_done:
            on_skill_done(skill, record, reused)
        return record

    records = await asyncio.gather(*(_one(s) for s in skills))
    _update_hashes(settings, records)
    return records


def _update_hashes(settings: Settings, records: list[dict]) -> None:
    """Record the content hash of every skill that generated something.

    hashes.json (skill id -> hash) is the sole freshness record: `sync` compares
    it against the new snapshot to decide what to invalidate. Skills that were
    already complete keep their hash; a run that generated nothing writes nothing.
    """
    fresh = {r["skill"]["id"]: r["skill"]["hash"] for r in records if r.get("generated")}
    if not fresh:
        return
    hashes = load_hashes(settings)
    hashes.update(fresh)
    write_hashes(settings, hashes)


def load_results(settings: Settings) -> list[dict]:
    """Load all per-skill result records, sorted by skill id.

    A directory counts as a result if hashes.json has the skill on record (the
    record sync prunes against); its outputs are reassembled from the per-prompt
    json files. A stray legacy result.json is not an output.
    """
    results: list[dict] = []
    for skill_id, hash_ in sorted(load_hashes(settings).items()):
        entry = {"id": skill_id, "hash": hash_}
        skill_dir = skill_result_dir(settings, skill_id)
        intros: dict[str, Any] = {}
        for json_file in sorted(skill_dir.glob("*.json")):
            if json_file.name == "result.json":
                continue
            try:
                intros[json_file.stem] = json.loads(json_file.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                logger.warning("Skipping unreadable %s", json_file)
        results.append({"skill": entry, "intros": intros})
    return results
