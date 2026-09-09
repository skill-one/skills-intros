"""Typer CLI: sync / invalidate / run."""

import asyncio
import logging

import typer

from .config import Settings
from .data import load_skills, sync_data
from .generate import run_all
from .llm import FakeLLM, make_llm
from .logging import setup_logging
from .outputs import invalidate as invalidate_cache
from .outputs import load_hashes
from .prompts import load_prompt_set

logger = logging.getLogger(__name__)

app = typer.Typer(help="Generate multi-angle Chinese introductions for agent skills.")


@app.command()
def sync() -> None:
    """Download the whole dist branch (skills.jsonl + every SKILL.md) as one
    tarball into the data dir, and prune results that went stale."""
    setup_logging()
    try:
        data_dir, pruned = sync_data(Settings())
    except RuntimeError as e:
        logger.error("%s", e)
        raise typer.Exit(1)
    message = f"Dataset ready at {data_dir}"
    if pruned:
        message += f" (invalidated {pruned} stale skill(s) whose upstream content changed)"
    typer.echo(message)


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
    if not skill and not prompt_ids and not all_skills:
        raise typer.BadParameter("refusing to invalidate everything - pass --all to confirm")

    recorded = load_hashes(settings)
    for skill_id in skill or ():
        if skill_id not in recorded:
            logger.warning("%s has no cached results", skill_id)
    removed = invalidate_cache(settings, skill or None, prompt_ids)
    targets = sorted(skill) if skill else sorted(recorded)
    logger.info("Invalidated %d output(s) across %d skill(s)", removed, len(targets))


@app.command()
def run(
    top: int | None = typer.Option(
        None, "--top", help="How many top skills to process (0 = all usable skills)"
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
    """Generate missing intros; every cached and valid prompt output is reused."""
    setup_logging(verbose)
    settings = Settings()
    if top is not None:
        settings.top_n = top

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

    skills = load_skills(settings)
    logger.info("Processing %d skills with model=%s%s",
                len(skills), settings.model, " (dry-run)" if dry_run else "")

    done = 0

    def on_done(_skill, _record, reused: bool) -> None:
        nonlocal done
        done += 1
        fresh = set(_record.get("generated", ()))
        parts = [pid + ("*" if pid in fresh else "") for pid in sorted(_record["intros"])]
        marker = " (cached)" if reused else ""
        logger.info("  [%d/%d] %s: %s%s", done, len(skills), _skill.id, ",".join(parts), marker)

    llm = FakeLLM() if dry_run else make_llm(settings)
    results = asyncio.run(
        run_all(llm, settings, skills, prompt_set, on_skill_done=on_done,
                only=only, debug=debug)
    )
    logger.info("Wrote %d records under %s", len(results), settings.output_dir / "skills")


def main() -> None:  # pragma: no cover
    app()


if __name__ == "__main__":
    app()
