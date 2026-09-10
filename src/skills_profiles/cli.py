"""Typer CLI: sync / invalidate / run."""

import asyncio
import logging
import time

import typer

from .config import Settings
from .data import load_skills, stale_result_ids, sync_data
from .generate import RunStats, coverage, run_all, select_skills, write_artifact_stats
from .llm import FakeLLM, make_llm
from .logging import setup_logging
from .outputs import invalidate as invalidate_cache
from .outputs import load_hashes
from .prompts import load_prompt_set

logger = logging.getLogger(__name__)

app = typer.Typer(help="Generate multi-angle Chinese profiles for agent skills.")


@app.command()
def sync(
    refresh: bool = typer.Option(
        False, "--refresh",
        help="Download the snapshot again even when it is already the newest tag",
    ),
) -> None:
    """Download the newest dist snapshot (skills.jsonl + every SKILL.md) as one
    tarball into the data dir. Sync never touches the generated results; invalidating
    stale ones is `invalidate --stale`'s explicit job.

    Upstream tags each daily scrape; a sync whose tag is already on disk does
    nothing, so repeat syncs cost one small request instead of a download.
    """
    setup_logging()
    try:
        report = sync_data(Settings(), refresh)
    except RuntimeError as e:
        logger.error("%s", e)
        raise typer.Exit(1)
    fetched = (f"downloaded {report.tag} in {report.seconds:.1f}s" if report.downloaded
               else f"already at {report.tag}")
    typer.echo(f"Dataset ready at {report.data_dir} ({fetched})")


@app.command()
def invalidate(
    skill: list[str] = typer.Option(
        None, "--skill", help="Skill id to invalidate; repeatable. Omit for every skill"
    ),
    prompts_opt: str | None = typer.Option(
        None, "--prompts", help="Comma-separated prompt ids; omit for every prompt"
    ),
    all_skills: bool = typer.Option(
        False, "--all", help="Allow invalidating every skill (required when no filter is given)"
    ),
    stale: bool = typer.Option(
        False, "--stale",
        help="Select every cached skill whose upstream content hash changed or that "
             "vanished from the snapshot (run `sync` first to have a fresh snapshot)",
    ),
) -> None:
    """Drop cached outputs so the next `run` regenerates them."""
    setup_logging()
    settings = Settings()

    prompt_ids: set[str] | None = None
    if prompts_opt:
        prompt_ids = {p.strip() for p in prompts_opt.split(",") if p.strip()}
        known = set(load_prompt_set(settings.prompts_dir).by_id)
        unknown = prompt_ids - known
        if unknown:
            raise typer.BadParameter(
                f"unknown prompt(s) {sorted(unknown)}; available: {sorted(known)}"
            )

    skill_ids = list(skill or [])
    if stale:
        found = stale_result_ids(settings)
        logger.info("%d stale skill(s): upstream content changed or skill gone", len(found))
        skill_ids = list(dict.fromkeys(skill_ids + found))
        if not found:
            logger.info("Nothing to invalidate")
            return
    if not skill_ids and not prompt_ids and not all_skills:
        raise typer.BadParameter("refusing to invalidate everything - pass --all to confirm")

    recorded = load_hashes(settings)
    for skill_id in skill_ids:
        if skill_id not in recorded:
            logger.warning("%s has no cached results", skill_id)
    removed = invalidate_cache(settings, skill_ids or None, prompt_ids)
    targets = sorted(skill_ids) if skill_ids else sorted(recorded)
    logger.info("Invalidated %d output(s) across %d skill(s)", removed, len(targets))


@app.command()
def run(
    limit: int | None = typer.Option(
        None, "--limit",
        help="How many skills to generate this run, most installed first "
             "(0 = every skill with missing prompts). Skills whose selected prompts "
             "are all cached, or that have no SKILL.md in the snapshot, are skipped "
             "and do not count",
    ),
    concurrency: int | None = typer.Option(
        None, "--concurrency",
        help="Max concurrent LLM calls shared across skills and prompts "
             "(defaults to SKILLS_PROFILES_CONCURRENCY or 2)",
    ),
    prompts_opt: str | None = typer.Option(
        None, "--prompts",
        help="Comma-separated prompt ids to fill in, e.g. 'tagline'. Cached outputs are "
             "reused under the same rules as a full run; use `invalidate` to drop them. "
             "Prompts outside the selection are carried over",
    ),
    dry_run: bool = typer.Option(False, "--dry-run", help="Use a fake LLM, no API calls"),
    debug: bool = typer.Option(
        False, "--debug", help="Dump the rendered system/user prompts to stderr"
    ),
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Enable debug logging"
    ),
) -> None:
    """Generate missing profiles; every cached and valid prompt output is reused."""
    setup_logging(verbose)
    settings = Settings()
    if limit is not None:
        settings.limit = limit
    if concurrency is not None:
        settings.concurrency = concurrency

    prompt_set = load_prompt_set(settings.prompts_dir)
    only = None
    if prompts_opt:
        ids = {p.strip() for p in prompts_opt.split(",") if p.strip()}
        unknown = ids - set(prompt_set.by_id)
        if unknown:
            raise typer.BadParameter(
                f"unknown prompt(s) {sorted(unknown)}; available: {sorted(prompt_set.by_id)}"
            )
        only = ids

    start = time.monotonic()
    skills = load_skills(settings)
    selected = select_skills(settings, prompt_set, skills, only)
    setup_seconds = time.monotonic() - start
    logger.info("Processing %d of %d skills with model=%s%s",
                len(selected), len(skills), settings.model,
                " (dry-run)" if dry_run else "")

    done = 0

    def on_done(_skill, _record, reused: bool) -> None:
        nonlocal done
        done += 1
        if _record.get("failed"):
            detail = "(failed)"
        elif _record.get("skipped"):
            detail = "(skipped: no SKILL.md)"
        elif reused:
            detail = "(cached)"
        else:
            detail = f"{','.join(sorted(_record.get('generated', ())))} " \
                     f"{_record.get('seconds', 0.0):.1f}s"
        logger.info("  [%d/%d] %s: %s", done, len(selected), _skill.id, detail)

    llm = FakeLLM() if dry_run else make_llm(settings)
    stats = RunStats(selected=len(selected))
    generate_start = time.monotonic()
    results = asyncio.run(
        run_all(llm, settings, selected, prompt_set, on_skill_done=on_done,
                only=only, debug=debug, stats=stats)
    )
    generate_seconds = time.monotonic() - generate_start
    total_seconds = time.monotonic() - start

    cov = coverage(settings, prompt_set, skills, only)
    avg = stats.llm_seconds / stats.prompts_generated if stats.prompts_generated else 0.0
    logger.info(
        "Done in %.1fs (setup %.1fs, generate %.1fs): %d prompt(s) generated for %d/%d "
        "skill(s), %d reused, %d stale cache(s), %d skipped (no SKILL.md), %d failed",
        total_seconds, setup_seconds, generate_seconds,
        stats.prompts_generated, stats.skills_generated, len(selected),
        stats.prompts_reused, stats.prompts_stale, stats.skills_skipped,
        stats.skills_failed,
    )
    if stats.prompts_generated:
        logger.info("LLM: %d call(s), %.1fs total, %.2fs average per prompt",
                    stats.prompts_generated, stats.llm_seconds, avg)
    # stats.json is the artifact's state, not the run's: what is on disk right
    # now, against which snapshot. Run counters and timings stay in the log.
    artifact = write_artifact_stats(settings, cov)
    logger.info(
        "Coverage: %d/%d skill(s) complete, %d remaining, %d stale (upstream changed; "
        "see `invalidate --stale`) | cached prompts: %s",
        cov["complete"], cov["skills"], cov["remaining"], artifact["skills"]["stale"],
        ", ".join(f"{pid} {n}/{cov['skills']}" for pid, n in cov["prompts"].items()),
    )
    # partial failure is not an error: completed prompts are on disk and get
    # published, the rest regenerates on the next run. A total washout (every
    # selected skill failed) is one: it almost always means a systemic problem
    # (bad key, endpoint down) and retrying here would not help.
    if stats.skills_failed:
        logger.warning("%d skill(s) failed - see the errors above", stats.skills_failed)
    if stats.skills_failed and stats.skills_failed == len(selected):
        logger.error("Every selected skill failed - refusing to report success")
        raise typer.Exit(1)


def main() -> None:  # pragma: no cover
    app()


if __name__ == "__main__":
    app()
