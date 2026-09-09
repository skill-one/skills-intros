"""Fetch the skill dataset (the scraper's dist branch) once, then read it locally.

`sync` downloads the whole branch as one tarball and unpacks into <data_dir> only
what a run reads: skills.jsonl plus every skills/<id>/SKILL.md. One request still
fetches the whole branch, so index and sources can never drift apart, and every
later read is a local file read.
"""

import json
import logging
import shutil
import tarfile
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path

from .config import DIST_BRANCH, TARBALL_URL, Settings
from .models import SkillRecord
from .outputs import invalidate, load_hashes

logger = logging.getLogger(__name__)

INDEX_NAME = "skills.jsonl"  # the index: one json line per skill
SKILLS_DIR = "skills"  # one directory per skill id, mirroring the upstream ids
SKILL_MD = "SKILL.md"
MAX_DOWNLOAD_RETRIES = 3
MD_MAX_CHARS = 20000  # cap on the SKILL.md text sent to the LLM


def _not_published() -> RuntimeError:
    return RuntimeError(
        f"'{DIST_BRANCH}' branch is not published at {TARBALL_URL} yet - "
        "the upstream daily scrape is still running; retry `skills-intros sync` later"
    )


def _download(url: str, dest: Path) -> bool:
    """Download url into dest atomically, retrying with exponential backoff.

    False means "no such file upstream" (HTTP 404); a failure that survives all
    retries raises RuntimeError.
    """
    partial = dest.with_name(dest.name + ".part")
    last_error: Exception | None = None
    for attempt in range(1, MAX_DOWNLOAD_RETRIES + 1):
        try:
            logger.info("Downloading %s (attempt %d/%d)", url, attempt, MAX_DOWNLOAD_RETRIES)
            urllib.request.urlretrieve(url, partial)
            partial.replace(dest)
            return True
        except urllib.error.HTTPError as e:
            if e.code == 404:
                logger.warning("No content at %s", url)
                partial.unlink(missing_ok=True)
                return False
            last_error = e
        except (urllib.error.URLError, OSError) as e:
            last_error = e
        logger.warning("Download failed: %s", last_error)
        if attempt < MAX_DOWNLOAD_RETRIES:
            time.sleep(2 ** attempt)
    partial.unlink(missing_ok=True)
    raise RuntimeError(
        f"Failed to download {url} after {MAX_DOWNLOAD_RETRIES} attempts: {last_error}"
    ) from last_error


def _download_snapshot(url: str, dest: Path) -> bool:
    """Replace dest with the tarball's contents; False means "nothing published yet".

    The archive is unpacked next to itself first, so a failed download or a
    corrupt archive leaves whatever is already in dest untouched.
    """
    with tempfile.TemporaryDirectory() as tmp:
        archive = Path(tmp) / "snapshot.tar.gz"
        if not _download(url, archive):
            return False
        unpacked = Path(tmp) / "unpacked"
        with tarfile.open(archive, "r:gz") as tar:
            tar.extractall(unpacked, members=_snapshot_files(tar), filter="data")
        shutil.rmtree(dest, ignore_errors=True)
        shutil.move(str(_snapshot_root(unpacked)), str(dest))
    return True


def _snapshot_files(tar: tarfile.TarFile):
    """The archive members worth unpacking: the index and every SKILL.md.

    The branch mirrors whole skill repos, and only these two kinds of files are
    ever read — keeping the rest (READMEs, evals, manifests, other markdown)
    would unpack ~70x more data than a run needs, on every single sync.
    """
    for member in tar:
        rel = member.name.split("/", 1)[-1]  # drop GitHub's <repo>-<branch>/ root
        if rel == INDEX_NAME or rel.startswith(f"{SKILLS_DIR}/") and rel.endswith(f"/{SKILL_MD}"):
            yield member


def _snapshot_root(unpacked: Path) -> Path:
    """GitHub archives wrap the branch contents in one <repo>-<branch>/ dir."""
    entries = list(unpacked.iterdir())
    return entries[0] if len(entries) == 1 and entries[0].is_dir() else unpacked


def sync_data(settings: Settings) -> tuple[Path, int]:
    """Replace <data_dir> with the dist branch snapshot and prune what went stale.

    One request downloads the whole branch as a tarball, of which only the index
    and the SKILL.md files are unpacked; the previous snapshot is replaced
    wholesale, so there is nothing incremental to fetch or to expire. Right after
    syncing, result dirs whose upstream hash changed (or whose skill disappeared
    upstream) are pruned, so the next `run` regenerates them; run itself never
    re-checks hashes. Returns (data_dir, pruned_result_count).
    """
    data_dir = settings.data_dir
    if data_dir.exists() and any(data_dir.iterdir()):
        if not (data_dir / INDEX_NAME).exists():
            raise RuntimeError(
                f"{data_dir} exists and is not a dataset directory - move it away or "
                "point SKILLS_INTROS_DATA_DIR at a different directory"
            )
    data_dir.parent.mkdir(parents=True, exist_ok=True)
    try:
        downloaded = _download_snapshot(TARBALL_URL, data_dir)
    except RuntimeError as e:
        raise _not_published() from e
    if not downloaded:
        raise _not_published()
    pruned = _prune_stale_results(settings, data_dir)
    if pruned:
        logger.info("Pruned %d stale result dir(s)", pruned)
    return data_dir, pruned


def load_skills(settings: Settings) -> list[SkillRecord]:
    """Every skill that has SKILL.md content upstream, most installed first.

    Reads the local snapshot: `skill_md` stays empty until `read_skill_md` fills
    it in, which a run does just for the skills it really generates. Narrowing
    the run is `generate.select_skills`'s job (see `--limit`).
    """
    index = settings.data_dir / INDEX_NAME
    if not index.is_file():
        raise FileNotFoundError(
            f"{INDEX_NAME} not found under {settings.data_dir} - "
            "run `skills-intros sync` first"
        )

    records: list[SkillRecord] = []
    for line in index.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        entry = json.loads(line)
        # content is saved iff the scraper recorded a content hash
        if not entry.get("hash"):
            continue
        records.append(
            SkillRecord(
                id=entry["id"],
                name=entry.get("name") or entry["id"],
                installs=int(entry.get("installs") or 0),
                source=entry.get("source", ""),
                hash=entry.get("hash", ""),
                # collapsed to one line for the system-prompt template
                description=" ".join((entry.get("description") or "").split()),
            )
        )
    records.sort(key=lambda r: r.installs, reverse=True)
    return records


def skill_md_path(settings: Settings, skill: SkillRecord) -> Path:
    """Where one skill's SKILL.md sits in the snapshot."""
    return settings.data_dir / SKILLS_DIR / skill.id.replace(":", "_") / SKILL_MD


def read_skill_md(settings: Settings, skill: SkillRecord) -> str | None:
    """One skill's SKILL.md text from the local snapshot.

    None when the snapshot has no source for it — a skill listed in skills.jsonl
    whose content the scraper could not save.
    """
    path = skill_md_path(settings, skill)
    if not path.is_file():
        return None
    return path.read_text(encoding="utf-8", errors="replace")[:MD_MAX_CHARS]


def _prune_stale_results(settings: Settings, data_dir: Path) -> int:
    """Invalidate artifacts that are stale against the freshly synced snapshot.

    Stale means: the skill is gone upstream, or its content hash changed.
    Invalidation goes through `invalidate` — the same path the `invalidate`
    command uses — so a stale skill ends up in exactly the state a manual
    invalidation leaves behind. Returns the number of pruned skills.
    """
    results_root = settings.output_dir / "skills"
    if not results_root.exists():
        return 0

    upstream: dict[str, str] = {}
    for line in (data_dir / INDEX_NAME).read_text(encoding="utf-8").splitlines():
        if line.strip():
            entry = json.loads(line)
            upstream[entry["id"]] = entry.get("hash", "")

    hashes = load_hashes(settings)
    stale = [sid for sid, hash_ in sorted(hashes.items()) if upstream.get(sid) != hash_]
    if stale:
        invalidate(settings, stale)
        logger.info("Invalidated %d stale skill(s)", len(stale))
    return len(stale)
