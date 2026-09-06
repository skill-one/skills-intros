"""End-to-end CLI dry-run test (no network)."""

from typer.testing import CliRunner

from skills_intros.cli import app

runner = CliRunner()


def test_run_dry_run_and_report(settings, monkeypatch):
    monkeypatch.setattr("skills_intros.cli.Settings", lambda: settings)

    result = runner.invoke(app, ["run", "--top", "2", "--dry-run"])
    assert result.exit_code == 0, result.output
    assert "Processing 2 skills" in result.output
    assert "(cached)" not in result.output

    # a second run reuses the on-disk results without regenerating
    result = runner.invoke(app, ["run", "--top", "2", "--dry-run"])
    assert result.exit_code == 0, result.output
    assert result.output.count("(cached)") == 2

    # --force regenerates even when results exist
    result = runner.invoke(app, ["run", "--top", "2", "--dry-run", "--force"])
    assert result.exit_code == 0, result.output
    assert "(cached)" not in result.output
