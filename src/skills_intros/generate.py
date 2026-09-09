"""DAG-driven generation; per-prompt files on disk act as the resume cache."""

import asyncio
import json
import logging
import sys
import time
from dataclasses import dataclass
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


@dataclass
class RunStats:
    """Aggregated counters for one `run`, tallied by `run_all`.

    `prompts_stale` counts reused-cached outputs that failed schema validation
    and were regenerated; `llm_seconds` sums the time spent inside `run_prompt`,
    so `llm_seconds / prompts_generated` is the average per-prompt latency.
    """

    selected: int = 0  # skills handed to run_all
    skills_generated: int = 0
    skills_skipped: int = 0  # no SKILL.md in the snapshot
    prompts_generated: int = 0
    prompts_reused: int = 0
    prompts_stale: int = 0
    llm_seconds: float = 0.0


def _tally(stats: RunStats, record: dict) -> None:
    """Fold one skill's record into the run stats."""
    generated = record.get("generated", ())
    stats.skills_generated += 1 if generated else 0
    stats.skills_skipped += 1 if record.get("skipped") else 0
    stats.prompts_generated += len(generated)
    stats.prompts_reused += len(record["intros"]) - len(generated)
    stats.prompts_stale += len(record.get("stale", ()))
    stats.llm_seconds += record.get("seconds", 0.0)


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


def _load_cached(
    settings: Settings, prompts: PromptSet, skill: SkillRecord, only: set[str] | None = None,
) -> tuple[dict[str, Any], list[str], list[str]]:
    """Split the selection into (cached outputs, prompt ids still to generate, stale ids).

    A prompt belongs to the selection when it is in `prompts` and (with `only`)
    in the closure of the requested ids. Its stored json is trusted as-is, but
    must still validate against the current schema — missing prompts come back
    as pending, schema-stale ones as stale (also pending, but counted apart).
    """
    targets = prompts.closure_ids(only) if only is not None else set(prompts.by_id)
    outputs: dict[str, Any] = {}
    stale: list[str] = []
    for spec_id in prompts.ordered_ids():
        if spec_id not in targets:
            continue
        stored = _read_prompt_output(settings, skill.id, spec_id)
        if stored is None:
            continue
        try:
            outputs[spec_id] = prompts.by_id[spec_id].output_model.model_validate(stored)
        except ValidationError:
            logger.debug("%s: stored %s no longer validates - regenerating", skill.id, spec_id)
            stale.append(spec_id)
    pending = [pid for pid in prompts.ordered_ids() if pid in targets and pid not in outputs]
    return outputs, pending, stale


def select_skills(
    settings: Settings,
    prompts: PromptSet,
    skills: list[SkillRecord],
    only: set[str] | None = None,
    limit: int | None = None,
) -> list[SkillRecord]:
    """The skills of this run: the first `limit` ones that still need work.

    Skills are considered in install order; one whose every selected prompt is
    already cached is skipped without spending any of the budget, so repeated
    runs keep moving down the list instead of re-scanning the same head.
    limit=None uses settings.limit; limit <= 0 selects every skill.
    """
    limit = settings.limit if limit is None else limit
    if limit <= 0:
        return list(skills)
    picked: list[SkillRecord] = []
    for skill in skills:
        if len(picked) == limit:
            break
        if _load_cached(settings, prompts, skill, only)[1]:
            picked.append(skill)
    return picked


def coverage(
    settings: Settings, prompts: PromptSet, skills: list[SkillRecord],
    only: set[str] | None = None,
) -> dict:
    """Cache coverage over all skills, for the run summary and stats.json.

    Applies the same cache rules as a run to every skill's stored outputs and
    returns {"skills", "complete", "remaining", "prompts"}: how many skills are
    complete (every selected prompt cached), how many still miss at least one,
    and, per prompt id, how many skills have it cached. Only called once per
    run: it re-reads every stored output.
    """
    targets = prompts.closure_ids(only) if only is not None else set(prompts.by_id)
    complete = 0
    per_prompt = dict.fromkeys(sorted(targets), 0)
    for skill in skills:
        outputs, pending, _ = _load_cached(settings, prompts, skill, only)
        if not pending:
            complete += 1
        for pid in outputs:
            per_prompt[pid] += 1
    return {
        "skills": len(skills),
        "complete": complete,
        "remaining": len(skills) - complete,
        "prompts": per_prompt,
    }


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

    The record carries run-bookkeeping besides the outputs: `generated` (prompt
    ids newly generated), `stale` (of those, ids whose cache was schema-stale),
    `seconds` (time spent inside the LLM) and `skipped` (no SKILL.md).
    """
    skill_dir = skill_result_dir(settings, skill.id)
    outputs, generated, stale = _load_cached(settings, prompts, skill, only)
    if not generated:
        return {"skill": skill.model_dump(), "intros": _dump(outputs)}, True

    skill_md = read_skill_md(settings, skill)
    if skill_md is None:
        logger.warning("%s: no SKILL.md in the snapshot - skipped", skill.id)
        return {"skill": skill.model_dump(), "intros": _dump(outputs), "skipped": True}, True
    skill = skill.model_copy(update={"skill_md": skill_md})

    seconds = 0.0
    for spec_id in generated:
        spec = prompts.by_id[spec_id]
        deps = {d: outputs[d] for d in spec.depends_on}
        start = time.monotonic()
        outputs[spec_id] = await run_prompt(llm, settings, prompts, spec, skill, deps, debug=debug)
        seconds += time.monotonic() - start
        write_prompt_output(settings, skill.id, spec_id, outputs[spec_id].model_dump(mode="json"))

    # a legacy single-file record has no meaning next to the per-prompt layout
    legacy = skill_dir / "result.json"
    if legacy.exists():
        legacy.unlink()

    return {
        "skill": skill.model_dump(),
        "intros": _dump(outputs),
        "generated": generated,
        "stale": stale,
        "seconds": seconds,
    }, False


async def run_all(
    llm,
    settings: Settings,
    skills: list[SkillRecord],
    prompts: PromptSet,
    on_skill_done: Callable[[SkillRecord, dict, bool], None] | None = None,
    only: set[str] | None = None,
    debug: bool = False,
    stats: RunStats | None = None,
) -> list[dict]:
    """Generate intros for all skills concurrently, bounded by a semaphore.

    Skills whose every requested prompt is already cached and valid are
    skipped; `only` narrows work to a subset of prompts (see run_one). When
    anything was generated, hashes.json is updated once, at the end. When
    `stats` is given, the run's counters are tallied into it.
    """
    sem = asyncio.Semaphore(settings.concurrency)

    async def _one(skill: SkillRecord) -> dict:
        async with sem:
            record, reused = await run_one(llm, settings, prompts, skill, only, debug)
        if on_skill_done:
            on_skill_done(skill, record, reused)
        if stats is not None:
            _tally(stats, record)
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
