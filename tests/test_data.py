"""Tests for skills.jsonl parsing, Top-N filtering, snapshot sync and local SKILL.md reads."""

import json
from pathlib import Path

import pytest

import skills_intros.data as data_mod
from conftest import fake_download, skill_md_text
from skills_intros.config import TARBALL_URL, Settings
from skills_intros.data import load_skills, read_skill_md, skill_md_path, sync_data
from skills_intros.outputs import load_hashes, write_hashes


def test_loads_only_valid_skills_sorted_by_installs(settings):
    skills = load_skills(settings)
    assert [s.name for s in skills] == ["Alpha", "Beta", "Gamma", "Hotel"]
    assert skills[0].installs == 300


def test_top_n_limits_result(settings):
    skills = load_skills(settings, top_n=2)
    assert [s.name for s in skills] == ["Alpha", "Beta"]


def test_top_n_zero_loads_all(settings):
    assert len(load_skills(settings, top_n=0)) == 4


def test_skill_md_empty_until_read(settings):
    """Loading the index alone reads no SKILL.md: the source comes on demand."""
    skills = load_skills(settings)
    assert skills[0].skill_md == ""
    assert "Alpha does useful things" in read_skill_md(settings, skills[0])


def test_description_loaded_from_skills_jsonl(settings):
    skills = load_skills(settings)
    assert skills[0].description == "Alpha 的官方技能描述"


def test_description_collapsed_to_one_line(settings):
    """Multiline index descriptions must not break the one-line prompt format."""
    path = settings.data_dir / "skills.jsonl"
    entries = [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines()]
    entries[0]["description"] = "第一行\n第二行"
    path.write_text(
        "\n".join(json.dumps(e) for e in entries) + "\n", encoding="utf-8"
    )
    assert load_skills(settings)[0].description == "第一行 第二行"


def test_description_empty_when_jsonl_lacks_it(settings):
    """Entries without a description still load, with '' as fallback."""
    hotel = next(s for s in load_skills(settings) if s.id == "owner-h/repo-h/hotel:sub")
    assert hotel.description == ""


def test_colon_slug_read_from_underscore_directory(settings):
    hotel = next(s for s in load_skills(settings) if s.id == "owner-h/repo-h/hotel:sub")
    assert "Hotel does useful things" in read_skill_md(settings, hotel)


def test_skill_md_lives_at_the_snapshot_path(settings):
    skill = load_skills(settings)[0]
    expected = Path("skills") / skill.id.replace(":", "_") / "SKILL.md"
    assert skill_md_path(settings, skill).relative_to(settings.data_dir) == expected
    assert skill_md_path(settings, skill).read_text(
        encoding="utf-8"
    ) == skill_md_text({"name": skill.name, "hash": skill.hash})


def test_skill_md_missing_in_snapshot_returns_none(settings):
    """A skill the snapshot has no source for yields nothing."""
    orphan = load_skills(settings)[0].model_copy(update={"id": "owner-x/repo-x/nope"})
    assert read_skill_md(settings, orphan) is None


def test_skill_md_capped_for_the_llm(settings):
    """Only the head of a huge SKILL.md reaches the prompt."""
    skill = load_skills(settings)[0]
    path = skill_md_path(settings, skill)
    path.write_text("x" * 100000, encoding="utf-8")
    assert len(read_skill_md(settings, skill)) == data_mod.MD_MAX_CHARS


def make_settings(tmp_path) -> Settings:
    """An isolated artifacts dir + snapshot dir under tmp_path."""
    return Settings(output_dir=tmp_path / "out", data_dir=tmp_path / "skills-sh")


def test_raises_without_dataset(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_skills(Settings(data_dir=tmp_path / "empty"))


def test_sync_refuses_to_wipe_foreign_data(tmp_path, monkeypatch):
    """A non-empty data dir that is not a dataset directory must not be deleted by sync."""
    settings = make_settings(tmp_path)
    data_dir = settings.data_dir
    data_dir.mkdir(parents=True)
    (data_dir / "user-file.txt").write_text("precious", encoding="utf-8")

    monkeypatch.setattr(data_mod, "_download", fake_download([]))
    with pytest.raises(RuntimeError, match="not a dataset directory"):
        sync_data(settings)
    assert (data_dir / "user-file.txt").read_text(encoding="utf-8") == "precious"


def test_sync_unpacks_the_whole_snapshot(tmp_path, monkeypatch):
    """One tarball request fills the data dir: index, every SKILL.md and
    everything else the branch carries."""
    settings = make_settings(tmp_path)
    served = fake_download([
        {"id": "o/r/s", "name": "s", "installs": "1", "source": "o/r", "hash": "h"},
    ])
    seen = []

    def recording(url: str, dest: Path) -> bool:
        seen.append(url)
        return served(url, dest)

    monkeypatch.setattr(data_mod, "_download", recording)
    data_dir, pruned = sync_data(settings)
    assert seen == [TARBALL_URL]
    assert (data_dir / "skills.jsonl").exists()
    assert (data_dir / "skills" / "o" / "r" / "s" / "SKILL.md").exists()
    assert (data_dir / "skills" / "o" / "r" / "s" / "extra.md").exists()
    assert pruned == 0
    assert load_skills(settings)[0].name == "s"
    assert read_skill_md(settings, load_skills(settings)[0]) is not None


def test_sync_replaces_the_previous_snapshot(tmp_path, monkeypatch):
    """Sync is wholesale: files that are gone upstream are gone locally too."""
    settings = make_settings(tmp_path)
    data_dir = settings.data_dir
    data_dir.mkdir(parents=True)
    (data_dir / "skills.jsonl").write_text(
        json.dumps({"id": "o/r/s", "name": "s", "installs": "1",
                    "source": "o/r", "hash": "old"}) + "\n", encoding="utf-8")
    stale = data_dir / "skills" / "o" / "r" / "gone" / "SKILL.md"
    stale.parent.mkdir(parents=True)
    stale.write_text("stale", encoding="utf-8")

    monkeypatch.setattr(data_mod, "_download", fake_download([
        {"id": "o/r/s", "name": "s", "installs": "1", "source": "o/r", "hash": "h"},
    ]))
    sync_data(settings)
    assert not stale.exists()
    assert load_skills(settings)[0].hash == "h"


def test_sync_prunes_stale_results(tmp_path, monkeypatch):
    """sync deletes result dirs whose recorded hash changed, whose skill vanished
    upstream, or whose directory is missing; intact results survive and
    hashes.json is rewritten without pruned entries."""
    settings = make_settings(tmp_path)
    results_root = settings.output_dir / "skills"

    def make_result(skill_id: str) -> None:
        d = results_root / skill_id.replace(":", "_")
        d.mkdir(parents=True)
        (d / "domain.json").write_text("{}", encoding="utf-8")

    make_result("o/r/unchanged")
    make_result("o/r/changed")
    make_result("o/r/gone")

    write_hashes(settings, {
        "o/r/unchanged": "h1",
        "o/r/changed": "old",
        "o/r/gone": "h2",
        "o/r/dirless": "h3",
    })

    monkeypatch.setattr(data_mod, "_download", fake_download([
        {"id": "o/r/unchanged", "name": "u", "installs": "1", "source": "o/r", "hash": "h1"},
        {"id": "o/r/changed", "name": "c", "installs": "2", "source": "o/r", "hash": "new"},
        {"id": "o/r/other", "name": "x", "installs": "3", "source": "o/r", "hash": "h9"},
    ]))
    _, pruned = sync_data(settings)
    assert pruned == 3
    assert (results_root / "o/r/unchanged" / "domain.json").exists()
    assert not (results_root / "o/r/changed").exists()
    assert not (results_root / "o/r/gone").exists()
    assert load_hashes(settings) == {"o/r/unchanged": "h1"}


def test_sync_leaves_legacy_result_json_dirs_alone(tmp_path, monkeypatch):
    """Dirs predating the split layout (result.json only, not on record) are
    not pruned by sync; the next run converts them in place."""
    settings = make_settings(tmp_path)
    results_root = settings.output_dir / "skills"
    legacy_dir = results_root / "o_r_legacy"
    legacy_dir.mkdir(parents=True)
    (legacy_dir / "result.json").write_text(
        json.dumps({"skill": {"id": "o/r/legacy", "hash": "stale"}, "intros": {}}),
        encoding="utf-8",
    )

    monkeypatch.setattr(data_mod, "_download", fake_download([
        {"id": "o/r/other", "name": "x", "installs": "1", "source": "o/r", "hash": "h9"},
    ]))
    _, pruned = sync_data(settings)
    assert pruned == 0
    assert (legacy_dir / "result.json").exists()
