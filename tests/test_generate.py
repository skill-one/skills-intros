"""Tests for DAG execution, file-based resume and end-to-end generation."""

import json

from skills_intros.data import load_skills
from skills_intros.generate import load_results, result_path, run_all, run_one
from skills_intros.llm import FakeLLM


class CountingLLM:
    """Wraps a LLM and counts how many times it was actually called."""

    def __init__(self, inner):
        self.inner = inner
        self.calls = 0

    async def create(self, response_model=None, messages=None, **kwargs):
        self.calls += 1
        return await self.inner.create(response_model, messages, **kwargs)


async def test_full_run_produces_all_prompt_outputs(settings, prompt_set):
    skill = load_skills(settings)[0]
    record, _ = await run_one(FakeLLM(), settings, prompt_set, skill, force=True)
    assert set(record["intros"]) == {"domain", "one_liner", "dev_intro", "scenario_intro",
                                     "blackbox", "whitebox", "comparison", "trigger_guide",
                                     "tagline"}


async def test_existing_results_skip_llm_calls(settings, prompt_set):
    skills = load_skills(settings)

    first = CountingLLM(FakeLLM())
    await run_all(first, settings, skills, prompt_set)
    assert first.calls == 4 * 9  # 4 skills x 9 prompts

    second = CountingLLM(FakeLLM())
    results = await run_all(second, settings, skills, prompt_set)
    assert second.calls == 0  # result.json on disk short-circuits the LLM
    assert len(results) == 4


async def test_force_regenerates(settings, prompt_set):
    skills = load_skills(settings)
    await run_all(FakeLLM(), settings, skills, prompt_set)

    forced = CountingLLM(FakeLLM())
    results = await run_all(forced, settings, skills, prompt_set, force=True)
    assert forced.calls == 4 * 9
    assert len(results) == 4


async def test_run_trusts_result_json_invalidated_by_sync(settings, prompt_set):
    """Invalidation is sync's job (it prunes stale artifacts); run never re-checks hashes."""
    skills = load_skills(settings)
    await run_all(FakeLLM(), settings, skills, prompt_set)

    # simulate an upstream update that sync has not pruned yet
    data_file = settings.workdir / "data" / "skills.jsonl"
    entries = [json.loads(l) for l in data_file.read_text(encoding="utf-8").splitlines()]
    for e in entries:
        if e["id"] == "owner-a/repo-a/alpha":
            e["hash"] = "new" + "a" * 61
    data_file.write_text(
        "\n".join(json.dumps(e) for e in entries) + "\n", encoding="utf-8"
    )

    llm = CountingLLM(FakeLLM())
    await run_all(llm, settings, load_skills(settings), prompt_set)
    assert llm.calls == 0  # run trusts result.json as-is


async def test_only_reuses_cached_targets_like_a_full_run(settings, prompt_set):
    """`only` follows the same cache rules as a full run: nothing missing -> skip."""
    skills = load_skills(settings)
    await run_all(FakeLLM(), settings, skills, prompt_set)

    llm = CountingLLM(FakeLLM())
    results = await run_all(llm, settings, skills, prompt_set, only={"tagline"})
    assert llm.calls == 0  # every tagline is already cached
    assert len(results) == 4


async def test_only_fills_in_missing_prompt_and_carries_over_rest(settings, prompt_set):
    """`only` generates just the missing prompt; everything else is carried over."""
    skills = load_skills(settings)
    await run_all(FakeLLM(), settings, skills, prompt_set)

    # drop tagline from Alpha's stored record to simulate a missing prompt
    path = result_path(settings, skills[0])
    record = json.loads(path.read_text(encoding="utf-8"))
    before = {pid: out for pid, out in record["intros"].items() if pid != "tagline"}
    record["intros"] = dict(before)
    path.write_text(json.dumps(record, ensure_ascii=False), encoding="utf-8")

    llm = CountingLLM(FakeLLM())
    await run_all(llm, settings, skills, prompt_set, only={"tagline"})
    assert llm.calls == 1  # only Alpha's missing tagline was generated

    updated = json.loads(path.read_text(encoding="utf-8"))
    assert set(updated["intros"]) == set(before) | {"tagline"}  # complete again
    for pid, out in before.items():
        assert updated["intros"][pid] == out  # carried over untouched


async def test_only_generates_missing_deps_from_scratch(settings, prompt_set):
    """With no stored results, `only` still pulls in its dependency closure."""
    skills = load_skills(settings)
    llm = CountingLLM(FakeLLM())
    await run_all(llm, settings, skills[:1], prompt_set, only={"comparison"})
    # comparison + dev_intro + scenario_intro + domain = 4 prompts
    assert llm.calls == 4
    record = json.loads(result_path(settings, skills[0]).read_text(encoding="utf-8"))
    assert set(record["intros"]) == {"domain", "dev_intro", "scenario_intro", "comparison"}

    # a partial record must not count as complete: a full run fills in the gaps
    llm = CountingLLM(FakeLLM())
    await run_all(llm, settings, skills[:1], prompt_set)
    assert llm.calls == 5  # only the missing blackbox, whitebox, one_liner, trigger_guide, tagline
    record = json.loads(result_path(settings, skills[0]).read_text(encoding="utf-8"))
    assert len(record["intros"]) == 9


async def test_only_with_force_regenerates_only_the_selection(settings, prompt_set):
    """--force targets the requested prompts; their dependencies are inputs and
    keep the normal cache rules (regenerated only when missing or invalid)."""
    skills = load_skills(settings)
    await run_all(FakeLLM(), settings, skills, prompt_set)
    before = json.loads(result_path(settings, skills[0]).read_text(encoding="utf-8"))

    # tagline depends on one_liner, but only tagline is forced -> 1 call
    llm = CountingLLM(FakeLLM())
    await run_all(llm, settings, skills[:1], prompt_set, only={"tagline"}, force=True)
    assert llm.calls == 1

    # the dependency output is reused unchanged, and so is everything else
    record = json.loads(result_path(settings, skills[0]).read_text(encoding="utf-8"))
    assert len(record["intros"]) == 9
    for pid in ("domain", "one_liner", "dev_intro", "scenario_intro",
                "comparison", "trigger_guide"):
        assert record["intros"][pid] == before["intros"][pid]

    # without force the cache rules match a full run: nothing regenerates
    llm = CountingLLM(FakeLLM())
    await run_all(llm, settings, skills[:1], prompt_set, only={"tagline"})
    assert llm.calls == 0


async def test_force_with_only_preserves_prompts_outside_closure(settings, prompt_set):
    """--force never deletes result.json: prompts outside the closure survive intact."""
    skills = load_skills(settings)
    await run_all(FakeLLM(), settings, skills, prompt_set)
    before = json.loads(result_path(settings, skills[0]).read_text(encoding="utf-8"))

    # closure of dev_intro = {domain, dev_intro}, but only dev_intro is forced -> 1 call
    llm = CountingLLM(FakeLLM())
    await run_all(llm, settings, skills[:1], prompt_set, only={"dev_intro"}, force=True)
    assert llm.calls == 1
    record = json.loads(result_path(settings, skills[0]).read_text(encoding="utf-8"))
    assert len(record["intros"]) == 9
    for pid in ("one_liner", "scenario_intro", "comparison", "trigger_guide", "tagline"):
        assert record["intros"][pid] == before["intros"][pid]


async def test_only_regenerates_cached_output_failing_current_schema(settings, prompt_set):
    """A cached output that no longer validates (e.g. after a taxonomy change)
    counts as missing and is regenerated instead of crashing the run."""
    skills = load_skills(settings)
    await run_all(FakeLLM(), settings, skills, prompt_set)

    # rewrite Alpha's stored domain to a value the current enum rejects
    path = result_path(settings, skills[0])
    record = json.loads(path.read_text(encoding="utf-8"))
    record["intros"]["domain"]["domain"] = "项目管理"
    path.write_text(json.dumps(record, ensure_ascii=False), encoding="utf-8")
    before = record["intros"]

    llm = CountingLLM(FakeLLM())
    await run_all(llm, settings, skills, prompt_set, only={"domain"})
    assert llm.calls == 1  # only Alpha's stale domain regenerated

    updated = json.loads(path.read_text(encoding="utf-8"))
    assert updated["intros"]["domain"]["domain"] == "办公效率"  # FakeLLM's fixed value
    for pid, out in before.items():
        if pid != "domain":
            assert updated["intros"][pid] == out  # carried over untouched


async def test_full_run_regenerates_cached_output_failing_current_schema(settings, prompt_set):
    """Full runs validate cached outputs too: only the invalid one regenerates."""
    skills = load_skills(settings)
    await run_all(FakeLLM(), settings, skills, prompt_set)

    # rewrite Alpha's stored domain to a value the current enum rejects
    path = result_path(settings, skills[0])
    record = json.loads(path.read_text(encoding="utf-8"))
    record["intros"]["domain"]["domain"] = "项目管理"
    path.write_text(json.dumps(record, ensure_ascii=False), encoding="utf-8")
    before = record["intros"]

    llm = CountingLLM(FakeLLM())
    await run_all(llm, settings, skills, prompt_set)
    assert llm.calls == 1  # only Alpha's stale domain regenerated

    updated = json.loads(path.read_text(encoding="utf-8"))
    assert updated["intros"]["domain"]["domain"] == "办公效率"  # FakeLLM's fixed value
    for pid, out in before.items():
        if pid != "domain":
            assert updated["intros"][pid] == out  # carried over untouched


async def test_run_one_rejects_unknown_only(settings, prompt_set):
    import pytest

    skills = load_skills(settings)
    with pytest.raises(KeyError):
        await run_all(FakeLLM(), settings, skills[:1], prompt_set, only={"nope"})


async def test_results_persisted_and_reloadable(settings, prompt_set):
    skills = load_skills(settings)
    await run_all(FakeLLM(), settings, skills, prompt_set)
    results = load_results(settings)
    assert len(results) == 4
    # sorted by skill id
    assert [r["skill"]["id"] for r in results] == [
        "owner-a/repo-a/alpha", "owner-b/repo-b/beta",
        "owner-c/repo-c/gamma", "owner-h/repo-h/hotel:sub",
    ]
    record = results[0]
    assert record["intros"]["domain"]["domain"] == "办公效率"
    assert record["intros"]["tagline"]["taglines"]


async def test_result_written_next_to_prompt_markdowns(settings, prompt_set):
    skill = load_skills(settings)[0]
    await run_all(FakeLLM(), settings, [skill], prompt_set)
    skill_dir = result_path(settings, skill).parent
    record = json.loads((skill_dir / "result.json").read_text(encoding="utf-8"))
    assert record["skill"]["id"] == skill.id
    assert {p.stem for p in skill_dir.glob("*.md")} == set(record["intros"])


async def test_dep_outputs_flow_into_downstream_prompts(settings, prompt_set):
    skill = load_skills(settings)[0]
    seen_messages = []

    class RecordingLLM:
        async def create(self, response_model=None, messages=None, **kwargs):
            seen_messages.append(messages[-1]["content"])
            return await FakeLLM().create(response_model, messages, **kwargs)

    await run_one(RecordingLLM(), settings, prompt_set, skill, force=True)
    comparison_prompt = seen_messages[-2]  # trigger_guide is last, comparison before it
    assert "离线演示介绍文本" in comparison_prompt  # dev_intro & scenario_intro fake texts


async def test_model_and_system_prompt_passed_to_llm(settings, prompt_set):
    skill = load_skills(settings)[0]
    captured = {}

    class RecordingLLM:
        async def create(self, response_model=None, messages=None, **kwargs):
            captured.update(kwargs, messages=messages)
            return await FakeLLM().create(response_model, messages, **kwargs)

    await run_one(RecordingLLM(), settings, prompt_set, skill, force=True)
    assert captured["model"] == settings.model
    assert captured["messages"][0]["role"] == "system"
    assert "推销自己" in captured["messages"][0]["content"]
    # the skill's SKILL.md source lives in the system prompt
    assert "Alpha does useful things" in captured["messages"][0]["content"]


async def test_debug_dumps_rendered_messages(settings, prompt_set, capfd):
    """debug=True prints the exact system/user messages to stderr before each call."""
    skill = load_skills(settings)[0]
    await run_one(FakeLLM(), settings, prompt_set, skill, force=True, debug=True)

    err = capfd.readouterr().err
    assert f"===== debug {skill.id} / domain =====" in err
    assert "----- system -----" in err
    assert "----- user -----" in err
    assert "Alpha does useful things." in err  # rendered skill_md, not the raw template
