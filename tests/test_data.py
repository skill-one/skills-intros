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
    """sync deletes results whose upstream hash changed, whose skill vanished
    upstream, or whose result.json is unreadable; intact results survive."""
    import io
    import tarfile

    import skills_intros.data as data_mod
    from skills_intros.config import Settings
    from skills_intros.data import sync_data

    settings = Settings(workdir=tmp_path / "out")
    results_root = settings.workdir / "results" / "skills"

    def make_result(dir_name: str, skill_id: str, hash_: str) -> None:
        d = results_root / dir_name
        d.mkdir(parents=True)
        record = {"skill": {"id": skill_id, "hash": hash_}, "intros": {}}
        (d / "result.json").write_text(json.dumps(record), encoding="utf-8")

    make_result("o_r_unchanged", "o/r/unchanged", "h1")
    make_result("o_r_changed", "o/r/changed", "old")
    make_result("o_r_gone", "o/r/gone", "h2")
    make_result("o_r_broken", "o/r/broken", "h3")
    (results_root / "o_r_broken" / "result.json").write_text("{not json",
                                                             encoding="utf-8")

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
    assert (results_root / "o_r_unchanged" / "result.json").exists()
    assert not (results_root / "o_r_changed").exists()
    assert not (results_root / "o_r_gone").exists()
    assert not (results_root / "o_r_broken").exists()
