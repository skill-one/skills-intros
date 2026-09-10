# Developing skills-profiles

The generator behind the dataset described in [README.md](README.md): it reads each skill's
`SKILL.md` from [skills-sh-mirror](https://github.com/skill-one/skills-sh-mirror), asks an
OpenAI-compatible LLM for seven structured angles per skill, and publishes the result to this
repository's `dist` branch. Read the README first if you only want the data.

中文: [DEVELOPING.zh-CN.md](DEVELOPING.zh-CN.md)

## Quickstart

Needs Python 3.12+ and [uv](https://docs.astral.sh/uv/); LLM credentials go in a local `.env`
(copy [`.env.example`](.env.example) — nothing is read from the network but the mirror and your own
endpoint).

```bash
uv sync
skills-profiles sync            # download the upstream snapshot (skipped when the tag is unchanged)
skills-profiles run --limit 10  # generate profiles, most installed first; cached skills are free
```

Or offline, end to end, no API calls: `skills-profiles run --limit 5 --dry-run`.

## CLI

| Command | What it does |
|---|---|
| `sync [--refresh]` | Pull the mirror's `dist` branch as one tarball into `cache/skills-sh`, unpacking only `skills.jsonl` and every `SKILL.md`. Records the tag in `SNAPSHOT.json` and skips the download when it is already current (`--refresh` forces it). Never touches the artifacts. |
| `run [--limit N] [--prompts a,b] [--concurrency C] [--dry-run] [--debug] [--verbose]` | Generate what is missing: skills ordered by installs, `N` of them (`0` = every skill with gaps). Cached and `SKILL.md`-less skills are skipped and do not consume the budget. |
| `invalidate [--skill ID]... [--prompts a,b] [--stale] [--all]` | Drop cached outputs so the next `run` refills them. `--stale` selects the skills whose upstream hash changed or that vanished (run `sync` first). Refuses a filter-less full wipe without `--all`. |

Redoing work is never a `run` flag: `invalidate` deletes, `run` refills. A run prints a timed
summary and overwrites `output/stats.json` (the artifact's state, not the run's). Skill-level
failures — quota, connection — are isolated: the run continues, finished prompts stay on disk and
get published, and only a total washout (every selected skill failed) exits non-zero.

## How it works

```
mirror dist branch tarball ──► cache/skills-sh (skills.jsonl + skills/<id>/SKILL.md)
                                     │
                                     └─► by installs, --limit of the ones still
                                         missing prompts ──► per-skill prompt DAG
                                                ──► output/skills/<id>/<prompt>.json
                                                ──► output/skills/<id>/md/<prompt>.md
                                                ──► output/skills.jsonl (id + hash + domain + persona)
```

`output/` (the artifacts) and `cache/skills-sh` (upstream data) are separate roots: nothing fetched
from upstream is ever written next to a generated profile.

Prompt DAG (edges mean "depends on the output of"):

```
domain   scenario   blackbox   whitebox   tagline   persona   comments
# no edges today: every built-in prompt is a root
# add `depends_on: [scenario]` to a prompt's frontmatter to chain it
```

Key design decisions:

- **No orchestration framework.** The DAG is ordered with the stdlib
  [`graphlib.TopologicalSorter`](https://docs.python.org/3/library/graphlib.html).
- **Structured outputs.** Every prompt declares a pydantic schema (`output:` in its frontmatter);
  LLM calls go through [instructor](https://python.useinstructor.com/) over an OpenAI-compatible
  client. Schemas live in `models.py`, which is also where the 13-value `Domain` taxonomy is defined.
- **File-based resume.** Each prompt's output is its own `<prompt_id>.json` (markdown copy in
  `md/`), committed the moment it is generated — output and cache in one file: present and
  schema-valid means no LLM call. Markdown is written first, json last, so a crash can leave a stray
  markdown but never a json without its copy. Resume granularity is per prompt.
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

## Project layout

```
prompts/               # one markdown file per prompt (+ _system.md)
src/skills_profiles/
├── config.py          # settings (pydantic-settings)
├── data.py            # mirror tarball download + index parsing + stale detection
├── models.py          # domain taxonomy + structured-output schemas
├── prompts.py         # frontmatter loader + DAG ordering + jinja2 rendering
├── llm.py             # instructor/openai client + offline FakeLLM
├── generate.py        # async DAG execution + file-based resume + coverage stats
├── outputs.py         # per-prompt json output + md/ rendering + index + invalidation
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
| `SKILLS_PROFILES_CONCURRENCY` | `2` | Max concurrent LLM calls, shared across skills and prompts |
| `SKILLS_PROFILES_OUTPUT_DIR` | `output` | Artifacts directory |
| `SKILLS_PROFILES_DATA_DIR` | `cache/skills-sh` | Upstream data directory |
| `SKILLS_PROFILES_PROMPTS_DIR` | `prompts` | Prompt markdown directory (plus `_system.md`) |

## Publishing (GitHub Actions)

Two manually-triggered workflows share one publish lock (`concurrency: publish-dist`) and are split
by concern:

| Workflow | Pipeline | Tag |
|---|---|---|
| [`sync`](.github/workflows/sync.yml) | restore dist → sync upstream → `invalidate --stale` → publish | `dist-YYYY-MM-DD`, force-updated within a day |
| [`generate`](.github/workflows/generate.yml) | restore dist → `run --limit <input, default 10>` → publish | `dist-<base>-N`, base = newest sync tag, N increments |

Both workflows share two composite actions: [`restore-dist`](.github/actions/restore-dist/action.yml)
(one codeload request pulls the branch back into `output/` and `cache/`) and
[`publish-dist`](.github/actions/publish-dist/action.yml) (mirror the working dirs back to `dist`,
tag, prune to the retention window). `dist` is the single atomic snapshot: the profiles at its root
plus a `cache/skills-sh/` dataset mirror. Because the dataset rides in the snapshot, **only `sync`
ever touches upstream** — it re-downloads when the restored marker lags the newest tag; `generate`
just reads the dataset the last `sync` published and never fetches. History is pruned to a rolling
window (default `1 month`; the newest commit and the newest tag of each pattern are always kept as a
floor).

```bash
gh workflow run generate.yml -f limit=50 -f concurrency=8   # one batch of profiles
gh workflow run sync.yml                                    # refresh upstream, drop stale profiles
```

Required configuration (Settings → Secrets and variables → Actions):

| Where | Name | Example |
|---|---|---|
| Secret | `SKILLS_PROFILES_API_KEY` | the endpoint's API key |
| Variable | `SKILLS_PROFILES_BASE_URL` | `https://api.b.ai/v1` |
| Variable | `SKILLS_PROFILES_MODEL` | `GLM-5.3-Flash` |

## Testing

The whole pipeline is verified offline: dataset parsing, DAG ordering, template rendering, resume
skip, invalidation, dependency passing, markdown rendering, and a full CLI dry-run — no network
access (`llm.py` provides a `FakeLLM`, and `conftest.py` replaces `data._download` with a fake that
serves a snapshot tarball built from the fixtures).

```bash
uv run pytest
```

Docs rule: every English document has a Chinese counterpart (`README.md` / `README.zh-CN.md`,
`DEVELOPING.md` / `DEVELOPING.zh-CN.md`) — keep both in sync, in the same pass.
