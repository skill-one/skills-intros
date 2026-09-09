"""End-to-end CLI dry-run test (no network)."""

import json
import re

from typer.testing import CliRunner

from skills_intros.cli import app

runner = CliRunner()


def test_run_limit_counts_only_skills_that_generate(settings, monkeypatch):
    monkeypatch.setattr("skills_intros.cli.Settings", lambda: settings)

    result = runner.invoke(app, ["run", "--limit", "2", "--dry-run"])
    assert result.exit_code == 0, result.output
    assert "Processing 2 of 4 skills" in result.output
    assert "(cached)" not in result.output

    # those two are cached now: the budget goes to the next two, not back to them
    result = runner.invoke(app, ["run", "--limit", "2", "--dry-run"])
    assert result.exit_code == 0, result.output
    assert "Processing 2 of 4 skills" in result.output
    assert "gamma" in result.output
    assert "hotel" in result.output

    # everything is cached: nothing left to do
    result = runner.invoke(app, ["run", "--limit", "2", "--dry-run"])
    assert result.exit_code == 0, result.output
    assert "Processing 0 of 4 skills" in result.output


def test_invalidated_prompt_is_regenerated(settings, monkeypatch):
    monkeypatch.setattr("skills_intros.cli.Settings", lambda: settings)
    runner.invoke(app, ["run", "--limit", "2", "--dry-run"])

    result = runner.invoke(app, ["invalidate", "--prompts", "tagline"])
    assert result.exit_code == 0, result.output
    assert "Invalidated 2 output(s) across 2 skill(s)" in result.output

    result = runner.invoke(app, ["run", "--limit", "2", "--dry-run"])
    assert result.exit_code == 0, result.output
    assert "(cached)" not in result.output  # the taglines were regenerated


def test_invalidate_needs_all_to_wipe_everything(settings, monkeypatch):
    monkeypatch.setattr("skills_intros.cli.Settings", lambda: settings)
    runner.invoke(app, ["run", "--limit", "2", "--dry-run"])

    result = runner.invoke(app, ["invalidate"])
    assert result.exit_code != 0  # no filter, no --all: refuse

    result = runner.invoke(app, ["invalidate", "--all"])
    assert result.exit_code == 0, result.output
    result = runner.invoke(app, ["run", "--limit", "2", "--dry-run"])
    assert "(cached)" not in result.output


def test_run_writes_a_stats_summary(settings, monkeypatch):
    """A run logs a timed summary and overwrites output/stats.json with the
    counters, coverage and snapshot tag CI reads."""
    monkeypatch.setattr("skills_intros.cli.Settings", lambda: settings)
    result = runner.invoke(app, ["run", "--limit", "2", "--dry-run"])
    assert result.exit_code == 0, result.output
    assert "Done in" in result.output
    assert "14 prompt(s) generated for 2/2 skill(s)" in result.output  # 2 skills x 7 prompts
    assert "Coverage:" in result.output
    # progress lines list only the newly generated prompts, with seconds, no markers
    assert "*" not in result.output
    assert re.search(r"owner-a/repo-a/alpha: \S+ \d+\.\d+s", result.output)

    stats = json.loads((settings.output_dir / "stats.json").read_text(encoding="utf-8"))
    assert stats["run"]["selected"] == 2
    assert stats["run"]["skills_generated"] == 2
    assert stats["run"]["prompts_generated"] == 2 * 7
    assert stats["run"]["prompts_reused"] == 0
    assert stats["run"]["total_seconds"] >= 0
    assert stats["coverage"]["complete"] == 2
    assert stats["coverage"]["remaining"] == 2
    assert stats["coverage"]["skills"] == 4
    assert stats["model"]


def test_run_stats_snapshot_is_overwritten(settings, monkeypatch):
    """stats.json is a single snapshot: the latest run replaces it wholesale.

    The second run's budget moves to the next two skills (the first are cached),
    so its stats describe that batch — while coverage spans the whole dataset.
    """
    monkeypatch.setattr("skills_intros.cli.Settings", lambda: settings)
    runner.invoke(app, ["run", "--limit", "2", "--dry-run"])
    runner.invoke(app, ["run", "--limit", "2", "--dry-run"])

    stats = json.loads((settings.output_dir / "stats.json").read_text(encoding="utf-8"))
    assert stats["run"]["skills_generated"] == 2  # gamma and hotel, the next batch
    assert stats["run"]["prompts_generated"] == 2 * 7
    assert stats["coverage"]["complete"] == 4
    assert stats["coverage"]["remaining"] == 0


def test_sync_reports_tag_and_prunes(settings, monkeypatch):
    """The sync summary names the tag, cache hit vs download, and the prune count."""
    from skills_intros.data import SyncReport

    monkeypatch.setattr("skills_intros.cli.Settings", lambda: settings)
    monkeypatch.setattr(
        "skills_intros.cli.sync_data",
        lambda s, refresh: SyncReport(
            data_dir=s.data_dir, tag="dist-2026-09-09",
            downloaded=True, seconds=1.5, pruned=3,
        ),
    )
    result = runner.invoke(app, ["sync"])
    assert result.exit_code == 0, result.output
    assert "dist-2026-09-09" in result.output
    assert "downloaded" in result.output
    assert "invalidated 3 stale skill(s)" in result.output


def test_invalidate_rejects_unknown_prompt(settings, monkeypatch):
    monkeypatch.setattr("skills_intros.cli.Settings", lambda: settings)
    result = runner.invoke(app, ["invalidate", "--prompts", "nope"])
    assert result.exit_code != 0
    assert "unknown prompt" in result.output
