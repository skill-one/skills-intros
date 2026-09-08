"""Fetch and parse the skills dataset published on the scraper's dist branch."""

import json
import logging
import shutil
import tarfile
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path

from .config import ARCHIVE_URL, DIST_BRANCH, Settings
from .models import SkillRecord

logger = logging.getLogger(__name__)

MAX_DOWNLOAD_RETRIES = 3


def _not_published() -> RuntimeError:
    return RuntimeError(
        f"'{DIST_BRANCH}' branch is not published on {ARCHIVE_URL} yet - "
        "the upstream daily scrape is still running; retry `skills-intros sync` later"
    )


def _extract(archive: str, data_dir: Path) -> None:
    """Extract a codeload tar.gz (single top-level dir) flat into data_dir."""
    data_dir.mkdir(parents=True, exist_ok=True)

    def _strip(member: tarfile.TarInfo) -> tarfile.TarInfo:
        member.path = member.path.partition("/")[2]
        return member

    with tarfile.open(archive, "r:gz") as tf:
        tf.extractall(
            data_dir,
            members=[_strip(m) for m in tf.getmembers() if "/" in m.path],
            filter="data",
        )


def _download_archive(url: str, dest: str) -> None:
    """Download archive with exponential backoff retry."""
    last_error: Exception | None = None
    for attempt in range(1, MAX_DOWNLOAD_RETRIES + 1):
        try:
            logger.info("Downloading archive (attempt %d/%d)...", attempt, MAX_DOWNLOAD_RETRIES)
            urllib.request.urlretrieve(url, dest)
            return
        except (urllib.error.URLError, OSError) as e:
            last_error = e
            logger.warning("Download failed: %s", e)
            if attempt < MAX_DOWNLOAD_RETRIES:
                time.sleep(2 ** attempt)
    raise RuntimeError(
        "Failed to download after %d attempts: %s" % (MAX_DOWNLOAD_RETRIES, last_error)
    ) from last_error


def sync_data(settings: Settings) -> tuple[Path, int]:
    """Download the dist-branch tarball and extract it into <workdir>/data.

    The upstream scraper rewrites the whole snapshot daily, so there is nothing
    incremental to fetch: each sync replaces the previous one wholesale. Right
    after extracting, result dirs whose upstream hash changed (or whose skill
    disappeared upstream) are pruned, so the next `run` regenerates them; run
    itself never re-checks hashes. Returns (data_dir, pruned_result_count).
    """
    data_dir = settings.workdir / "data"
    if data_dir.exists() and any(data_dir.iterdir()):
        if not (data_dir / "skills.jsonl").exists():
            raise RuntimeError(
                f"{data_dir} exists and is not a dataset snapshot - move it away or "
                "point SKILLS_INTROS_WORKDIR at a different directory"
            )
        shutil.rmtree(data_dir)
    settings.workdir.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=settings.workdir, suffix=".tar.gz") as tmp:
        try:
            _download_archive(ARCHIVE_URL, tmp.name)
        except RuntimeError as e:
            raise _not_published() from e
        _extract(tmp.name, data_dir)
    pruned = _prune_stale_results(settings, data_dir)
    if pruned:
        logger.info("Pruned %d stale result dir(s)", pruned)
    return data_dir, pruned


def _prune_stale_results(settings: Settings, data_dir: Path) -> int:
    """Delete result dirs that are stale against the freshly synced snapshot.

    Stale means: the skill is gone upstream, its content hash changed, or the
    result.json is unreadable (it would crash run anyway). Returns the number
    of pruned dirs.
    """
    results_root = settings.workdir / "results" / "skills"
    if not results_root.exists():
        return 0

    upstream: dict[str, str] = {}
    for line in (_dataset_root(data_dir) / "skills.jsonl").read_text(
        encoding="utf-8"
    ).splitlines():
        if line.strip():
            entry = json.loads(line)
            upstream[entry["id"]] = entry.get("hash", "")

    pruned = 0
    for result_file in results_root.rglob("result.json"):
        try:
            record = json.loads(result_file.read_text(encoding="utf-8"))
            skill_id = record["skill"]["id"]
            stored_hash = record["skill"].get("hash", "")
        except (json.JSONDecodeError, KeyError, TypeError):
            skill_id, stored_hash = None, None
        if skill_id is not None and upstream.get(skill_id) == stored_hash:
            continue
        shutil.rmtree(result_file.parent)
        pruned += 1
    return pruned


def _dataset_root(data_dir: Path) -> Path:
    """dist snapshots put skills.jsonl at the root; local scraper runs under data/."""
    for candidate in (data_dir, data_dir / "data"):
        if (candidate / "skills.jsonl").exists():
            return candidate
    raise FileNotFoundError(
        f"skills.jsonl not found under {data_dir} - run `skills-intros sync` first"
    )


def load_skills(settings: Settings, top_n: int | None = None) -> list[SkillRecord]:
    """Load the top N skills (by installs) that have SKILL.md content on disk.

    top_n=None uses settings.top_n; top_n <= 0 loads every usable skill.
    """
    root = _dataset_root(settings.workdir / "data")

    records: list[SkillRecord] = []
    for line in (root / "skills.jsonl").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        entry = json.loads(line)
        # content is saved iff the scraper recorded a content hash
        if not entry.get("hash"):
            continue
        skill_md = root / "skills" / entry["id"].replace(":", "_") / "SKILL.md"
        if not skill_md.exists():
            continue
        text = skill_md.read_text(encoding="utf-8", errors="replace")[:20000]
        records.append(
            SkillRecord(
                id=entry["id"],
                name=entry.get("name") or entry["id"],
                installs=int(entry.get("installs") or 0),
                source=entry.get("source", ""),
                hash=entry.get("hash", ""),
                skill_md=text,
                # collapsed to one line for the system-prompt template
                description=" ".join((entry.get("description") or "").split()),
            )
        )
    records.sort(key=lambda r: r.installs, reverse=True)
    top_n = settings.top_n if top_n is None else top_n
    return records if top_n <= 0 else records[:top_n]
