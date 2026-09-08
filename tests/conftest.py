"""Shared fixtures: an isolated workdir with a small fake dataset on disk."""

import json
from pathlib import Path

import pytest

from skills_intros.config import Settings
from skills_intros.prompts import load_prompt_set

PROJECT_ROOT = Path(__file__).resolve().parent.parent

SKILLS = [
    {"id": "owner-a/repo-a/alpha", "name": "Alpha", "description": "Alpha 的官方技能描述",
     "installs": "300", "source": "owner-a/repo-a", "hash": "a" * 64},
    {"id": "owner-b/repo-b/beta", "name": "Beta", "description": "Beta 的官方技能描述",
     "installs": "200", "source": "owner-b/repo-b", "hash": "b" * 64},
    {"id": "owner-c/repo-c/gamma", "name": "Gamma", "description": "Gamma 的官方技能描述",
     "installs": "100", "source": "owner-c/repo-c", "hash": "c" * 64},
    # no description in the index: SkillRecord.description falls back to ""
    {"id": "owner-h/repo-h/hotel:sub", "name": "Hotel", "installs": "50",
     "source": "owner-h/repo-h", "hash": "h" * 64},
    # filtered out: no saved content (no hash)
    {"id": "owner-d/repo-d/delta", "name": "Delta", "installs": "90",
     "source": "owner-d/repo-d"},
    # filtered out: indexed as saved but SKILL.md missing on disk
    {"id": "owner-g/repo-g/golf", "name": "Golf", "installs": "60",
     "source": "owner-g/repo-g", "hash": "g" * 64, "noFile": True},
]


def make_fake_dataset(settings: Settings) -> None:
    data_dir = settings.workdir / "data"
    skills_dir = data_dir / "skills"
    skills_dir.mkdir(parents=True, exist_ok=True)
    with (data_dir / "skills.jsonl").open("w", encoding="utf-8") as f:
        for entry in SKILLS:
            f.write(json.dumps(entry) + "\n")
    for entry in SKILLS:
        if not entry.get("hash") or entry.get("noFile"):
            continue
        directory = skills_dir / entry["id"].replace(":", "_")
        directory.mkdir(parents=True, exist_ok=True)
        (directory / "SKILL.md").write_text(
            f"---\nname: {entry['name']}\n---\n\n{entry['name']} does useful things.\n",
            encoding="utf-8",
        )


@pytest.fixture
def settings(tmp_path) -> Settings:
    s = Settings(workdir=tmp_path / "out")
    make_fake_dataset(s)
    return s


@pytest.fixture
def prompt_set():
    return load_prompt_set(PROJECT_ROOT / "prompts")
