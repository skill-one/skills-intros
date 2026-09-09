# skills-intros

Generate multi-angle Chinese introductions for [agent skills](https://www.skills.sh)
collected by [skill-one/skills-sh-mirror](https://github.com/skill-one/skills-sh-mirror).

> 中文文档: [README.zh-CN.md](README.zh-CN.md)

## Quickstart

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/); LLM credentials go in a
local `.env` (see `.env.example`).

```bash
uv sync
skills-intros sync            # download the upstream snapshot (skipped when the tag is unchanged)
skills-intros run --limit 50  # generate intros, most installed first; cached skills are skipped for free
```

More `run` options:

```bash
skills-intros run --limit 0           # every skill with missing prompts
skills-intros run --prompts tagline   # generate just this one prompt
skills-intros run --limit 5 --dry-run # offline smoke test (fake LLM, no API calls)
skills-intros run --limit 5 --debug   # print the rendered prompts to stderr
skills-intros run --verbose           # DEBUG logging
```

Re-runs resume for free: each prompt is committed to disk as soon as it is generated,
so only missing prompts cost LLM calls — even after a crash mid-run. To redo work,
invalidate first:

```bash
skills-intros invalidate --prompts whitebox        # one prompt, for every skill
skills-intros invalidate --skill owner/repo/name   # every prompt of one skill
skills-intros invalidate --stale                   # skills whose upstream content changed (or vanished)
skills-intros invalidate --all                     # everything (needs --all)
```

## Artifacts

```
output/                                      # generated intros, publishable on their own
├── hashes.json                              # skill id -> the upstream hash its intros were built from
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

## Continuous generation (GitHub Actions)

`.github/workflows/generate.yml` runs on demand (Actions → generate → Run workflow):

```
restore dist branch → sync → invalidate --stale → run --limit <input, default 100> → publish to dist
```

The `dist` branch is both the published artifact and the cache; its root mirrors
`output/`. Required configuration (Settings → Secrets and variables → Actions):

| Where | Name | Example |
|---|---|---|
| Secret | `SKILLS_INTROS_API_KEY` | the endpoint's API key |
| Variable | `SKILLS_INTROS_BASE_URL` | `https://api.b.ai/v1` |
| Variable | `SKILLS_INTROS_MODEL` | `GLM-5.3-Flash` |

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
skills-intros run --prompts my_angle --limit 0
```

## Configuration

Resolution order (highest first): `SKILLS_INTROS_*` env vars → local `.env` → built-in
defaults.

| Variable | Default | Description |
|---|---|---|
| `SKILLS_INTROS_MODEL` | `gpt-4.1-mini` | Any OpenAI-compatible chat model |
| `SKILLS_INTROS_BASE_URL` | – | OpenAI-compatible endpoint |
| `SKILLS_INTROS_API_KEY` | – | API key for the endpoint |
| `SKILLS_INTROS_LIMIT` | `50` | Skills to generate per run (`0` = all; cached skills are skipped, not counted) |
| `SKILLS_INTROS_CONCURRENCY` | `8` | Max concurrent LLM calls, shared across skills and prompts |
| `SKILLS_INTROS_OUTPUT_DIR` | `output` | Artifacts directory |
| `SKILLS_INTROS_DATA_DIR` | `cache/skills-sh` | Upstream data directory |
| `SKILLS_INTROS_PROMPTS_DIR` | `prompts` | Prompt markdown directory (plus `_system.md`) |

To develop this software, see [CONTRIBUTING.md](CONTRIBUTING.md).
