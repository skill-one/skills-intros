"""Write one markdown file per prompt output under results/skills/<id>/."""

from pathlib import Path

from .config import Settings
from .models import Domain


def write_skill_output(settings: Settings, record: dict) -> Path:
    """Write one markdown file per prompt output under results/skills/<id>/."""
    s, intros = record["skill"], record["intros"]
    skill_dir = settings.workdir / "results" / "skills" / s["id"].replace(":", "_")
    skill_dir.mkdir(parents=True, exist_ok=True)
    name = s["id"].rsplit("/", 1)[-1]
    for prompt_id, output in intros.items():
        lines = [
            f"# {name} (`{s['id']}`)",
            "",
            f"## {prompt_id}",
            "",
        ]
        lines += _render_output(output)
        (skill_dir / f"{prompt_id}.md").write_text(
            "\n".join(lines).rstrip() + "\n", encoding="utf-8"
        )
    return skill_dir


def write_skill_outputs(settings: Settings, results: list[dict]) -> Path:
    skills_dir = settings.workdir / "results" / "skills"
    skills_dir.mkdir(parents=True, exist_ok=True)
    for record in results:
        write_skill_output(settings, record)
    return skills_dir


def _render_output(output: dict) -> list[str]:
    """Generic markdown rendering: lists become bullets, strings become paragraphs."""
    lines: list[str] = []
    for key, value in output.items():
        if isinstance(value, list):
            lines += [f"- {item}" for item in value]
        elif len(output) > 1:
            if isinstance(value, str):
                value = Domain.display(value)  # known domain values get their emoji
            lines.append(f"**{key}**: {value}")
        else:
            lines.append(str(value))
        lines.append("")
    return lines
