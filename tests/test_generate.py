"""Tests for DAG execution, file-based resume and end-to-end generation."""

import json

import pytest

from skills_intros.data import load_skills
from skills_intros.generate import load_results, run_all, run_one
from skills_intros.llm import FakeLLM
from skills_intros.outputs import (
    hashes_path,
    invalidate,
    load_hashes,
    prompt_result_path,
    skill_result_dir,
)


class CountingLLM:
    """Wraps a LLM and counts how many times it was actually called."""

    def __init__(self, inner):
        self.inner = inner
        self.calls = 0

    async def create(self, response_model=None, messages=None, **kwargs):
        self.calls += 1
        return await self.inner.create(response_model, messages, **kwargs)


def stored_intros(settings, skill_id: str) -> dict:
    """All per-prompt json outputs stored on disk for one skill."""
    skill_dir = skill_result_dir(settings, skill_id)
    return {
        p.stem: json.loads(p.read_text(encoding="utf-8"))
        for p in sorted(skill_dir.glob("*.json"))
    }


async def test_full_run_produces_all_prompt_outputs(settings, prompt_set):
    skill = load_skills(settings)[0]
    record, _ = await run_one(FakeLLM(), settings, prompt_set, skill)
    assert set(record["intros"]) == {"domain", "scenario_intro", "blackbox",
                                     "whitebox", "comparison", "trigger_guide",
                                     "tagline"}


async def test_existing_results_skip_llm_calls(settings, prompt_set):
    skills = load_skills(settings)

    first = CountingLLM(FakeLLM())
    await run_all(first, settings, skills, prompt_set)
    assert first.calls == 4 * 7  # 4 skills x 7 prompts

    second = CountingLLM(FakeLLM())
    results = await run_all(second, settings, skills, prompt_set)
    assert second.calls == 0  # per-prompt jsons on disk short-circuit the LLM
    assert len(results) == 4


async def test_cached_run_is_untouched_until_invalidated(settings, prompt_set):
    """Nothing regenerates until the cache is dropped: `invalidate` is the only
    way to make a run redo work."""
    skills = load_skills(settings)
    await run_all(FakeLLM(), settings, skills, prompt_set)

    cached = CountingLLM(FakeLLM())
    results = await run_all(cached, settings, skills, prompt_set)
    assert cached.calls == 0
    assert len(results) == 4

    assert invalidate(settings) == 28  # 4 skills x 7 prompts
    assert load_hashes(settings) == {}  # emptied skills leave the prune index

    forced = CountingLLM(FakeLLM())
    results = await run_all(forced, settings, skills, prompt_set)
    assert forced.calls == 4 * 7
    assert len(results) == 4


async def test_hash_registered_only_when_generating(settings, prompt_set):
    """hashes.json gains an entry only for skills that generated something this
    run; a fully cached run leaves the index untouched."""
    skills = load_skills(settings)
    await run_all(FakeLLM(), settings, skills[:1], prompt_set)
    assert hashes_path(settings).read_text(encoding="utf-8") == json.dumps(
        {skills[0].id: skills[0].hash}, ensure_ascii=False
    )

    # a run that generates nothing rewrites nothing
    before = hashes_path(settings).read_text(encoding="utf-8")
    await run_all(FakeLLM(), settings, skills[:1], prompt_set)
    assert hashes_path(settings).read_text(encoding="utf-8") == before


async def test_only_runs_write_no_hash_entry_when_fully_cached(settings, prompt_set):
    skills = load_skills(settings)
    await run_all(FakeLLM(), settings, skills, prompt_set)

    await run_all(FakeLLM(), settings, skills, prompt_set, only={"tagline"})
    # nothing was generated, so no new hash entries appeared
    assert len(json.loads(hashes_path(settings).read_text(encoding="utf-8"))) == 4


async def test_run_trusts_existing_outputs_invalidated_by_sync(settings, prompt_set):
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
    assert llm.calls == 0  # run trusts per-prompt jsons as-is


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

    # drop Alpha's tagline json to simulate a missing prompt
    tagline_path = prompt_result_path(settings, skills[0].id, "tagline")
    tagline_path.unlink()
    before = stored_intros(settings, skills[0].id)

    llm = CountingLLM(FakeLLM())
    await run_all(llm, settings, skills, prompt_set, only={"tagline"})
    assert llm.calls == 1  # only Alpha's missing tagline was generated

    updated = stored_intros(settings, skills[0].id)
    assert set(updated) == set(before) | {"tagline"}  # complete again
    for pid, out in before.items():
        assert updated[pid] == out  # carried over untouched


async def test_only_generates_missing_deps_from_scratch(settings, prompt_set):
    """With no stored results, `only` still pulls in its dependency closure."""
    skills = load_skills(settings)
    llm = CountingLLM(FakeLLM())
    await run_all(llm, settings, skills[:1], prompt_set, only={"comparison"})
    # comparison + scenario_intro = 2 prompts
    assert llm.calls == 2
    assert set(stored_intros(settings, skills[0].id)) == {"scenario_intro", "comparison"}

    # a partial directory must not count as complete: a full run fills in the gaps
    llm = CountingLLM(FakeLLM())
    await run_all(llm, settings, skills[:1], prompt_set)
    assert llm.calls == 5  # only the missing domain, blackbox, whitebox, trigger_guide, tagline
    assert len(stored_intros(settings, skills[0].id)) == 7


async def test_invalidated_prompt_regenerates_only_itself(settings, prompt_set):
    """Dropping one prompt's cache makes the next run redo exactly that prompt;
    its dependencies are inputs and keep the normal cache rules."""
    skills = load_skills(settings)
    await run_all(FakeLLM(), settings, skills, prompt_set)
    before = stored_intros(settings, skills[0].id)

    assert invalidate(settings, [skills[0].id], {"tagline"}) == 1
    # a partially invalidated skill keeps its prune-index entry
    assert skills[0].id in load_hashes(settings)

    # tagline has no dependency, and only tagline was invalidated -> 1 call
    llm = CountingLLM(FakeLLM())
    await run_all(llm, settings, skills[:1], prompt_set, only={"tagline"})
    assert llm.calls == 1

    # every other prompt is reused unchanged
    assert len(stored_intros(settings, skills[0].id)) == 7
    updated = stored_intros(settings, skills[0].id)
    for pid in ("domain", "scenario_intro", "blackbox", "whitebox",
                "comparison", "trigger_guide"):
        assert updated[pid] == before[pid]


async def test_run_preserves_prompts_outside_closure(settings, prompt_set):
    """A run never touches prompts outside the closure: their files survive intact."""
    skills = load_skills(settings)
    await run_all(FakeLLM(), settings, skills, prompt_set)
    before = stored_intros(settings, skills[0].id)

    # closure of scenario_intro = {domain, scenario_intro}, but only scenario_intro
    # was invalidated -> 1 call
    invalidate(settings, [skills[0].id], {"scenario_intro"})
    llm = CountingLLM(FakeLLM())
    await run_all(llm, settings, skills[:1], prompt_set, only={"scenario_intro"})
    assert llm.calls == 1
    updated = stored_intros(settings, skills[0].id)
    assert len(updated) == 7
    for pid in ("domain", "blackbox", "whitebox", "comparison", "trigger_guide", "tagline"):
        assert updated[pid] == before[pid]


async def test_regenerates_cached_output_failing_current_schema(settings, prompt_set):
    """A cached output that no longer validates (e.g. after a taxonomy change)
    counts as missing and is regenerated instead of crashing the run."""
    skills = load_skills(settings)
    await run_all(FakeLLM(), settings, skills, prompt_set)

    # rewrite Alpha's stored domain to a value the current enum rejects
    domain_path = prompt_result_path(settings, skills[0].id, "domain")
    domain = json.loads(domain_path.read_text(encoding="utf-8"))
    domain["domain"] = "项目管理"
    domain_path.write_text(json.dumps(domain, ensure_ascii=False), encoding="utf-8")
    before = stored_intros(settings, skills[0].id)

    llm = CountingLLM(FakeLLM())
    await run_all(llm, settings, skills, prompt_set, only={"domain"})
    assert llm.calls == 1  # only Alpha's stale domain regenerated

    updated = stored_intros(settings, skills[0].id)
    assert updated["domain"]["domain"] == "办公效率"  # FakeLLM's fixed value
    for pid, out in before.items():
        if pid != "domain":
            assert updated[pid] == out  # carried over untouched


async def test_run_one_rejects_unknown_only(settings, prompt_set):
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


async def test_crash_mid_run_keeps_completed_prompts(settings, prompt_set):
    """Each prompt is committed to disk right after generation, so a crash
    (simulated here by an LLM failing partway) keeps completed prompts and a
    rerun only regenerates what is missing."""
    skills = load_skills(settings)
    skill = skills[0]

    class FlakyLLM:
        """Generates the first two prompts, then explodes."""

        def __init__(self):
            self.inner = FakeLLM()
            self.calls = 0

        async def create(self, response_model=None, messages=None, **kwargs):
            self.calls += 1
            if self.calls > 2:
                raise RuntimeError("boom")
            return await self.inner.create(response_model, messages, **kwargs)

    with pytest.raises(RuntimeError, match="boom"):
        await run_one(FlakyLLM(), settings, prompt_set, skill)
    assert len(stored_intros(settings, skill.id)) == 2  # first two prompts survived

    llm = CountingLLM(FakeLLM())
    await run_one(llm, settings, prompt_set, skill)  # cache rules apply
    assert llm.calls == 5  # only the remaining five were regenerated
    assert len(stored_intros(settings, skill.id)) == 7


async def test_legacy_result_json_removed_on_regeneration(settings, prompt_set):
    """A pre-split result.json is ignored as a cache and deleted once the skill
    regenerates under the new layout."""
    skill = load_skills(settings)[0]
    legacy = skill_result_dir(settings, skill.id) / "result.json"
    legacy.parent.mkdir(parents=True)
    legacy.write_text(json.dumps({"skill": {"id": skill.id}, "intros": {}}), encoding="utf-8")

    llm = CountingLLM(FakeLLM())
    await run_one(llm, settings, prompt_set, skill)
    assert llm.calls == 7  # the legacy file did not count as a cache
    assert not legacy.exists()
    assert len(stored_intros(settings, skill.id)) == 7


async def test_dep_outputs_flow_into_downstream_prompts(settings, prompt_set):
    skill = load_skills(settings)[0]
    seen_messages = []

    class RecordingLLM:
        async def create(self, response_model=None, messages=None, **kwargs):
            seen_messages.append(messages[-1]["content"])
            return await FakeLLM().create(response_model, messages, **kwargs)

    await run_one(RecordingLLM(), settings, prompt_set, skill)
    comparison_prompt = seen_messages[-2]  # trigger_guide is last, comparison before it
    assert "离线演示介绍文本" in comparison_prompt  # scenario_intro's fake text


async def test_model_and_system_prompt_passed_to_llm(settings, prompt_set):
    skill = load_skills(settings)[0]
    captured = {}

    class RecordingLLM:
        async def create(self, response_model=None, messages=None, **kwargs):
            captured.update(kwargs, messages=messages)
            return await FakeLLM().create(response_model, messages, **kwargs)

    await run_one(RecordingLLM(), settings, prompt_set, skill)
    assert captured["model"] == settings.model
    assert captured["messages"][0]["role"] == "system"
    assert "推销自己" in captured["messages"][0]["content"]
    # the skill's SKILL.md source lives in the system prompt
    assert "Alpha does useful things" in captured["messages"][0]["content"]


async def test_debug_dumps_rendered_messages(settings, prompt_set, capfd):
    """debug=True prints the exact system/user messages to stderr before each call."""
    skill = load_skills(settings)[0]
    await run_one(FakeLLM(), settings, prompt_set, skill, debug=True)

    err = capfd.readouterr().err
    assert f"===== debug {skill.id} / domain =====" in err
    assert "----- system -----" in err
    assert "----- user -----" in err
    assert "Alpha does useful things." in err  # rendered skill_md, not the raw template
