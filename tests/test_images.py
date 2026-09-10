"""Tests for cover rendering: the recipe projection, the endpoint contract,
the file-is-the-cache rule, and the `covers` command. All offline: the image
endpoint is reached only through a stubbed urlopen, and dry-runs through
FakeImages."""

import asyncio
import io
import json
import urllib.error
from pathlib import Path

import pytest
from typer.testing import CliRunner

import skills_profiles.images as images_mod
from skills_profiles.cli import app
from skills_profiles.config import Settings
from skills_profiles.data import load_skills
from skills_profiles.images import (
    CHARACTER,
    FAKE_PNG,
    NEGATIVE_PROMPT,
    CoverStats,
    FakeImages,
    ImageClient,
    cover_needed,
    covers_on_disk,
    image_prompt,
    request_payload,
    run_covers,
    seed_for,
    select_cover_skills,
)
from skills_profiles.models import Domain
from skills_profiles.outputs import invalidate, write_prompt_output
from skills_profiles.prompts import load_prompt_set

runner = CliRunner()
PROMPTS = load_prompt_set(Path(__file__).resolve().parent.parent / "prompts")


def store(settings, skill_id: str, prompt_id: str, output: dict) -> None:
    """Put one prompt's output on disk, as a run would."""
    write_prompt_output(settings, skill_id, prompt_id, output)


def cover_of(settings, skill_id: str) -> Path:
    return images_mod.cover_path(settings, skill_id)


class StubResponse:
    """A urlopen answer: a json body plus the trace header the endpoint sets."""

    def __init__(self, body: dict, trace: str = "trace-1"):
        self._body = json.dumps(body).encode("utf-8")
        self.headers = {"x-siliconcloud-trace-id": trace}

    def read(self) -> bytes:
        return self._body

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False


def http_error(code: int, body: dict | None = None) -> urllib.error.HTTPError:
    payload = json.dumps(body).encode("utf-8") if body else b""
    return urllib.error.HTTPError("https://x", code, f"reason {code}", {}, io.BytesIO(payload))


class StubUrlopen:
    """Serves canned answers (or errors) in order and records what was posted."""

    def __init__(self, *outcomes):
        self.outcomes = list(outcomes)
        self.requests: list[tuple[dict, dict]] = []

    def __call__(self, request, timeout=None):
        self.requests.append((json.loads(request.data.decode("utf-8")),
                              dict(request.headers)))
        if len(self.requests) > len(self.outcomes):
            raise AssertionError("asked the endpoint more times than the test staged")
        outcome = self.outcomes[len(self.requests) - 1]
        if isinstance(outcome, Exception):
            raise outcome
        return outcome


@pytest.fixture
def with_profiles(settings):
    """Two skills holding the text half of a cover: subject + category."""
    skills = load_skills(settings)
    store(settings, skills[0].id, "cover", {"text": "a librarian indexing a shelf of books."})
    store(settings, skills[0].id, "domain", {"domain": str(Domain.KNOWLEDGE), "reason": "r"})
    store(settings, skills[1].id, "cover", {"text": "a reviewer blocking a bad commit"})
    store(settings, skills[1].id, "domain", {"domain": "不存在的分类", "reason": "r"})
    return skills[:2]


# --- the recipe: subject + the category's fixed style -----------------------

def test_image_prompt_is_subject_then_framing_then_category_look(settings, with_profiles):
    assert image_prompt(settings, with_profiles[0].id) == (
        f"a librarian indexing a shelf of books, {CHARACTER}, "
        f"{Domain.KNOWLEDGE.cover_style}")


@pytest.mark.parametrize("domain", list(Domain))
def test_every_cover_stays_a_single_person_whatever_the_category(settings, domain):
    """The person is guaranteed in code: a thin recipe must not yield a still life."""
    skill = load_skills(settings)[0]
    store(settings, skill.id, "cover", {"text": "someone doing something"})
    store(settings, skill.id, "domain", {"domain": str(domain), "reason": "r"})
    prompt = image_prompt(settings, skill.id)
    assert CHARACTER in prompt and domain.cover_style in prompt
    assert "crowd" in NEGATIVE_PROMPT and "multiple people" in NEGATIVE_PROMPT


@pytest.mark.parametrize("domain", list(Domain))
def test_a_category_style_never_names_a_competing_subject(domain):
    """A style says what a category looks like; props belong to the recipe."""
    style = domain.cover_style
    assert style.startswith("flat vector illustration")
    assert not any(word in style for word in
                   ("character", "person", "man ", "woman", "gears", "editor",
                    "library", "storefront", "book", "pen", "shield"))


def test_image_prompt_falls_back_to_the_other_style_for_an_unknown_domain(settings, with_profiles):
    assert image_prompt(settings, with_profiles[1].id).endswith(Domain.OTHER.cover_style)


def test_image_prompt_is_none_without_a_cover_output(settings):
    assert image_prompt(settings, load_skills(settings)[0].id) is None


def test_image_prompt_survives_an_empty_subject(settings, with_profiles):
    """A recipe with no subject is still renderable, not silently skipped."""
    store(settings, with_profiles[0].id, "cover", {"text": "  "})
    assert image_prompt(settings, with_profiles[0].id) == (
        f"{CHARACTER}, {Domain.KNOWLEDGE.cover_style}")


def test_cover_is_a_prompt_file_with_a_persona_dependency():
    """The text half costs one LLM call per skill and reads the persona it draws."""
    spec = PROMPTS.by_id["cover"]
    assert spec.depends_on == frozenset({"persona"})
    assert spec.output_model.__name__ == "ImagePrompt"


def test_every_category_has_its_own_style():
    assert len({d.cover_style for d in Domain}) == len(Domain), "two categories look identical"
    assert Domain.style_for("") == Domain.OTHER.cover_style


def test_the_recipe_must_be_an_english_phrase_line():
    """Measured: a Chinese marketing paragraph validates as a string and renders garbage."""
    from pydantic import ValidationError

    from skills_profiles.models import ImagePrompt

    assert ImagePrompt(text="  a scout riffling through shelves of skill cards. ").text == (
        "a scout riffling through shelves of skill cards")
    for bad in ("技能猎头, 你随口一句就有现成的本事", "",
                "a worker " * 40, "a worker! (at a desk)"):
        with pytest.raises(ValidationError, match="英文|不能为空|60|短语"):
            ImagePrompt(text=bad)


async def test_the_dry_run_fake_satisfies_the_recipe_schema():
    """A fake that broke the schema would make every offline dry-run fail loudly."""
    from skills_profiles.llm import FakeLLM
    from skills_profiles.models import ImagePrompt

    output = await FakeLLM().create(ImagePrompt, [], model="unused")
    assert ImagePrompt.model_validate_json(output.model_dump_json()) == output
    assert output.text.isascii()


# --- the request, per the documented contract ------------------------------

def test_payload_uses_the_documented_field_names(settings):
    assert request_payload(settings, "a lighthouse at dusk", 42) == {
        "model": "Kwai-Kolors/Kolors",
        "prompt": "a lighthouse at dusk",
        "negative_prompt": NEGATIVE_PROMPT,
        "image_size": "1024x1024",
        "seed": 42,
        "num_inference_steps": 20,
        "guidance_scale": 7.5,
    }


def test_payload_drops_the_optional_knobs_when_unset(settings):
    settings.image_steps = 0     # 0 stands for "omit": no documented range allows it
    settings.image_guidance = 0
    body = request_payload(settings, "p", 1)
    assert "num_inference_steps" not in body and "guidance_scale" not in body


def test_seed_is_stable_within_the_documented_range():
    assert seed_for("owner/repo/slug") == seed_for("owner/repo/slug")
    assert seed_for("a/b/c") != seed_for("a/b/d")
    assert 0 <= seed_for("owner/repo/slug") <= 9_999_999_999


def test_endpoint_url_is_derived_from_the_image_base_url():
    assert Settings(image_base_url="https://api.siliconflow.cn/v1/").images_url == (
        "https://api.siliconflow.cn/v1/images/generations")


@pytest.mark.parametrize("size", ["1024x1024", "768x1024"])
def test_settings_accept_a_documented_kolors_size(size):
    assert Settings(image_size=size).image_size == size


@pytest.mark.parametrize("kwargs, message", [
    ({"image_size": "square"}, r"image_size must be \[width\]x\[height\]"),
    ({"image_size": "512x512"}, r"documents image_size"),
    ({"image_steps": 101}, r"image_steps must be 0 \(omit the field\) or within 1\.\.100"),
    ({"image_guidance": 25}, r"image_guidance must be 0 \(omit the field\) or within 0\.\.20"),
    ({"image_limit": -1}, r"image_limit must be >= 0"),
])
def test_settings_reject_values_the_docs_do_not_allow(kwargs, message):
    with pytest.raises(ValueError, match=message):
        Settings(**kwargs)


def test_zero_is_the_documented_way_to_omit_a_knob():
    settings = Settings(image_steps=0, image_guidance=0)
    assert (settings.image_steps, settings.image_guidance) == (0, 0)


def test_request_returns_the_image_url_and_trace(settings, monkeypatch):
    stub = StubUrlopen(StubResponse({"images": [{"url": "https://cdn/x.png"}], "seed": 7}))
    monkeypatch.setattr(images_mod.urllib.request, "urlopen", stub)
    settings.image_api_key = "sk-image"

    url, trace = images_mod._request_image(settings, "p", 1)

    assert (url, trace) == ("https://cdn/x.png", "trace-1")
    body, headers = stub.requests[0]
    assert body["prompt"] == "p"
    assert headers["Authorization"] == "Bearer sk-image"


def test_request_retries_a_rate_limit_then_gives_up(settings, monkeypatch):
    monkeypatch.setattr(images_mod.time, "sleep", lambda _s: None)

    def limited() -> urllib.error.HTTPError:
        # a fresh error per attempt: its body stream can only be read once
        return http_error(429, {"message": "TPM limit reached"})

    stub = StubUrlopen(*[limited() for _ in range(4)])
    monkeypatch.setattr(images_mod.urllib.request, "urlopen", stub)
    settings.max_retries = 3

    with pytest.raises(RuntimeError, match="TPM limit reached"):
        images_mod._request_image(settings, "p", 1)
    assert len(stub.requests) == 4, "the initial try plus three retries, no more"


def test_request_does_not_retry_a_rejected_payload(settings, monkeypatch):
    """A 400 says the request itself is wrong; sending it again only burns time."""
    monkeypatch.setattr(images_mod.time, "sleep", lambda _s: None)
    stub = StubUrlopen(http_error(400, {"code": 20012, "message": "bad image_size"}))
    monkeypatch.setattr(images_mod.urllib.request, "urlopen", stub)
    settings.max_retries = 3

    with pytest.raises(RuntimeError, match="bad image_size"):
        images_mod._request_image(settings, "p", 1)
    assert len(stub.requests) == 1


def test_request_needs_a_url_in_the_answer(settings, monkeypatch):
    monkeypatch.setattr(images_mod.urllib.request, "urlopen",
                        StubUrlopen(StubResponse({"images": []})))
    with pytest.raises(RuntimeError, match="no image url"):
        images_mod._request_image(settings, "p", 1)


async def test_client_stores_the_bytes_behind_the_expiring_url(settings, with_profiles,
                                                               monkeypatch):
    dest = cover_of(settings, with_profiles[0].id)
    dest.parent.mkdir(parents=True, exist_ok=True)
    monkeypatch.setattr(images_mod.urllib.request, "urlopen",
                        StubUrlopen(StubResponse({"images": [{"url": "https://cdn/x.png"}]})))
    seen = {}

    def fake_download(url, target, timeout=None):
        seen["url"], seen["timeout"] = url, timeout
        Path(target).write_bytes(b"\x89PNG real bytes")
        return True

    monkeypatch.setattr(images_mod, "download_file", fake_download)
    await ImageClient(settings).generate("a subject, a style", 3, dest)

    assert seen["url"] == "https://cdn/x.png"  # fetched at once: the url dies in an hour
    assert seen["timeout"] == images_mod.REQUEST_TIMEOUT_SECONDS, "a hung download would" \
        " hold a concurrency slot forever"
    assert dest.read_bytes() == b"\x89PNG real bytes"


async def test_client_reports_an_already_expired_url(settings, with_profiles, monkeypatch):
    dest = cover_of(settings, with_profiles[0].id)
    monkeypatch.setattr(images_mod.urllib.request, "urlopen",
                        StubUrlopen(StubResponse({"images": [{"url": "https://cdn/x.png"}]})))
    monkeypatch.setattr(images_mod, "download_file", lambda url, target, timeout=None: False)

    with pytest.raises(RuntimeError, match="already gone"):
        await ImageClient(settings).generate("p", 3, dest)
    assert not dest.exists()


# --- selection and the run --------------------------------------------------

def test_selection_skips_rendered_and_unready_skills_without_spending_budget(settings,
                                                                             with_profiles):
    skills = load_skills(settings)
    assert [s.id for s in select_cover_skills(settings, skills, limit=0)] == [
        skills[0].id, skills[1].id]  # install order; the two others have no recipe

    assert select_cover_skills(settings, skills, limit=1) == [skills[0]]
    assert select_cover_skills(settings, skills, limit=99) == [skills[0], skills[1]]

    cover_of(settings, skills[0].id).parent.mkdir(parents=True, exist_ok=True)
    cover_of(settings, skills[0].id).write_bytes(FAKE_PNG)
    assert cover_needed(settings, skills[0].id) is False
    assert select_cover_skills(settings, skills, limit=99) == [skills[1]]


def test_selection_default_limit_comes_from_settings(settings, with_profiles):
    skills = load_skills(settings)
    settings.image_limit = 1
    assert select_cover_skills(settings, skills) == [skills[0]]


async def test_run_covers_renders_each_pending_skill_once(settings, with_profiles):
    stats = CoverStats()
    seen: list[str] = []
    skills = with_profiles

    rendered = await run_covers(FakeImages(), settings, skills,
                               on_skill_done=lambda s, w: seen.append(s.id), stats=stats)

    assert rendered == [s.id for s in skills]
    assert seen == [s.id for s in skills]
    assert stats.rendered == 2 and stats.skills_failed == 0
    assert all(cover_of(settings, s.id).read_bytes() == FAKE_PNG for s in skills)
    assert covers_on_disk(settings) == 2

    again = await run_covers(FakeImages(), settings,
                             select_cover_skills(settings, load_skills(settings), limit=0),
                             stats=stats)
    assert again == [], "a rendered cover is never re-rendered"


async def test_run_covers_isolates_a_failing_skill(settings, with_profiles):
    class Exploding(FakeImages):
        async def generate(self, prompt, seed, dest):
            if "reviewer" in prompt:
                raise RuntimeError("429 TPM limit reached")
            await super().generate(prompt, seed, dest)

    skills = with_profiles
    stats = CoverStats()
    rendered = await run_covers(Exploding(), settings, skills, stats=stats)

    assert rendered == [skills[0].id], "one bad skill must not stop the others"
    assert (stats.rendered, stats.skills_failed) == (1, 1)
    assert cover_of(settings, skills[0].id).is_file()
    assert not cover_of(settings, skills[1].id).exists()


async def test_render_refuses_a_skill_with_no_recipe(settings):
    skill = load_skills(settings)[0]

    with pytest.raises(RuntimeError, match="no cover output"):
        await images_mod.render_cover(FakeImages(), settings, skill, asyncio.Semaphore(1))


# --- invalidation drops the picture with its recipe -------------------------

def test_invalidate_cover_takes_the_png_with_the_json(settings, with_profiles):
    """One invalidation drops the picture and its recipe, so both refill together."""
    skill = with_profiles[0]
    cover_of(settings, skill.id).parent.mkdir(parents=True, exist_ok=True)
    cover_of(settings, skill.id).write_bytes(FAKE_PNG)

    assert invalidate(settings, [skill.id], {"cover"}) == 1
    assert not cover_of(settings, skill.id).exists()
    assert image_prompt(settings, skill.id) is None
    assert not cover_needed(settings, skill.id), "nothing to render until run refills it"


def test_invalidate_a_different_prompt_keeps_the_picture(settings, with_profiles):
    skill = with_profiles[0]
    cover_of(settings, skill.id).parent.mkdir(parents=True, exist_ok=True)
    cover_of(settings, skill.id).write_bytes(FAKE_PNG)

    assert invalidate(settings, [skill.id], {"domain"}) == 1
    assert cover_of(settings, skill.id).is_file(), "only cover owns the png"
    assert image_prompt(settings, skill.id).endswith(Domain.OTHER.cover_style), \
        "the recipe lost its category, so the style falls back"


def test_a_transient_failure_then_success_renders(settings, monkeypatch):
    """The point of retrying: a rate-limited first answer must not lose the cover."""
    monkeypatch.setattr(images_mod.time, "sleep", lambda _s: None)
    stub = StubUrlopen(http_error(429, {"message": "TPM limit reached"}),
                       StubResponse({"images": [{"url": "https://cdn/x.png"}]}))
    monkeypatch.setattr(images_mod.urllib.request, "urlopen", stub)
    settings.max_retries = 3

    url, _trace = images_mod._request_image(settings, "p", 1)
    assert url == "https://cdn/x.png" and len(stub.requests) == 2


def test_no_retries_means_exactly_one_attempt(settings, monkeypatch):
    monkeypatch.setattr(images_mod.time, "sleep", lambda _s: None)
    stub = StubUrlopen(http_error(503, {"message": "overloaded"}))
    monkeypatch.setattr(images_mod.urllib.request, "urlopen", stub)
    settings.max_retries = 0

    with pytest.raises(RuntimeError, match="overloaded"):
        images_mod._request_image(settings, "p", 1)
    assert len(stub.requests) == 1


def test_a_reply_that_is_not_json_is_named_as_the_endpoints_fault(settings, monkeypatch):
    class HtmlReply(StubResponse):
        def read(self) -> bytes:
            return b"<html>502 bad gateway</html>"

    monkeypatch.setattr(images_mod.urllib.request, "urlopen", StubUrlopen(HtmlReply({})))
    with pytest.raises(RuntimeError, match="not json"):
        images_mod._request_image(settings, "p", 1)


def test_an_empty_ci_variable_leaves_the_documented_default():
    """Actions export an unconfigured repo variable as "", which must not erase a default."""
    settings = Settings(image_size="", image_model="", image_base_url="")
    assert settings.image_size == "1024x1024"
    assert settings.image_model == "Kwai-Kolors/Kolors"
    assert settings.images_url.endswith("/v1/images/generations")


def test_the_shipped_cover_template_uses_the_persona_it_declares(settings):
    """A typo in cover.md would silently yield an empty subject: jinja defines nothing away."""
    from skills_profiles.images import PROMPT_ID
    from skills_profiles.prompts import render_user_prompt
    from skills_profiles.models import Persona

    spec = PROMPTS.by_id[PROMPT_ID]
    rendered = render_user_prompt(spec, {"persona": Persona(tool="npx skills",
                                                           role="技能猎头",
                                                           scene="找现成技能装上时")})
    assert "{" not in rendered  # no unresolved placeholder survived
    assert "npx skills" in rendered and "技能猎头" in rendered and "找现成技能装上时" in rendered
    assert "你自己" in rendered, "the recipe must draw the professional, not their tools"


# --- the CLI ----------------------------------------------------------------

def test_covers_dry_run_writes_pictures_and_stats(settings, with_profiles, monkeypatch):
    monkeypatch.setattr("skills_profiles.cli.Settings", lambda: settings)
    result = runner.invoke(app, ["covers", "--limit", "2", "--dry-run"])

    assert result.exit_code == 0, result.output
    assert "Rendering 2 of 4 skill(s) with model=Kwai-Kolors/Kolors size=1024x1024" \
        in result.output
    assert "2 cover(s) rendered" in result.output
    stats = json.loads((settings.output_dir / "stats.json").read_text(encoding="utf-8"))
    assert stats["covers"] == {"rendered": 2}
    assert stats["prompts"]["cover"] == 2, "the recipe count rides in with the rest"


def test_covers_second_run_has_nothing_to_do(settings, with_profiles, monkeypatch):
    monkeypatch.setattr("skills_profiles.cli.Settings", lambda: settings)
    runner.invoke(app, ["covers", "--limit", "2", "--dry-run"])
    result = runner.invoke(app, ["covers", "--limit", "2", "--dry-run"])

    assert result.exit_code == 0, result.output
    assert "Rendering 0 of 4 skill(s)" in result.output
    assert "0 cover(s) rendered" in result.output


def test_covers_needs_an_image_key_before_reading_the_dataset(settings, monkeypatch):
    """A missing key is a config mistake, not a per-skill failure."""
    settings.image_api_key = None
    monkeypatch.setattr("skills_profiles.cli.Settings", lambda: settings)
    result = runner.invoke(app, ["covers"])

    assert result.exit_code != 0
    assert "no image endpoint key" in result.output
    assert "images/generations" in result.output


@pytest.mark.parametrize("flag", ["--concurrency", "--limit"])
def test_covers_rejects_an_out_of_range_flag_before_any_work(settings, monkeypatch, flag):
    """The CLI overrides settings by assignment, which now validates too: a 0 or a
    negative would otherwise mean a semaphore that never frees or an unbounded run."""
    monkeypatch.setattr("skills_profiles.cli.Settings", lambda: settings)
    value = "0" if flag == "--concurrency" else "-1"
    result = runner.invoke(app, ["covers", flag, value, "--dry-run"])

    assert result.exit_code != 0
    assert ("concurrency must be >= 1" if flag == "--concurrency"
            else "image_limit must be >= 0") in str(result.exception)


def test_run_rejects_a_zero_concurrency(settings, monkeypatch):
    monkeypatch.setattr("skills_profiles.cli.Settings", lambda: settings)
    result = runner.invoke(app, ["run", "--limit", "1", "--concurrency", "0", "--dry-run"])

    assert result.exit_code != 0
    assert "concurrency must be >= 1" in str(result.exception)


def test_run_and_covers_are_two_independent_halves(settings, monkeypatch):
    """`run` writes recipes but never pictures; `covers` renders what is ready."""
    monkeypatch.setattr("skills_profiles.cli.Settings", lambda: settings)
    runner.invoke(app, ["run", "--limit", "1", "--dry-run"])

    assert covers_on_disk(settings) == 0
    assert len([s for s in load_skills(settings)
                if cover_needed(settings, s.id)]) == 1, "one recipe waiting to be drawn"

    result = runner.invoke(app, ["covers", "--dry-run"])
    assert result.exit_code == 0, result.output
    assert covers_on_disk(settings) == 1
