"""Tests for skills.jsonl parsing and Top-N filtering."""

import json

import pytest

from skills_intros.data import load_skills


def test_loads_only_valid_skills_sorted_by_installs(settings):
    skills = load_skills(settings)
    assert [s.name for s in skills] == ["Alpha", "Beta", "Gamma", "Hotel"]
    assert skills[0].installs == 300


def test_top_n_limits_result(settings):
    skills = load_skills(settings, top_n=2)
    assert [s.name for s in skills] == ["Alpha", "Beta"]


def test_top_n_zero_loads_all(settings):
    assert len(load_skills(settings, top_n=0)) == 4


def test_skill_md_content_loaded(settings):
    skills = load_skills(settings)
    assert "does useful things" in skills[0].skill_md


def test_description_loaded_from_skills_jsonl(settings):
    skills = load_skills(settings)
    assert skills[0].description == "Alpha 的官方技能描述"


def test_description_collapsed_to_one_line(settings):
    """Multiline index descriptions must not break the one-line prompt format."""
    path = settings.workdir / "data" / "skills.jsonl"
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


def test_colon_slug_resolved_to_underscore_directory(settings):
    skills = load_skills(settings)
    hotel = next(s for s in skills if s.id == "owner-h/repo-h/hotel:sub")
    assert "Hotel does useful things" in hotel.skill_md


def test_raises_without_dataset(tmp_path):
    from skills_intros.config import Settings

    with pytest.raises(FileNotFoundError):
        load_skills(Settings(workdir=tmp_path / "empty"))


def test_sync_refuses_to_wipe_foreign_data(tmp_path):
    """A non-empty data dir that is not a dataset snapshot must not be deleted by sync."""
    from skills_intros.config import Settings
    from skills_intros.data import sync_data

    settings = Settings(workdir=tmp_path / "out")
    data_dir = settings.workdir / "data"
    data_dir.mkdir(parents=True)
    (data_dir / "user-file.txt").write_text("precious", encoding="utf-8")

    with pytest.raises(RuntimeError, match="not a dataset snapshot"):
        sync_data(settings)
    assert (data_dir / "user-file.txt").read_text(encoding="utf-8") == "precious"


def test_sync_downloads_and_extracts_snapshot(tmp_path, monkeypatch):
    """sync downloads the branch tarball and extracts it flat into workdir/data."""
    import io
    import tarfile

    import skills_intros.data as data_mod
    from skills_intros.config import Settings
    from skills_intros.data import sync_data

    settings = Settings(workdir=tmp_path / "out")

    def fake_download(url: str, dest: str) -> None:
        with tarfile.open(dest, "w:gz") as tf:
            def add(name: str, content: str) -> None:
                payload = content.encode()
                info = tarfile.TarInfo(f"snapshot/{name}")
                info.size = len(payload)
                tf.addfile(info, io.BytesIO(payload))

            add("skills.jsonl",
                json.dumps({"id": "o/r/s", "name": "s", "installs": "1",
                            "source": "o/r", "hash": "h"}) + "\n")
            add("skills/o/r/s/SKILL.md", "---\nname: s\n---\n\ns does useful things.\n")

    monkeypatch.setattr(data_mod, "_download_archive", fake_download)
    data_dir, pruned = sync_data(settings)
    assert (data_dir / "skills.jsonl").exists()
    assert not (data_dir / "snapshot").exists()  # top-level dir stripped
    assert pruned == 0
    assert load_skills(settings)[0].name == "s"


def test_sync_prunes_stale_results(tmp_path, monkeypatch):
    """sync deletes result dirs whose index hash changed, whose skill vanished
    upstream, or whose directory is missing; intact results survive and the
    index is rewritten without pruned entries."""
    import io
    import tarfile

    import skills_intros.data as data_mod
    from skills_intros.config import Settings
    from skills_intros.data import sync_data
    from skills_intros.outputs import hashes_path

    settings = Settings(workdir=tmp_path / "out")
    results_root = settings.workdir / "results" / "skills"

    def make_result(skill_id: str) -> None:
        d = results_root / skill_id.replace(":", "_")
        d.mkdir(parents=True)
        (d / "domain.json").write_text("{}", encoding="utf-8")

    make_result("o/r/unchanged")
    make_result("o/r/changed")
    make_result("o/r/gone")

    hashes_path(settings).write_text(json.dumps({
        "o/r/unchanged": "h1",
        "o/r/changed": "old",
        "o/r/gone": "h2",
        "o/r/dirless": "h3",  # index entry whose dir was already removed
    }), encoding="utf-8")

    def fake_download(url: str, dest: str) -> None:
        with tarfile.open(dest, "w:gz") as tf:
            def add(name: str, content: str) -> None:
                payload = content.encode()
                info = tarfile.TarInfo(f"snapshot/{name}")
                info.size = len(payload)
                tf.addfile(info, io.BytesIO(payload))

            add("skills.jsonl",
                json.dumps({"id": "o/r/unchanged", "name": "u", "installs": "1",
                            "source": "o/r", "hash": "h1"}) + "\n"
                + json.dumps({"id": "o/r/changed", "name": "c", "installs": "2",
                              "source": "o/r", "hash": "new"}) + "\n"
                + json.dumps({"id": "o/r/other", "name": "x", "installs": "3",
                              "source": "o/r", "hash": "h9"}) + "\n")
            for rid in ("o/r/unchanged", "o/r/changed", "o/r/other"):
                add(f"skills/{rid}/SKILL.md", "---\nname: x\n---\n\ndoes things.\n")

    monkeypatch.setattr(data_mod, "_download_archive", fake_download)
    _, pruned = sync_data(settings)
    assert pruned == 3
    assert (results_root / "o/r/unchanged" / "domain.json").exists()
    assert not (results_root / "o/r/changed").exists()
    assert not (results_root / "o/r/gone").exists()
    assert json.loads(hashes_path(settings).read_text(encoding="utf-8")) == {
        "o/r/unchanged": "h1"
    }


def test_sync_leaves_legacy_result_json_dirs_alone(tmp_path, monkeypatch):
    """Dirs predating the split layout (result.json only, no index entry) are
    not pruned by sync; the next run converts them in place."""
    import io
    import tarfile

    import skills_intros.data as data_mod
    from skills_intros.config import Settings
    from skills_intros.data import sync_data

    settings = Settings(workdir=tmp_path / "out")
    results_root = settings.workdir / "results" / "skills"
    legacy_dir = results_root / "o_r_legacy"
    legacy_dir.mkdir(parents=True)
    (legacy_dir / "result.json").write_text(
        json.dumps({"skill": {"id": "o/r/legacy", "hash": "stale"}, "intros": {}}),
        encoding="utf-8",
    )

    def fake_download(url: str, dest: str) -> None:
        with tarfile.open(dest, "w:gz") as tf:
            def add(name: str, content: str) -> None:
                payload = content.encode()
                info = tarfile.TarInfo(f"snapshot/{name}")
                info.size = len(payload)
                tf.addfile(info, io.BytesIO(payload))

            add("skills.jsonl",
                json.dumps({"id": "o/r/other", "name": "x", "installs": "1",
                            "source": "o/r", "hash": "h9"}) + "\n")
            add("skills/o/r/other/SKILL.md", "---\nname: x\n---\n\ndoes things.\n")

    monkeypatch.setattr(data_mod, "_download_archive", fake_download)
    _, pruned = sync_data(settings)
    assert pruned == 0
    assert (legacy_dir / "result.json").exists()
