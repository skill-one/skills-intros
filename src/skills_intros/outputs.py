"""On-disk results layout: one json+md pair per prompt under results/skills/<id>/,
plus results/hashes.json (skill id -> upstream content hash) as sync's prune index."""

import json
import logging
from pathlib import Path

from .config import Settings
from .models import Domain

logger = logging.getLogger(__name__)


def skill_result_dir(settings: Settings, skill_id: str) -> Path:
    """Per-skill results live under results/skills/<owner>/<repo>/<slug>/ (id-based,
    mirroring the upstream data/skills/ layout)."""
    return settings.workdir / "results" / "skills" / skill_id.replace(":", "_")


def prompt_result_path(settings: Settings, skill_id: str, prompt_id: str) -> Path:
    """The json file holding one prompt's structured output."""
    return skill_result_dir(settings, skill_id) / f"{prompt_id}.json"


def hashes_path(settings: Settings) -> Path:
    """The prune index: skill id -> the upstream hash its outputs were generated against."""
    return settings.workdir / "results" / "hashes.json"


def load_hashes(settings: Settings) -> dict[str, str]:
    """The prune index; absent or unreadable file means 'nothing known' ({})."""
    try:
        hashes = json.loads(hashes_path(settings).read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        logger.warning("%s is unreadable - treating as empty", hashes_path(settings))
        return {}
    if not isinstance(hashes, dict):
        logger.warning("%s is not an object - treating as empty", hashes_path(settings))
        return {}
    return hashes


def write_prompt_output(settings: Settings, skill_id: str, prompt_id: str, output: dict) -> Path:
    """Write one prompt's output as <prompt_id>.md + <prompt_id>.json.

    Markdown first, json last: the json is the commit marker, so a crash can
    only leave a stray markdown (regenerated together with the json next run),
    never a valid-looking json without its markdown.
    """
    skill_dir = skill_result_dir(settings, skill_id)
    skill_dir.mkdir(parents=True, exist_ok=True)
    (skill_dir / f"{prompt_id}.md").write_text(
        _render_markdown(skill_id, prompt_id, output), encoding="utf-8"
    )
    (skill_dir / f"{prompt_id}.json").write_text(
        json.dumps(output, ensure_ascii=False), encoding="utf-8"
    )
    return skill_dir


def _render_markdown(skill_id: str, prompt_id: str, output: dict) -> str:
    name = skill_id.rsplit("/", 1)[-1]
    lines = [f"# {name} (`{skill_id}`)", "", f"## {prompt_id}", ""]
    lines += _render_output(output)
    return "\n".join(lines).rstrip() + "\n"


def _render_output(output: dict) -> list[str]:
    """Generic markdown rendering: lists become bullets, strings become paragraphs."""
    lines: list[str] = []
    for key, value in output.items():
        if isinstance(value, list):
            if value and isinstance(value[0], dict):
                for item in value:
                    lines.append(f"- {_render_dict(item)}")
            else:
                lines.extend(f"- {item}" for item in value)
        elif isinstance(value, dict):
            lines.append(_render_dict(value))
        elif len(output) > 1:
            if isinstance(value, str):
                value = Domain.display(value)  # known domain values get their emoji
            lines.append(f"**{key}**: {value}")
        else:
            lines.append(str(value))
        lines.append("")
    return lines


def _render_dict(d: dict) -> str:
    """Render a dict as 'key: value, key: value'."""
    return ", ".join(f"{k}: {v}" for k, v in d.items())
