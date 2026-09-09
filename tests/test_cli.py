"""End-to-end CLI dry-run test (no network)."""

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


def test_invalidate_rejects_unknown_prompt(settings, monkeypatch):
    monkeypatch.setattr("skills_intros.cli.Settings", lambda: settings)
    result = runner.invoke(app, ["invalidate", "--prompts", "nope"])
    assert result.exit_code != 0
    assert "unknown prompt" in result.output
