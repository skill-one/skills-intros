"""Cover images: one png per skill, rendering the skill as a person at work.

The picture is a projection of three parts, and only the first is the model's
job: the subject `cover.json` holds (who that person is, what they hold, in what
moment), the framing every cover shares (`CHARACTER`, which is why a cover is
always one person and never a still life), and the look of the skill's usage
category (`domain.json` -> `Domain.cover_style`: medium, palette, light). This
module only renders, which keeps the two costs apart: a picture you do not like
is re-rendered without spending any text call, and re-running the DAG never
re-renders a picture.

Rendering is its own command rather than a `run` flag for three reasons: the
image endpoint is a different service with its own key (see config's `image_*`),
its calls are far slower and costlier than a chat call, and its answer is a url
the provider expires within the hour - so the bytes must be fetched at once and
stored, never referenced.

The file is the cache, as everywhere else in the artifact layout: a skill that
has a `cover.png` is never re-rendered, and dropping one is
`invalidate --prompts cover`'s job (it takes the json with it, so the recipe and
the picture are refilled together). A skill with no `cover` output yet simply has
nothing to render and waits for a later run.
"""

import asyncio
import base64
import json
import logging
import time
import urllib.error
import urllib.request
import zlib
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from .config import Settings
from .data import download_file
from .models import Domain, SkillRecord
from .outputs import SKILLS_SUBDIR, prompt_asset_path, read_prompt_output

logger = logging.getLogger(__name__)

PROMPT_ID = "cover"  # the prompt whose output supplies the picture's subject
ASSET_SUFFIX = ".png"  # the rendered cover, next to its json in the skill dir
# A cover is always one person, whatever the subject line says: the profiles cast
# every skill as an occupation (see prompts/persona.md), and a diffusion model
# left to itself fills the frame with the props a prompt mentions instead.
CHARACTER = ("one character, full body, center of the composition, "
             "dressed and posed for their occupation")
# The two things no cover may contain: letters (diffusion models render them as
# garbage) and a crowd (this is a portrait of one professional, not a street scene)
NEGATIVE_PROMPT = ("text, letters, numbers, logo, watermark, blurry, low quality, "
                   "crowd, multiple people")
# a stalled endpoint must become a timeout, not a hung CI job (the docs list 504)
REQUEST_TIMEOUT_SECONDS = 300
# transient per the docs (429 rate limit "TPM limit reached", 503 model service
# overloaded, 504 gateway timeout) plus the proxy-side 502 that fronts them
RETRYABLE_STATUS = frozenset({429, 502, 503, 504})

# a real 1x1 png, so a dry-run exercises the same layout as a real render
FAKE_PNG = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVR4nGNoaGgAAAMEAYFL09IQAAAAAElFTkSuQmCC"
)


@dataclass
class CoverStats:
    """Aggregated counters for one `covers` run, tallied by `run_covers`."""

    rendered: int = 0
    skills_failed: int = 0
    seconds: float = 0.0
    bytes_written: int = 0


def cover_path(settings: Settings, skill_id: str) -> Path:
    """Where a skill's rendered cover lives."""
    return prompt_asset_path(settings, skill_id, PROMPT_ID, ASSET_SUFFIX)


def covers_on_disk(settings: Settings) -> int:
    """How many skills hold a rendered cover.

    Counted from the artifact tree, like every other number in stats.json: it is
    the dataset's current state, not a run's tally, so `run` and `covers` report
    the same figure whichever of them wrote the file last.
    """
    root = settings.output_dir / SKILLS_SUBDIR
    return sum(1 for _ in root.rglob(f"{PROMPT_ID}{ASSET_SUFFIX}"))


def cover_needed(settings: Settings, skill_id: str) -> bool:
    """True when there is a recipe to render and no picture yet."""
    return image_prompt(settings, skill_id) is not None and not cover_path(
        settings, skill_id).is_file()


def image_prompt(settings: Settings, skill_id: str) -> str | None:
    """The full prompt for one cover: subject, framing, then the category's look.

    The subject is the model's answer (who that person is, what they hold, in what
    moment); `CHARACTER` is what makes the result a portrait however thin that
    answer is; the style comes from the category lookup rather than from the
    model, so the 13 categories stay visually distinct families and none of them
    competes with the person for the frame. None means the skill has no `cover`
    output yet, i.e. nothing to render; a stored but empty subject still renders
    the framed character on the category's look, because that is a visible
    outcome you can invalidate, not a silently skipped skill.
    """
    stored = read_prompt_output(settings, skill_id, PROMPT_ID)
    if stored is None:
        return None
    subject = str(stored.get("text") or "").strip().rstrip(".,; ")
    category = (read_prompt_output(settings, skill_id, "domain") or {}).get("domain", "")
    parts = (subject, CHARACTER, Domain.style_for(str(category)))
    return ", ".join(part for part in parts if part)


def seed_for(skill_id: str) -> int:
    """A seed stable per skill id (the endpoint documents values up to 9999999999).

    Providers do not promise that a fixed seed reproduces the same pixels, so
    this is not a byte-level cache — the file's existence is. Pinning the seed
    just keeps a deliberate re-render close to the picture it replaces.
    """
    return zlib.crc32(skill_id.encode("utf-8"))


def request_payload(settings: Settings, prompt: str, seed: int) -> dict:
    """The generations body, per the endpoint's documented fields.

    `num_inference_steps` and `guidance_scale` are dropped when set to 0: the
    latter is documented as Kolors-only (Qwen-Image wants `cfg`), so switching
    models needs no code change. `batch_size` is never sent — one picture per
    skill, and the field is Kolors-only too.
    """
    payload: dict = {
        "model": settings.image_model,
        "prompt": prompt,
        "negative_prompt": NEGATIVE_PROMPT,
        "image_size": settings.image_size,
        "seed": seed,
    }
    if settings.image_steps:
        payload["num_inference_steps"] = settings.image_steps
    if settings.image_guidance:
        payload["guidance_scale"] = settings.image_guidance
    return payload


def _error_detail(error: urllib.error.HTTPError) -> str:
    """The provider's own message from an error body ({"code", "message", "data"})."""
    try:
        body = json.loads(error.read().decode("utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        return error.reason or str(error.code)
    if isinstance(body, dict):
        return str(body.get("message") or body)
    return str(body)


def _request_image(settings: Settings, prompt: str, seed: int) -> tuple[str, str]:
    """One generations request; returns (image url, provider trace id).

    Retries transient failures with exponential backoff. A 400/401/403 is raised
    at once: the same request would be rejected the same way, and the message
    (bad size, bad key) is worth seeing rather than three copies of.
    """
    request = urllib.request.Request(
        settings.images_url,
        data=json.dumps(request_payload(settings, prompt, seed)).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {settings.image_api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    attempts = settings.max_retries + 1  # one try plus the documented retries
    last_error: Exception | None = None
    for attempt in range(1, attempts + 1):
        try:
            with urllib.request.urlopen(
                    request, timeout=REQUEST_TIMEOUT_SECONDS) as response:
                raw = response.read().decode("utf-8", "replace")
                trace = response.headers.get("x-siliconcloud-trace-id", "")
            try:
                body = json.loads(raw)
            except json.JSONDecodeError as e:
                # e.g. an html error page from something in front of the endpoint
                raise RuntimeError(
                    f"image endpoint replied with something that is not json "
                    f"(trace {trace}): {raw[:200]!r}") from e
            # the answer is `{"images": [{"url": ...}], "timings", "seed"}`:
            # a url, not base64, and not the `data` array the OpenAI type expects
            urls = [img.get("url") for img in body.get("images") or [] if img.get("url")]
            if not urls:
                raise RuntimeError(f"no image url in the response: {str(body)[:200]}")
            logger.debug("generated an image (trace %s)", trace)
            return str(urls[0]), trace
        except urllib.error.HTTPError as e:
            detail = f"image endpoint returned {e.code}: {_error_detail(e)}"
            if e.code not in RETRYABLE_STATUS:
                raise RuntimeError(detail) from e
            last_error = RuntimeError(detail)
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            last_error = RuntimeError(f"image endpoint unreachable: {e}")
        logger.warning("%s (attempt %d/%d)", last_error, attempt, attempts)
        if attempt < attempts:
            time.sleep(2**attempt)
    raise RuntimeError(
        f"giving up on the image endpoint after {attempts} attempt(s): {last_error}"
    ) from last_error


class ImageClient:
    """The provider's text-to-image endpoint (see Settings.images_url)."""

    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    async def generate(self, prompt: str, seed: int, dest: Path) -> None:
        """Write one cover to dest; the blocking HTTP runs in a worker thread."""
        await asyncio.to_thread(self._generate, prompt, seed, dest)

    def _generate(self, prompt: str, seed: int, dest: Path) -> None:
        url, trace = _request_image(self.settings, prompt, seed)
        # the url is good for an hour: download it now, store the bytes
        if not download_file(url, dest, timeout=REQUEST_TIMEOUT_SECONDS):
            raise RuntimeError(f"the generated image was already gone (404, trace {trace})")


class FakeImages:
    """Deterministic offline stand-in for dry-runs and tests."""

    async def generate(self, prompt: str, seed: int, dest: Path) -> None:
        dest.write_bytes(FAKE_PNG)


def make_images(settings: Settings) -> ImageClient:
    """The real client; like `make_llm`, it holds no connection of its own."""
    return ImageClient(settings)


async def render_cover(
    images, settings: Settings, skill: SkillRecord, sem: asyncio.Semaphore,
) -> tuple[float, int]:
    """Render one skill's cover; returns (seconds, bytes written)."""
    prompt = image_prompt(settings, skill.id)
    if prompt is None:  # select_cover_skills filters these out; a caller may not
        raise RuntimeError(f"{skill.id} has no {PROMPT_ID} output to render")
    dest = cover_path(settings, skill.id)
    dest.parent.mkdir(parents=True, exist_ok=True)
    async with sem:
        start = time.monotonic()
        await images.generate(prompt, seed_for(skill.id), dest)
        seconds = time.monotonic() - start
    return seconds, dest.stat().st_size


async def run_covers(
    images,
    settings: Settings,
    skills: list[SkillRecord],
    on_skill_done: Callable[[SkillRecord, int | None], None] | None = None,
    stats: CoverStats | None = None,
) -> list[str]:
    """Render covers for the given skills concurrently; returns the ids rendered.

    Same contract as `generate.run_all`: one semaphore bounds the whole run at
    `settings.concurrency` requests in flight, a skill whose render raises is
    isolated (the error is logged, the run continues, the missing picture is
    picked up by the next run), and nothing outside the selection is touched.
    """
    sem = asyncio.Semaphore(settings.concurrency)
    done = 0

    async def _one(skill: SkillRecord) -> str | None:
        nonlocal done
        try:
            seconds, written = await render_cover(images, settings, skill, sem)
        except Exception as e:
            logger.error("%s: cover failed, continuing with the rest: %s", skill.id, e)
            if on_skill_done:
                on_skill_done(skill, None)
            if stats is not None:
                stats.skills_failed += 1
            return None
        if on_skill_done:
            on_skill_done(skill, written)
        if stats is not None:
            stats.rendered += 1
            stats.seconds += seconds
            stats.bytes_written += written
        done += 1
        logger.debug("%s: %.1fs, %.0f KB", skill.id, seconds, written / 1024)
        return skill.id

    results = await asyncio.gather(*(_one(s) for s in skills))
    return [r for r in results if r]


def select_cover_skills(
    settings: Settings, skills: list[SkillRecord], limit: int | None = None,
) -> list[SkillRecord]:
    """The first `limit` skills (install order) that have a recipe but no picture.

    `skills` is the pipeline's window (see `data.portfolio`), so covers never reach
    past `settings.total_limit` however many runs happen. The budget rule of
    `generate.select_skills` carries over: skills with nothing to do are passed over
    without consuming any of it, so repeated `covers` runs keep walking down the list
    instead of re-scanning the same head. limit=None uses settings.image_limit;
    limit <= 0 renders every pending skill in the window.
    """
    limit = settings.image_limit if limit is None else limit
    ready = [s for s in skills if cover_needed(settings, s.id)]
    return ready if limit <= 0 else ready[:limit]
