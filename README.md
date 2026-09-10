# skills-profiles

Generate multi-angle Chinese profiles for [agent skills](https://www.skills.sh)
collected by [skill-one/skills-sh-mirror](https://github.com/skill-one/skills-sh-mirror).

> 中文文档: [README.zh-CN.md](README.zh-CN.md)

## Quickstart

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/); LLM credentials go in a
local `.env` (see `.env.example`).

```bash
uv sync
skills-profiles sync            # download the upstream snapshot (skipped when the tag is unchanged)
skills-profiles run --limit 10  # generate profiles, most installed first; cached skills are skipped for free
```

More `run` options:

```bash
skills-profiles run --limit 0           # every skill with missing prompts
skills-profiles run --prompts tagline   # generate just this one prompt
skills-profiles run --limit 5 --dry-run # offline smoke test (fake LLM, no API calls)
skills-profiles run --limit 5 --debug   # print the rendered prompts to stderr
skills-profiles run --concurrency 3     # cap parallel LLM calls (default 2)
skills-profiles run --verbose           # DEBUG logging
```

Re-runs resume for free: each prompt is committed to disk as soon as it is generated,
so only missing prompts cost LLM calls — even after a crash mid-run. To redo work,
invalidate first:

```bash
skills-profiles invalidate --prompts whitebox        # one prompt, for every skill
skills-profiles invalidate --skill owner/repo/name   # every prompt of one skill
skills-profiles invalidate --stale                   # skills whose upstream content changed (or vanished)
skills-profiles invalidate --all                     # everything (needs --all)
```

## Artifacts

```
output/                                      # generated profiles, publishable on their own
├── skills.jsonl                             # the skill index: id, upstream hash, aggregated domain/persona
├── stats.json                               # artifact state: complete/remaining/stale skills, per-prompt coverage
└── skills/<owner>/<repo>/<skill>/           # the directory name is the skills.jsonl id
    ├── domain.json                          # one json per prompt, committed on generation (cache marker)
    └── md/domain.md                         # markdown copy for browsing

cache/skills-sh/                             # upstream data, kept separate from the artifacts
├── skills.jsonl                             # the index: one json line per skill
└── skills/<owner>/<repo>/<skill>/SKILL.md   # each skill's source
```

Built-in prompts: `domain`, `scenario`, `blackbox`, `whitebox`, `tagline`, `persona`, `comments`.

- `sync` only downloads data and never touches the artifacts: one tarball request,
  unpacking just the index and the SKILL.md files; the newest tag is recorded in
  `cache/skills-sh/SNAPSHOT.json` and the download is skipped while it is unchanged.
- Invalidation is explicit: `invalidate --stale` drops every skill whose recorded hash
  no longer matches the snapshot (or that vanished from it — run `sync` first);
  `run` itself just reuses whatever is on disk.
- Every `run` prints a timed summary and overwrites `stats.json` — the artifact's
  current state, not the run's; `sync` reports the tag it aligned to and the download
  duration.
- Skill-level failures (quota, connection) are isolated: the run continues, completed
  prompts stay on disk and get published, and only a total washout (every selected
  skill failed) exits non-zero.
- Skills whose SKILL.md is missing from the snapshot (the scraper could not save it,
  e.g. a name/case mismatch with the repo) are passed over during selection and never
  consume the `--limit` budget.

## Continuous generation (GitHub Actions)

Two manually-triggered workflows share the same `dist` publish lock and are
separated by concern:

| Workflow | Pipeline | Tag |
|---|---|---|
| `sync` | restore dist → sync upstream → invalidate --stale → publish | `dist-YYYY-MM-DD` (force-updated within a day) |
| `generate` | restore dist → run --limit <input, default 10> → publish | `dist-<base>-N` (base = newest sync tag, N increments) |

The bare date tag is the day's dataset baseline; suffixed tags are output
iterations on top of it. `dist` is both the published artifact and the cache —
its root mirrors `output/`, and history is pruned to a rolling retention window
(default `1 month`; the newest commit and the newest tag of each pattern are
always kept as a floor). Required configuration (Settings → Secrets and
variables → Actions):

| Where | Name | Example |
|---|---|---|
| Secret | `SKILLS_PROFILES_API_KEY` | the endpoint's API key |
| Variable | `SKILLS_PROFILES_BASE_URL` | `https://api.b.ai/v1` |
| Variable | `SKILLS_PROFILES_MODEL` | `GLM-5.3-Flash` |

## Adding a prompt

One markdown file under `prompts/` is one prompt; the file name is the prompt id.
`_system.md` is the shared system prompt (it provides `{{ skill.name }}`,
`{{ skill.description }}` and the full `{{ skill_md }}`), so prompt files only
describe the task:

```markdown
---
description: one line
output: IntroText          # a pydantic schema registered in models.py
depends_on: [scenario]     # DAG edges; omit for root prompts
---

请为下面的 skill 写……
{{ deps.scenario.text }}   # deps maps prompt ids to their parsed output objects
```

Then generate it for every skill (cached prompts are reused, only missing ones are
generated — invalidate first to redo):

```bash
skills-profiles run --prompts my_angle --limit 0
```

## Configuration

Resolution order (highest first): `SKILLS_PROFILES_*` env vars → local `.env` → built-in
defaults.

| Variable | Default | Description |
|---|---|---|
| `SKILLS_PROFILES_MODEL` | `gpt-4.1-mini` | Any OpenAI-compatible chat model |
| `SKILLS_PROFILES_BASE_URL` | – | OpenAI-compatible endpoint |
| `SKILLS_PROFILES_API_KEY` | – | API key for the endpoint |
| `SKILLS_PROFILES_LIMIT` | `10` | Skills to generate per run (`0` = all; cached skills are skipped, not counted) |
| `SKILLS_PROFILES_CONCURRENCY` | `2` | Max concurrent LLM calls, shared across skills and prompts (also `--concurrency`) |
| `SKILLS_PROFILES_OUTPUT_DIR` | `output` | Artifacts directory |
| `SKILLS_PROFILES_DATA_DIR` | `cache/skills-sh` | Upstream data directory |
| `SKILLS_PROFILES_PROMPTS_DIR` | `prompts` | Prompt markdown directory (plus `_system.md`) |

To develop this software, see [CONTRIBUTING.md](CONTRIBUTING.md).
