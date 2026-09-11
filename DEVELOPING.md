# Developing skills-profiles

The generator behind the dataset described in [README.md](README.md): it reads each skill's
`SKILL.md` from [skills-sh-mirror](https://github.com/skill-one/skills-sh-mirror), asks an
OpenAI-compatible LLM for eight structured angles per skill, renders a cover image from one of them,
and publishes the result to this repository's `dist` branch. Read the README first if you only want
the data.

中文: [DEVELOPING.zh-CN.md](DEVELOPING.zh-CN.md)

## Quickstart

Needs Python 3.12+ and [uv](https://docs.astral.sh/uv/); LLM credentials go in a local `.env`
(copy [`.env.example`](.env.example) — nothing is read from the network but the mirror, your own
endpoint, and the image endpoint when you render covers).

```bash
uv sync
skills-profiles sync            # download the upstream snapshot (skipped when the tag is unchanged)
skills-profiles run --limit 10  # generate profiles + render ready covers, most installed first;
                                # cached skills are free, covers are paced at 2/minute per key
```

Or offline, end to end, no API calls: `skills-profiles run --limit 5 --dry-run` (text plus
placeholder covers).

## CLI

| Command | What it does |
|---|---|
| `sync [--refresh]` | Pull the mirror's `dist` branch as one tarball into `cache/skills-sh`, unpacking only `skills.jsonl` and every `SKILL.md`. Records the tag in `SNAPSHOT.json` and skips the download when it is already current (`--refresh` forces it). Never touches the artifacts. |
| `run [--limit N] [--prompts a,b] [--concurrency C] [--dry-run] [--debug] [--verbose]` | Complete skills, most installed first: `N` of them (`0` = every skill with gaps). A skill is complete when every prompt is cached and its cover.png is drawn — the selection counts both halves, so the run fills missing text and then renders the selected skills' missing pictures, paced at `SKILLS_PROFILES_IMAGE_RATE_LIMIT` images/minute per key. Skills that need nothing, or have no `SKILL.md` in the snapshot, are skipped and do not consume the budget; without `SKILLS_PROFILES_IMAGE_API_KEY` the render pass is skipped with a warning, not an error. |
| `invalidate [--skill ID]... [--prompts a,b] [--stale] [--all]` | Drop cached outputs so the next `run` refills them. `--stale` selects the skills whose upstream hash changed or that vanished (run `sync` first). Refuses a filter-less full wipe without `--all`. Invalidating `cover` takes its `cover.png` along, which is how a picture is redrawn. |

Redoing work is never a `run` flag: `invalidate` deletes, `run` refills. A run prints a timed
summary and overwrites `output/stats.json` (the artifact's state, not the run's). Skill-level
failures — quota, connection — are isolated: the run continues, finished prompts stay on disk and
get published, and only a total washout (every selected skill failed) exits non-zero. The cover
rendering post-pass follows the same rules: a failed render is logged, the run continues, and the
missing picture is drawn by a later run. Image requests are additionally paced per key — at
most `SKILLS_PROFILES_IMAGE_RATE_LIMIT` images in any minute for each configured key (the endpoint's
documented quota, 2/min on siliconflow; `SKILLS_PROFILES_IMAGE_API_KEYS` adds more keys, and N keys
render N times as fast), `0` to disable — so a big batch waits its turn instead of collecting 429s;
the per-request retry rules in `images.py` remain the backstop.

Both commands work inside one dataset ceiling, `SKILLS_PROFILES_TOTAL_LIMIT` (default 1000): only
the most installed N skills are ever profiled or drawn, however large a run's `--limit` is. It is a
rank window, not a count of finished work — a top skill whose recipe is not filled in yet, or whose
render failed, keeps its slot rather than promoting a lower one, so re-runs and `invalidate` redraws
reuse the same N. Being one setting, it bounds profiles and pictures at once (and, since each cover
is ~1.7 MB, the total cover weight `dist` can hold); `--limit`
stay per-run budgets *within* it, and CI inherits the ceiling from the default.

## How it works

```
mirror dist branch tarball ──► cache/skills-sh (skills.jsonl + skills/<id>/SKILL.md)
                                     │
                                     └─► by installs, --limit of the ones still
                                         missing prompts ──► per-skill prompt DAG
                                                ──► output/skills/<id>/<prompt>.json
                                                ──► output/skills/<id>/md/<prompt>.md
                                                ──► output/skills.jsonl (id + hash + domain + persona)
                        cover.json + domain.json ──► `run`'s post-pass
                                                ──► output/skills/<id>/cover.png
```

`output/` (the artifacts) and `cache/skills-sh` (upstream data) are separate roots: nothing fetched
from upstream is ever written next to a generated profile.

Prompt DAG (edges mean "depends on the output of"):

```
domain   scenario   blackbox   whitebox   tagline   comments      (roots)
persona ──► cover                                                 (the picture is drawn from the portrait)
# add `depends_on: [scenario]` to a prompt's frontmatter to chain it
```

Key design decisions:

- **No orchestration framework.** The DAG is ordered with the stdlib
  [`graphlib.TopologicalSorter`](https://docs.python.org/3/library/graphlib.html).
- **Structured outputs.** Every prompt declares a pydantic schema (`output:` in its frontmatter);
  LLM calls go through [instructor](https://python.useinstructor.com/) over an OpenAI-compatible
  client. Schemas live in `models.py`, which is also where the 13-value `Domain` taxonomy is defined
  — each category carries its emoji, its classification hint and the style its covers share.
- **File-based resume.** Each prompt's output is its own `<prompt_id>.json` (markdown copy in
  `md/`), committed the moment it is generated — output and cache in one file: present and
  schema-valid means no LLM call. Markdown is written first, json last, so a crash can leave a stray
  markdown but never a json without its copy. Resume granularity is per prompt.
- **A cover is a recipe plus a render.** `cover` is an ordinary prompt, so it inherits the DAG, the
  cache, the markdown copy and `invalidate`; the moment the text pass is done, `run`'s post-pass
  renders every ready recipe in the window (paced per key by a per-minute limiter, see the CLI
  section); `images.py` then assembles the picture from three
  parts, and only the first is the model's: the **subject** (`cover.json` — the skill's persona as a
  person doing their work, and `ImagePrompt` *validates* that it reads as one: English only, comma
  phrases, a word cap, so instructor retries a recipe that came back as Chinese marketing prose
  instead of the renderer drawing from it), the **framing** (`CHARACTER`, one full-body professional at the center,
  a constant so no recipe can lose the person), and the **look** (`Domain.cover_style` per category,
  which deliberately names medium/palette/light and *no props*: measured against the endpoint, props
  in the style out-competed the subject and drew still lifes). Keeping the halves apart also keeps
  the costs apart: re-rendering spends no LLM call, and re-running the DAG never re-renders a
  picture. The picture's cache is the file's existence (`cover.png`), because the endpoint answers
  with a url that expires within the hour — bytes are stored, urls never are.
- **The index is a projection.** `skills.jsonl` is rewritten in full from what is on disk —
  `id`, the generation-time `hash`, and the `domain`/`persona` outputs re-read from their json — so a
  row can never drift from the files, and lines written before an aggregated prompt existed heal on
  the next rewrite. It is what `invalidate --stale` compares hashes against; neither `run` nor
  `sync` re-checks them.
- **One snapshot, one request.** `sync` downloads the branch as a single codeload tarball and
  replaces the previous snapshot wholesale — no per-file fetching, no expiry logic of its own.
  Only what a run reads is unpacked; the branch also mirrors whole skill repos (READMEs, evals,
  manifests), roughly 70x more data that nothing ever reads. Upstream tags each daily scrape
  `dist-<date>`, so a repeat sync costs one small request instead of the whole download. In CI the
  snapshot is restored from our own `dist` (which mirrors the dataset), so `sync` re-downloads only
  when the restored marker lags the newest upstream tag.
- **Prompts as files.** One markdown file per prompt under `prompts/`; the file name is the prompt
  id. YAML frontmatter carries metadata, the body is the jinja2 user-prompt template, and
  `_system.md` holds the shared system prompt.

### Partial regeneration

`run --prompts <id>` computes the dependency closure of the target prompts and generates only
what is missing in it. Dependencies are inputs, so they reuse their stored json and are regenerated
only when missing or schema-invalid. Prompts outside the closure are untouched — nothing outside the
selection is ever recomputed by accident. A skill left with no output at all is dropped from
`skills.jsonl`, i.e. it counts as new again.

The closure walks to dependencies, never to dependents: invalidating `persona` leaves a `cover`
recipe — and the `cover.png` rendered from it — describing the older portrait. That keeps
invalidation explicit, since nothing should be recomputed just because something upstream moved;
when you do want the follow-on work, name it, e.g. `invalidate --prompts persona,cover`, which
drops the picture along with its recipe.

## Adding a prompt

One markdown file is one prompt — no code change unless you need a new output schema (then register
the model in `models.py`):

```markdown
---
description: one line
output: IntroText          # a pydantic schema registered in models.py
depends_on: [scenario]     # DAG edges; omit for root prompts
---

请为下面的 skill 写……
{{ deps.scenario.text }}   # deps maps prompt ids to their parsed output objects
```

`_system.md` provides `{{ skill.name }}`, `{{ skill.description }}` and the full `{{ skill_md }}`
(capped at 20,000 characters), so a prompt file only has to describe the task. Then fill it in for
every skill — cached angles are reused, so only the new one costs calls:

```bash
skills-profiles run --prompts my_angle --limit 0
```

Decide whether the new angle belongs in the index: add its id to `AGGREGATED_PROMPTS` in
`outputs.py` and it is folded into every `skills.jsonl` row from then on.

A prompt that also produces a file that is not json registers its suffixes in `PROMPT_ASSETS`
(`outputs.py`) — that is how `cover` owns `cover.png`, and why invalidating the prompt drops the
rendered artifact with its recipe, so the two can never disagree.

## Project layout

```
prompts/               # one markdown file per prompt (+ _system.md)
src/skills_profiles/
├── config.py          # settings (pydantic-settings)
├── data.py            # mirror tarball download + index parsing + stale detection
├── models.py          # domain taxonomy + structured-output schemas
├── prompts.py         # frontmatter loader + DAG ordering + jinja2 rendering
├── llm.py             # instructor/openai client + offline FakeLLM
├── images.py          # text-to-image client + cover selection + offline FakeImages
├── generate.py        # async DAG execution + file-based resume + coverage stats
├── outputs.py         # per-prompt json output + md/ rendering + assets + index + invalidation
├── logging.py         # --verbose logging setup
└── cli.py             # typer commands (sync / invalidate / run)
.github/actions/publish-dist/   # the shared publish step used by both workflows
tests/                 # offline fixtures + end-to-end CLI tests
```

## Configuration

Resolution order (highest first): `SKILLS_PROFILES_*` env vars → local `.env` → built-in defaults.

| Variable | Default | Description |
|---|---|---|
| `SKILLS_PROFILES_MODEL` | `gpt-4.1-mini` | Any OpenAI-compatible chat model |
| `SKILLS_PROFILES_BASE_URL` | – | OpenAI-compatible endpoint |
| `SKILLS_PROFILES_API_KEY` | – | API key for the endpoint |
| `SKILLS_PROFILES_LIMIT` | `10` | Skills per run (`0` = all; cached ones are skipped, not counted) |
| `SKILLS_PROFILES_TOTAL_LIMIT` | `1000` | Skills the whole pipeline serves, most installed first — a ceiling on the dataset, not on one run: `run` stops at it, for profiles and pictures alike (`0` = all) |
| `SKILLS_PROFILES_CONCURRENCY` | `2` | Max concurrent LLM calls / image requests, shared across skills and prompts |
| `SKILLS_PROFILES_OUTPUT_DIR` | `output` | Artifacts directory |
| `SKILLS_PROFILES_DATA_DIR` | `cache/skills-sh` | Upstream data directory |
| `SKILLS_PROFILES_PROMPTS_DIR` | `prompts` | Prompt markdown directory (plus `_system.md`) |
| `SKILLS_PROFILES_IMAGE_BASE_URL` | `https://api.siliconflow.cn/v1` | Text-to-image endpoint; covers are drawn from a service of their own |
| `SKILLS_PROFILES_IMAGE_API_KEY` | – | Its key (without one, `run` skips the render pass with a warning; `--dry-run` needs none) |
| `SKILLS_PROFILES_IMAGE_API_KEYS` | – | Extra keys, comma-separated: each key holds its own per-minute quota, so N keys render N times as fast |
| `SKILLS_PROFILES_IMAGE_RATE_LIMIT` | `2` | Max images per minute **per key** (the endpoint's documented quota; `0` = unbounded) |
| `SKILLS_PROFILES_IMAGE_MODEL` | `Kwai-Kolors/Kolors` | Any model the endpoint serves |
| `SKILLS_PROFILES_IMAGE_SIZE` | `1024x1024` | Checked against the sizes the endpoint documents per model |
| `SKILLS_PROFILES_IMAGE_STEPS` | `20` | `num_inference_steps` (1–100); `0` omits the field |
| `SKILLS_PROFILES_IMAGE_GUIDANCE` | `7.5` | `guidance_scale` (≤ 20, documented as Kolors-only); `0` omits it for other models |

## Publishing (GitHub Actions)

Two manually-triggered workflows share one publish lock (`concurrency: publish-dist`) and are split
by concern:

| Workflow | Pipeline | Tag |
|---|---|---|
| [`sync`](.github/workflows/sync.yml) | restore dist → sync upstream → `invalidate --stale` → publish | `dist-YYYY-MM-DD`, force-updated within a day |
| [`generate`](.github/workflows/generate.yml) | restore dist → `run --limit <input, default 10>` → publish | `dist-<base>-N`, base = newest sync tag, N increments |

`generate`'s `run` renders covers too when `SKILLS_PROFILES_IMAGE_API_KEY` is configured (paced per
key at the per-minute rate limit); without the key it stays text-only, and the backlog is drawn by
later runs once the key exists. `limit` counts skills to complete — text and picture alike — so
`limit=100` with covers pending means up to 100 renders (~25 min on two keys at 4/min).

Both workflows share two composite actions: [`restore-dist`](.github/actions/restore-dist/action.yml)
(one codeload request pulls the branch back into `output/` and `cache/`) and
[`publish-dist`](.github/actions/publish-dist/action.yml) (mirror the working dirs back to `dist`,
tag, prune to the retention window). `dist` is the single atomic snapshot: the profiles at its root
plus a `cache/skills-sh/` dataset mirror. Because the dataset rides in the snapshot, **only `sync`
ever touches upstream** — it re-downloads when the restored marker lags the newest tag; `generate`
just reads the dataset the last `sync` published and never fetches. History is pruned to a
rolling window (default `1 month`; the newest commit and the newest tag of each pattern are always
kept as a floor).

`generate` is the only workflow that adds binary weight, and it is bounded twice: the `limit` input
caps how many skills one batch completes (text and covers alike), while `SKILLS_PROFILES_TOTAL_LIMIT`
caps the dataset (`run` only ever serves the most installed N skills). Each picture is ~1.7 MB as
measured at 1024x1024 and every later run fetches the whole branch back, so it is that ceiling —
not any single run — that bounds how many covers `dist` can ever hold: an existing `cover.png` is
restored and kept, never re-rendered.

```bash
gh workflow run generate.yml -f limit=50 -f concurrency=8   # complete 50 skills (text + covers)
gh workflow run sync.yml                                    # refresh upstream, drop stale profiles
```

Required configuration (Settings → Secrets and variables → Actions):

| Where | Name | Example |
|---|---|---|
| Secret | `SKILLS_PROFILES_API_KEY` | the endpoint's API key |
| Secret | `SKILLS_PROFILES_IMAGE_API_KEY` | the text-to-image endpoint's key (optional: without it `generate` stays text-only) |
| Variable | `SKILLS_PROFILES_BASE_URL` | `https://api.b.ai/v1` |
| Variable | `SKILLS_PROFILES_MODEL` | `GLM-5.3-Flash` |
| Variable | `SKILLS_PROFILES_IMAGE_BASE_URL`, `SKILLS_PROFILES_IMAGE_MODEL`, `SKILLS_PROFILES_IMAGE_SIZE` | optional; default to the documented Kolors endpoint at `1024x1024` |
| Variable | `SKILLS_PROFILES_TOTAL_LIMIT` | optional; the built-in `1000` already bounds local and CI alike, so set it only to change the ceiling |

## Testing

The whole pipeline is verified offline: dataset parsing, DAG ordering, template rendering, resume
skip, invalidation, dependency passing, markdown rendering, the cover recipe's prompt/seed/payload
construction, the endpoint's retry rules, the per-key rate limiter, and a full CLI dry-run of `run`
— no
network access (`llm.py` and `images.py` provide `FakeLLM` / `FakeImages`, `conftest.py` replaces
`data.download_file` with a fake that serves a snapshot tarball built from the fixtures, and the
image endpoint is reached only through a stubbed `urlopen`).

```bash
uv run pytest
```

Docs rule: every English document has a Chinese counterpart (`README.md` / `README.zh-CN.md`,
`DEVELOPING.md` / `DEVELOPING.zh-CN.md`) — keep both in sync, in the same pass.
