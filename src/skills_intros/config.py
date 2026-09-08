"""Runtime configuration: env vars over .env over built-in defaults."""

from pathlib import Path

from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

REPO = "skill-one/skills-sh-scraper"
DIST_BRANCH = "dist"
REPO_URL = f"https://github.com/{REPO}"
ARCHIVE_URL = f"https://codeload.github.com/{REPO}/tar.gz/refs/heads/{DIST_BRANCH}"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="SKILLS_INTROS_", env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    model: str = "gpt-4.1-mini"
    base_url: str | None = None  # override for OpenAI-compatible endpoints
    api_key: str | None = None
    top_n: int = 50
    concurrency: int = 8
    max_retries: int = 3
    workdir: Path = Path("output")  # holds data/ and results
    prompts_dir: Path = Path("prompts")  # one markdown file per prompt

    @model_validator(mode="after")
    def _validate(self) -> "Settings":
        if self.concurrency < 1:
            raise ValueError("concurrency must be >= 1")
        if self.max_retries < 0:
            raise ValueError("max_retries must be >= 0")
        return self
