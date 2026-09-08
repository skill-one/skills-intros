"""DAG-driven generation; per-prompt files on disk act as the resume cache."""

import asyncio
import json
import logging
import sys
from pathlib import Path
from typing import Any, Callable

from pydantic import ValidationError

from .config import Settings
from .models import SkillRecord
from .outputs import (
    hashes_path,
    load_hashes,
    prompt_result_path,
    skill_result_dir,
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
    force: bool = False, only: set[str] | None = None, debug: bool = False,
    hashes: dict[str, str] | None = None,
) -> tuple[dict, bool]:
    """Generate one skill's intros; returns (record, reused).

    Storage: each prompt's output is its own <prompt_id>.json under the skill's
    results dir, committed (json+md) right after it is generated, so a crash
    keeps every completed prompt. results/hashes.json maps skill id -> the
    upstream hash the outputs were generated against; it is the index `sync`
    prunes against. The hash is registered only when this run actually
    generated something — a fully cached run leaves the disk untouched.

    Cache rules are identical for full runs and `only` runs: an existing
    per-prompt json is trusted as-is (sync prunes artifacts whose upstream
    content changed), but every reused output must still validate against its
    current schema — missing or invalid prompts are regenerated, and prompts
    outside the selection are simply not touched.

    force applies to the prompts the caller asked for (`only`, or every prompt
    when it is None); dependencies pulled in by the closure are inputs, so they
    keep the normal cache rules and are only computed when missing or invalid.
    """
    targets = prompts.closure_ids(only) if only is not None else set(prompts.by_id)
    forced = set(only) if only is not None else set(prompts.by_id)
    if hashes is None:
        hashes = load_hashes(settings)
    skill_dir = skill_result_dir(settings, skill.id)

    outputs: dict[str, Any] = {}
    generated = False
    for spec_id in prompts.ordered_ids():
        if spec_id not in targets:
            continue
        spec = prompts.by_id[spec_id]
        deps = {d: outputs[d] for d in spec.depends_on}
        stored = _read_prompt_output(settings, skill.id, spec_id)
        if not (force and spec_id in forced) and stored is not None:
            try:
                outputs[spec_id] = spec.output_model.model_validate(stored)
                continue
            except ValidationError:
                pass  # schema-stale: treat as missing
        generated = True
        outputs[spec_id] = await run_prompt(llm, settings, prompts, spec, skill, deps, debug=debug)
        write_prompt_output(settings, skill.id, spec_id, outputs[spec_id].model_dump(mode="json"))

    intros = {pid: out.model_dump(mode="json") for pid, out in outputs.items()}
    if not generated:
        return {"skill": skill.model_dump(), "intros": intros}, True

    if hashes.get(skill.id) != skill.hash:
        hashes[skill.id] = skill.hash
        hashes_path(settings).write_text(json.dumps(hashes, ensure_ascii=False), encoding="utf-8")

    # a legacy single-file record has no meaning next to the per-prompt layout
    legacy = skill_dir / "result.json"
    if legacy.exists():
        legacy.unlink()

    return {"skill": skill.model_dump(), "intros": intros}, False


async def run_all(
    llm,
    settings: Settings,
    skills: list[SkillRecord],
    prompts: PromptSet,
    on_skill_done: Callable[[SkillRecord, dict, bool], None] | None = None,
    force: bool = False,
    only: set[str] | None = None,
    debug: bool = False,
) -> list[dict]:
    """Generate intros for all skills concurrently, bounded by a semaphore.

    Skills whose every requested prompt is already cached and valid are skipped
    unless force is set; `only` narrows work to a subset of prompts (see run_one).
    """
    sem = asyncio.Semaphore(settings.concurrency)
    hashes = load_hashes(settings)

    async def _one(skill: SkillRecord) -> dict:
        async with sem:
            record, reused = await run_one(llm, settings, prompts, skill, force, only, debug, hashes)
        if on_skill_done:
            on_skill_done(skill, record, reused)
        return record

    return await asyncio.gather(*(_one(s) for s in skills))


def load_results(settings: Settings) -> list[dict]:
    """Load all per-skill result records, sorted by skill id.

    A directory counts as a result if hashes.json has an entry for it (the
    index is what sync prunes against); its outputs are reassembled from the
    per-prompt json files. A stray legacy result.json is not an output.
    """
    hashes = load_hashes(settings)
    results: list[dict] = []
    for skill_id, stored_hash in sorted(hashes.items()):
        skill_dir = skill_result_dir(settings, skill_id)
        intros: dict[str, Any] = {}
        for json_file in sorted(skill_dir.glob("*.json")):
            if json_file.name == "result.json":
                continue
            try:
                intros[json_file.stem] = json.loads(json_file.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                logger.warning("Skipping unreadable %s", json_file)
        results.append({"skill": {"id": skill_id, "hash": stored_hash}, "intros": intros})
    return results
