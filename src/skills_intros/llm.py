"""LLM client factory and an offline fake for dry-runs."""

import instructor
from instructor import Instructor
from openai import AsyncOpenAI

from .config import Settings


def make_llm(settings: Settings) -> Instructor:  # type: ignore[type-arg]
    """instructor-patched async client; supports any OpenAI-compatible endpoint."""
    client = AsyncOpenAI(base_url=settings.base_url, api_key=settings.api_key)
    return instructor.from_openai(client)


class FakeLLM:
    """Deterministic offline stand-in for dry-runs and tests."""

    async def create(self, response_model, messages=None, **kwargs):
        system = messages[0]["content"] if messages else ""
        name = "该 skill"
        for line in system.splitlines():
            if line.startswith("skill 名称:"):
                name = line.removeprefix("skill 名称:").strip()
                break
        return _fake_output(response_model, name)


def _fake_output(model, name: str):
    from . import models as m

    if model is m.DomainClassification:
        return m.DomainClassification(domain=m.Domain.OFFICE, reason="离线演示用的固定分类")
    if model is m.OneLiner:
        return m.OneLiner(text=f"{name} 是一个离线演示用的一句话简介。")
    if model is m.IntroText:
        return m.IntroText(text=f"{name} 的离线演示介绍文本, 用于验证管道, 不含真实内容。")
    if model is m.TriggerGuide:
        return m.TriggerGuide(
            use_when=[f"当任务涉及 {name} 时"],
            avoid_when=["任务与该 skill 无关时"],
        )
    if model is m.Taglines:
        return m.Taglines(taglines=[f"{name}, 简单高效", "让 agent 更能干", "省时省力的好帮手"])
    raise TypeError(f"FakeLLM cannot handle {model}")
