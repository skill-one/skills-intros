"""Tests for the markdown-file-backed prompt DAG."""

from pathlib import Path

import pytest

from skills_intros.models import Domain, DomainClassification, OneLiner
from skills_intros.prompts import _load_prompt, load_prompt_set, render_user_prompt

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PROMPTS_DIR = PROJECT_ROOT / "prompts"


@pytest.fixture
def prompts():
    return load_prompt_set(PROMPTS_DIR)


class FakeSkill:
    id = "a/b/c"
    name = "Alpha"
    skill_md = "Alpha does useful things."


def test_all_seven_prompts_loaded_from_files(prompts):
    expected = {"domain", "one_liner", "dev_intro", "scenario_intro",
                "comparison", "trigger_guide", "tagline"}
    assert set(prompts.by_id) == expected
    files = {p.stem for p in PROMPTS_DIR.glob("*.md") if not p.name.startswith("_")}
    assert files == expected


def test_system_prompt_loaded(prompts):
    assert "中文介绍词" in prompts.system_prompt


def test_all_dependencies_resolve(prompts):
    for spec in prompts.by_id.values():
        for dep in spec.depends_on:
            assert dep in prompts.by_id, f"{spec.id} depends on unknown {dep}"


def test_topological_order_puts_roots_first(prompts):
    order = prompts.ordered_ids()
    assert set(order) == set(prompts.by_id)
    assert order.index("domain") < order.index("dev_intro")
    assert order.index("dev_intro") < order.index("comparison")
    assert order.index("scenario_intro") < order.index("trigger_guide")
    assert order.index("one_liner") < order.index("tagline")


def test_render_injects_dep_outputs(prompts):
    spec = prompts.by_id["dev_intro"]
    deps = {"domain": DomainClassification(domain=Domain.DEV_CODING, reason="test")}
    prompt = render_user_prompt(spec, FakeSkill(), deps)
    assert "开发编程" in prompt
    assert "Alpha does useful things." in prompt


def test_render_root_prompt_without_deps(prompts):
    prompt = render_user_prompt(prompts.by_id["one_liner"], FakeSkill(), {})
    assert "Alpha" in prompt


def test_domain_prompt_renders_full_taxonomy(prompts):
    """Every category (emoji + name) and its description must reach the prompt."""
    prompt = render_user_prompt(prompts.by_id["domain"], FakeSkill(), {})
    for domain in Domain:
        assert f"- {domain.emoji} {domain.value}: " in prompt
    assert "agent 基础设施" in prompt  # boundary hint for the largest bucket
    assert "行业专业" not in prompt  # removed from the taxonomy


def test_render_uses_one_liner_text(prompts):
    spec = prompts.by_id["tagline"]
    deps = {"one_liner": OneLiner(text="一句话简介内容")}
    prompt = render_user_prompt(spec, FakeSkill(), deps)
    assert "一句话简介内容" in prompt


def _write(tmp_path: Path, name: str, content: str) -> Path:
    path = tmp_path / name
    path.write_text(content, encoding="utf-8")
    return path


VALID = """\
---
description: D
output: IntroText
---

Body {{ skill.name }}
"""


def test_load_prompt_roundtrip(tmp_path):
    spec = _load_prompt(_write(tmp_path, "sample.md", VALID))
    assert spec.id == "sample"
    assert spec.output_model.__name__ == "IntroText"
    assert spec.depends_on == frozenset()
    assert "Body" in spec.template


def test_rejects_missing_frontmatter(tmp_path):
    path = _write(tmp_path, "bad.md", "no frontmatter here")
    with pytest.raises(ValueError, match="frontmatter"):
        _load_prompt(path)


def test_rejects_unknown_output_model(tmp_path):
    path = _write(tmp_path, "bad.md", VALID.replace("IntroText", "NoSuchModel"))
    with pytest.raises(ValueError, match="unknown output model"):
        _load_prompt(path)


def test_rejects_unknown_dependency(tmp_path):
    _write(tmp_path, "sample.md", VALID)
    orphan = VALID.replace("id: sample", "id: orphan").replace(
        "---\n\nBody", "depends_on: [nonexistent]\n---\n\nBody"
    )
    _write(tmp_path, "orphan.md", orphan)
    with pytest.raises(ValueError, match="unknown prompts"):
        load_prompt_set(tmp_path)


def test_rejects_missing_system_prompt(tmp_path):
    _write(tmp_path, "sample.md", VALID)
    with pytest.raises(FileNotFoundError):
        load_prompt_set(tmp_path)
