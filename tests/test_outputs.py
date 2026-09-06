"""Tests for per-skill markdown output rendering."""

import pytest

from skills_intros.data import load_skills
from skills_intros.generate import run_all
from skills_intros.llm import FakeLLM
from skills_intros.models import Domain
from skills_intros.outputs import write_skill_outputs


@pytest.fixture
async def results(settings, prompt_set):
    skills = load_skills(settings)
    return await run_all(FakeLLM(), settings, skills, prompt_set)


def test_write_skill_outputs_one_file_per_prompt(settings, results):
    skills_dir = write_skill_outputs(settings, results)
    for record in results:
        skill_dir = skills_dir / record["skill"]["id"].replace(":", "_")
        assert {p.stem for p in skill_dir.glob("*.md")} == set(record["intros"])


def test_skill_output_files_render_fields(settings, results):
    skills_dir = write_skill_outputs(settings, results)
    record = results[0]
    skill_dir = skills_dir / record["skill"]["id"].replace(":", "_")
    intro = record["intros"]

    one_liner = (skill_dir / "one_liner.md").read_text(encoding="utf-8")
    assert record["skill"]["id"].rsplit("/", 1)[-1] in one_liner
    assert intro["one_liner"]["text"] in one_liner

    taglines = (skill_dir / "tagline.md").read_text(encoding="utf-8")
    for tagline in intro["tagline"]["taglines"]:
        assert f"- {tagline}" in taglines

    guide = (skill_dir / "trigger_guide.md").read_text(encoding="utf-8")
    for item in intro["trigger_guide"]["use_when"]:
        assert f"- {item}" in guide

    domain_md = (skill_dir / "domain.md").read_text(encoding="utf-8")
    assert Domain.display(intro["domain"]["domain"]) in domain_md  # emoji-prefixed
