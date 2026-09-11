"""Typer CLI: sync / invalidate / run."""

import asyncio
import logging
import time
from typing import Callable

import typer

from .config import Settings
from .data import load_skills, portfolio, stale_result_ids, sync_data
from .generate import RunStats, coverage, run_all, select_skills, write_artifact_stats
from .images import CoverStats, FakeImages, cover_needed, make_images, run_covers
from .llm import FakeLLM, make_llm
from .logging import setup_logging
from .models import SkillRecord
from .outputs import invalidate as invalidate_cache
from .outputs import load_hashes
from .prompts import load_prompt_set

logger = logging.getLogger(__name__)

app = typer.Typer(help="Generate multi-angle Chinese profiles for agent skills.")


def cover_progress(total: int) -> Callable[[SkillRecord, int | None], None]:
    """The per-skill logger of `run`'s rendering post-pass."""
    done = 0

    def on_done(_skill: SkillRecord, written: int | None) -> None:
        nonlocal done
        done += 1
        if written is None:
            detail = "(failed)"
        elif written >= 1_048_576:
            detail = f"{written / 1_048_576:.1f} MB"
        else:
            detail = f"{written / 1024:.0f} KB"
        logger.info("  [%d/%d] %s: %s", done, total, _skill.id, detail)

    return on_done


def served_skills(settings: Settings) -> list[SkillRecord]:
    """The snapshot narrowed to the pipeline's window (`data.portfolio`).

    Where `run` starts, so the one dataset ceiling (`SKILLS_PROFILES_TOTAL_LIMIT`)
    bounds profiles and pictures alike; the cap is only announced when it trims.
    """
    every_skill = load_skills(settings)
    skills = portfolio(settings, every_skill)
    if len(skills) < len(every_skill):
        logger.info("Serving the top %d of %d installed skills (total_limit=%d); "
                    "the rest are never profiled or drawn",
                    len(skills), len(every_skill), settings.total_limit)
    return skills


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
        help="How many skills to complete this run, most installed first "
             "(0 = every skill with gaps). A skill is complete when every prompt "
             "is cached and its cover.png is drawn; skills that need nothing, or "
             "have no SKILL.md in the snapshot, are skipped and do not count",
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
    """Complete skills: fill missing profiles, then render their missing covers.

    `--limit N` means "make N skills complete": the selection counts a skill
    that is missing any prompt or whose cover.png has not been drawn yet, and
    the run fills both halves for exactly the skills it selected. Rendering is
    paced at `SKILLS_PROFILES_IMAGE_RATE_LIMIT` images/minute per key (default
    2); without an image key the post-pass is skipped with a warning and picked
    up by a later run once the key is set.
    """
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
    skills = served_skills(settings)
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

    covers_stats = CoverStats()
    covers_seconds = 0.0
    if not dry_run and not settings.image_keys:
        logger.warning("no image endpoint key (SKILLS_PROFILES_IMAGE_API_KEY) - "
                       "covers not rendered; the next run picks them up once the key is set")
    else:
        # `limit` already counted cover-less skills (see select_skills): render
        # exactly the pictures this run's skills are missing, nothing past it
        pending = [s for s in selected if cover_needed(settings, s.id)]
        if pending:
            logger.info("Rendering %d pending cover(s) with model=%s size=%s%s",
                        len(pending), settings.image_model, settings.image_size,
                        " (dry-run)" if dry_run else "")
            images = FakeImages() if dry_run else make_images(settings)
            covers_start = time.monotonic()
            asyncio.run(run_covers(images, settings, pending,
                                   on_skill_done=cover_progress(len(pending)),
                                   stats=covers_stats))
            covers_seconds = time.monotonic() - covers_start
    total_seconds = time.monotonic() - start

    cov = coverage(settings, prompt_set, skills, only)
    avg = stats.llm_seconds / stats.prompts_generated if stats.prompts_generated else 0.0
    logger.info(
        "Done in %.1fs (setup %.1fs, generate %.1fs, covers %.1fs): %d prompt(s) "
        "generated for %d/%d skill(s), %d reused, %d stale cache(s), %d skipped "
        "(no SKILL.md), %d failed; %d cover(s) rendered, %d failed",
        total_seconds, setup_seconds, generate_seconds, covers_seconds,
        stats.prompts_generated, stats.skills_generated, len(selected),
        stats.prompts_reused, stats.prompts_stale, stats.skills_skipped,
        stats.skills_failed, covers_stats.rendered, covers_stats.skills_failed,
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
