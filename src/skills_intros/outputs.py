"""On-disk artifact layout under <output_dir>: one json per prompt in
skills/<id>/ (with a markdown copy in md/), plus hashes.json — skill id -> the
upstream content hash its intros were generated from, which is all `sync` needs
to decide what to invalidate."""

import json
import shutil
from collections.abc import Iterable
from pathlib import Path
from typing import Mapping

from .config import Settings
from .models import Domain

MD_SUBDIR = "md"  # markdown browsing copies, kept out of the json directory


def skill_result_dir(settings: Settings, skill_id: str) -> Path:
    """Per-skill artifacts live under <output_dir>/skills/<owner>/<repo>/<slug>/
    (id-based, mirroring the upstream data/skills/ layout)."""
    return settings.output_dir / "skills" / skill_id.replace(":", "_")


def prompt_result_path(settings: Settings, skill_id: str, prompt_id: str) -> Path:
    """The json file holding one prompt's structured output."""
    return skill_result_dir(settings, skill_id) / f"{prompt_id}.json"


def prompt_markdown_path(settings: Settings, skill_id: str, prompt_id: str) -> Path:
    """The markdown copy of one prompt's output; kept in a `md/` subdir so the
    skill directory itself only holds json."""
    return skill_result_dir(settings, skill_id) / MD_SUBDIR / f"{prompt_id}.md"


def hashes_path(settings: Settings) -> Path:
    """The invalidation record: skill id -> upstream content hash."""
    return settings.output_dir / "hashes.json"


def load_hashes(settings: Settings) -> dict[str, str]:
    """skill id -> the hash its intros were generated from; {} when unknown."""
    try:
        return json.loads(hashes_path(settings).read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {}


def write_hashes(settings: Settings, hashes: Mapping[str, str]) -> None:
    """Rewrite the whole record, sorted by skill id."""
    path = hashes_path(settings)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(dict(sorted(hashes.items())), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def write_stats(settings: Settings, stats: Mapping) -> Path:
    """Overwrite output/stats.json: the artifact's current state, not the run's.

    How many skills are complete/remaining and how many skills hold each
    prompt's output on disk, plus the snapshot tag the artifacts were built
    from. Run counters and timings stay in the log; one snapshot file (no
    history) so CI and humans read the same place. Sorting dict keys keeps the
    layout stable across runs.
    """
    path = settings.output_dir / "stats.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(stats, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return path


def write_prompt_output(settings: Settings, skill_id: str, prompt_id: str, output: dict) -> Path:
    """Write one prompt's output as json in the skill dir + a markdown copy in md/.

    Markdown first, json last: the json is the commit marker, so a crash can
    only leave a stray markdown (regenerated together with the json next run),
    never a valid-looking json without its markdown.
    """
    skill_dir = skill_result_dir(settings, skill_id)
    md_path = prompt_markdown_path(settings, skill_id, prompt_id)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text(_render_markdown(skill_id, prompt_id, output), encoding="utf-8")
    (skill_dir / f"{prompt_id}.json").write_text(
        json.dumps(output, ensure_ascii=False), encoding="utf-8"
    )
    return skill_dir


def invalidate(settings: Settings, skill_ids: Iterable[str] | None = None,
               prompt_ids: Iterable[str] | None = None) -> int:
    """Delete cached prompt outputs so the next run regenerates them.

    `skill_ids` None means every skill on record; `prompt_ids` None
    means every prompt of each selected skill. A skill left without any output
    is dropped from the record, i.e. it counts as new again. This is the only
    invalidation path: `sync` uses it for skills whose upstream hash changed.
    Returns the number of removed prompt outputs.
    """
    hashes = load_hashes(settings)
    targets = sorted(hashes) if skill_ids is None else list(dict.fromkeys(skill_ids))
    removed = 0
    dropped = False
    for skill_id in targets:
        paths = (_stored_jsons(settings, skill_id) if prompt_ids is None
                 else [prompt_result_path(settings, skill_id, p) for p in prompt_ids])
        for path in paths:
            _unlink(path.parent / MD_SUBDIR / f"{path.stem}.md")
            removed += _unlink(path)
        if not _stored_jsons(settings, skill_id):
            shutil.rmtree(skill_result_dir(settings, skill_id), ignore_errors=True)
            dropped |= hashes.pop(skill_id, None) is not None
    if dropped:
        write_hashes(settings, hashes)
    return removed


def _stored_jsons(settings: Settings, skill_id: str) -> list[Path]:
    """The prompt jsons cached for one skill (a legacy result.json is not one)."""
    return sorted(p for p in skill_result_dir(settings, skill_id).glob("*.json")
                  if p.name != "result.json")


def _unlink(path: Path) -> int:
    """Remove a file if present; 1 when something was removed."""
    try:
        path.unlink()
    except FileNotFoundError:
        return 0
    return 1


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
