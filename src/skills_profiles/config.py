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


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="SKILLS_PROFILES_", env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    model: str = "gpt-4.1-mini"
    base_url: str | None = None  # override for OpenAI-compatible endpoints
    api_key: str | None = None
    limit: int = 10  # skills to generate per run; cached/sourceless ones are skipped, not counted
    concurrency: int = 2
    max_retries: int = 3
    # generated profiles: skills.jsonl + skills/<id>/<prompt>.json (with md/ copies)
    output_dir: Path = Path("output")
    # the unpacked dist branch: skills.jsonl + skills/<id>/SKILL.md
    data_dir: Path = Path("cache/skills-sh")
    prompts_dir: Path = Path("prompts")  # one markdown file per prompt

    @model_validator(mode="after")
    def _validate(self) -> "Settings":
        if self.concurrency < 1:
            raise ValueError("concurrency must be >= 1")
        if self.max_retries < 0:
            raise ValueError("max_retries must be >= 0")
        return self
