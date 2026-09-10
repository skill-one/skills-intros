"""Runtime configuration: env vars over .env over built-in defaults."""

from pathlib import Path

from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

REPO = "skill-one/skills-sh-mirror"
DIST_BRANCH = "dist"
REPO_URL = f"https://github.com/{REPO}"
# the daily snapshot as GitHub publishes it: `sync` downloads and unpacks this
TAGS_ATOM_URL = f"{REPO_URL}/tags.atom"


def tarball_url(ref: str = DIST_BRANCH) -> str:
    """The whole branch in one request, at a branch, tag or commit."""
    return f"https://codeload.github.com/{REPO}/tar.gz/{ref}"


TARBALL_URL = tarball_url()

# the image_size values the API documents for each text-to-image model; an
# unknown model is left alone (the endpoint answers with a 400 and a message).
# https://api-docs.siliconflow.cn/docs/api/images-generations-post
DOCUMENTED_SIZES: dict[str, tuple[str, ...]] = {
    "Kwai-Kolors/Kolors": ("1024x1024", "960x1280", "768x1024", "720x1440", "720x1280"),
}


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="SKILLS_PROFILES_", env_file=".env", env_file_encoding="utf-8", extra="ignore",
        # the CLI overrides limits by assignment; validating it keeps `--concurrency 0`
        # an error rather than a semaphore that never lets a request through
        validate_assignment=True,
    )

    model: str = "gpt-4.1-mini"
    base_url: str | None = None  # override for OpenAI-compatible endpoints
    api_key: str | None = None
    limit: int = 10  # skills to generate per run; cached/sourceless ones are skipped, not counted
    # a ceiling on the dataset, not a per-run budget: `run` and `covers` only ever
    # serve this many of the most installed skills. Unlike `limit` it is set once
    # (here, or SKILLS_PROFILES_TOTAL_LIMIT) so local and CI cannot drift apart;
    # 0 means "no ceiling, every skill". See data.portfolio for where it applies.
    total_limit: int = 1000
    concurrency: int = 2
    max_retries: int = 3
    # generated profiles: skills.jsonl + skills/<id>/<prompt>.json (with md/ copies)
    output_dir: Path = Path("output")
    # the unpacked dist branch: skills.jsonl + skills/<id>/SKILL.md
    data_dir: Path = Path("cache/skills-sh")
    prompts_dir: Path = Path("prompts")  # one markdown file per prompt

    # Covers: a separate text-to-image endpoint (own key, own base url), so the
    # chat provider and the image provider are freely different services.
    image_base_url: str = "https://api.siliconflow.cn/v1"
    image_api_key: str | None = None
    image_model: str = "Kwai-Kolors/Kolors"
    image_size: str = "1024x1024"
    # 0 means "do not send the field": the endpoint documents num_inference_steps
    # per model family and guidance_scale as Kolors-only, and 0 is a value neither
    # range allows, so switching model needs no code change and works from env too
    image_steps: int = 20           # num_inference_steps: more steps, better and slower
    image_guidance: float = 7.5     # guidance_scale: how strictly the prompt is followed
    image_limit: int = 10  # covers rendered per run; already-rendered ones are skipped

    @property
    def images_url(self) -> str:
        """The image generations endpoint on the configured base url."""
        return self.image_base_url.rstrip("/") + "/images/generations"

    @model_validator(mode="before")
    @classmethod
    def _empty_means_unset(cls, values):
        """An empty env var or `.env` line means "not set", not "".

        Actions export a secret or variable nobody configured as an empty string,
        which would otherwise replace a default (and an empty `image_size` aborts
        every run) instead of leaving the documented default in place.
        """
        if isinstance(values, dict):
            return {key: value for key, value in values.items() if value != ""}
        return values

    @model_validator(mode="after")
    def _validate(self) -> "Settings":
        if self.concurrency < 1:
            raise ValueError("concurrency must be >= 1")
        if self.max_retries < 0:
            raise ValueError("max_retries must be >= 0")
        if self.total_limit < 0:
            raise ValueError("total_limit must be >= 0")
        if self.image_limit < 0:
            raise ValueError("image_limit must be >= 0")
        width, sep, height = self.image_size.partition("x")
        if not sep or not width.isdigit() or not height.isdigit():
            raise ValueError(f"image_size must be [width]x[height], got {self.image_size!r}")
        documented = DOCUMENTED_SIZES.get(self.image_model)
        if documented and self.image_size not in documented:
            raise ValueError(
                f"{self.image_model} documents image_size "
                f"{'/'.join(documented)}, got {self.image_size!r}")
        if self.image_steps and not 1 <= self.image_steps <= 100:
            raise ValueError("image_steps must be 0 (omit the field) or within 1..100")
        if self.image_guidance and not 0 < self.image_guidance <= 20:
            raise ValueError("image_guidance must be 0 (omit the field) or within 0..20")
        return self
