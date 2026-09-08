"""Typer CLI: sync / run."""

import asyncio
import logging

import typer

from .config import Settings
from .data import load_skills, sync_data
from .generate import run_all
from .llm import FakeLLM, make_llm
from .logging import setup_logging
from .prompts import load_prompt_set

logger = logging.getLogger(__name__)

app = typer.Typer(help="Generate multi-angle Chinese introductions for agent skills.")


@app.command()
def sync() -> None:
    """Download the skills dataset snapshot (dist branch) into output/data."""
    setup_logging()
    try:
        data_dir, pruned = sync_data(Settings())
    except RuntimeError as e:
        logger.error("%s", e)
        raise typer.Exit(1)
    message = f"Dataset ready at {data_dir}"
    if pruned:
        message += f" (pruned {pruned} stale result dir(s) whose upstream content changed)"
    typer.echo(message)


@app.command()
def run(
    top: int | None = typer.Option(
        None, "--top", help="How many top skills to process (0 = all usable skills)"
    ),
    prompts_opt: str | None = typer.Option(
        None, "--prompts",
        help="Comma-separated prompt ids to fill in, e.g. 'tagline'. Cached outputs are "
             "reused under the same rules as a full run; use --force to regenerate. "
             "Prompts outside the selection are carried over",
    ),
    force: bool = typer.Option(
        False, "--force", help="Regenerate regardless of existing results or content hash. "
                              "Applies to --prompts only when given: their dependencies are "
                              "reused from cache unless missing or invalid"
    ),
    dry_run: bool = typer.Option(False, "--dry-run", help="Use a fake LLM, no API calls"),
    debug: bool = typer.Option(
        False, "--debug", help="Dump the rendered system/user prompts to stderr"
    ),
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Enable debug logging"
    ),
) -> None:
    """Generate intros; skills with up-to-date results are skipped unless --force."""
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
        marker = " (cached)" if reused else (f" ({'+'.join(sorted(only))})" if only else "")
        logger.info("  [%d/%d] %s%s", done, len(skills), _skill.id, marker)

    llm = FakeLLM() if dry_run else make_llm(settings)
    results = asyncio.run(
        run_all(llm, settings, skills, prompt_set, on_skill_done=on_done,
                force=force, only=only, debug=debug)
    )
    logger.info("Wrote %d records under %s", len(results), settings.workdir / "results" / "skills")


def main() -> None:  # pragma: no cover
    app()


if __name__ == "__main__":
    app()
