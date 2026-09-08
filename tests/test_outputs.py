"""Tests for per-prompt markdown output rendering and the on-disk layout."""

import pytest

from skills_intros.data import load_skills
from skills_intros.generate import run_all
from skills_intros.llm import FakeLLM
from skills_intros.models import Domain


@pytest.fixture
async def results(settings, prompt_set):
    skills = load_skills(settings)
    return await run_all(FakeLLM(), settings, skills, prompt_set)


def test_one_json_and_md_pair_per_prompt(settings, results):
    for record in results:
        skill_id = record["skill"]["id"]
        skill_dir = settings.workdir / "results" / "skills" / skill_id.replace(":", "_")
        stems_json = {p.stem for p in skill_dir.glob("*.json")}
        stems_md = {p.stem for p in skill_dir.glob("*.md")}
        assert stems_json == set(record["intros"])
        assert stems_md == set(record["intros"])


def test_skill_output_files_render_fields(settings, results):
    record = results[0]
    skill_id = record["skill"]["id"]
    skill_dir = settings.workdir / "results" / "skills" / skill_id.replace(":", "_")
    intro = record["intros"]

    one_liner = (skill_dir / "one_liner.md").read_text(encoding="utf-8")
    assert skill_id.rsplit("/", 1)[-1] in one_liner
    assert intro["one_liner"]["text"] in one_liner

    taglines = (skill_dir / "tagline.md").read_text(encoding="utf-8")
    for tagline in intro["tagline"]["taglines"]:
        assert f"- {tagline}" in taglines

    guide = (skill_dir / "trigger_guide.md").read_text(encoding="utf-8")
    for item in intro["trigger_guide"]["use_when"]:
        assert f"- {item}" in guide

    domain_md = (skill_dir / "domain.md").read_text(encoding="utf-8")
    assert Domain.display(intro["domain"]["domain"]) in domain_md  # emoji-prefixed
