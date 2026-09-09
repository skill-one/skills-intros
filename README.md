# skills-intros

Generate multi-angle Chinese introductions for [agent skills](https://www.skills.sh) collected by
[skill-one/skills-sh-scraper](https://github.com/skill-one/skills-sh-scraper).

- Just want the results? See [Artifacts](#artifacts).
- Want to run it or add a prompt? See [Quickstart](#quickstart).
- Want to develop this software? See [CONTRIBUTING.md](CONTRIBUTING.md).

## Artifacts

Each skill gets one directory under `output/skills/`:

```
output/
├── hashes.json                          # skill id -> the upstream hash its intros were built from
└── skills/<owner>/<repo>/<skill>/
    ├── domain.json                      # one json per prompt
    ├── scenario.json
    └── md/                              # markdown copies for browsing
        ├── domain.md
        └── ...
```

- The directory name is the skill `id` from `skills.jsonl`, mirroring the upstream `skills/` layout.
- Each prompt's structured output lives in its own `<prompt_id>.json` (the cache commit marker); a markdown copy for easy browsing goes to `md/<prompt_id>.md`, so the directory itself stays json-only.
- Built-in prompts: `domain`, `scenario`, `blackbox`, `whitebox`, `tagline`, `persona`, `comments`.

Freshness: `hashes.json` records, for every skill that has generated intros, the upstream
content hash those intros were built from. Validity is decided at `sync` time: each sync
compares the recorded hash against the freshly downloaded snapshot and immediately prunes
entries whose upstream hash changed or whose skill disappeared. `run` itself just reuses
whatever is on disk.

## Data

Generated intros and the upstream skills data they are built from live under two
separate roots (`output/` and `cache/skills-sh`, both overridable) so the
two sources are never mixed and the intros can be published on their own:

```
cache/skills-sh/                            # SKILLS_INTROS_DATA_DIR: upstream skills basic info
├── skills.jsonl                            # the index: one json line per skill
└── skills/<owner>/<repo>/<skill>/SKILL.md  # each skill's source
```

`sync` downloads the whole dist branch as one tarball and unpacks it here — one request, no
per-file fetching. Everything under `cache/skills-sh` is a re-downloadable copy of the dist
branch: each sync replaces it wholesale, so index and sources can never drift apart.

## Quickstart

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/).

```bash
uv sync
# LLM credentials: put KEY / BASE_URL / MODEL in a local .env (see .env.example)
skills-intros sync            # download the dist branch snapshot (prunes stale results)
skills-intros run --top 50    # generate intros for the top 50 skills by installs
```

More `run` options:

```bash
skills-intros run --top 0             # all usable skills
skills-intros run --prompts tagline   # generate one prompt for all skills
skills-intros run --top 5 --dry-run   # offline smoke test with a fake LLM
skills-intros run --top 5 --debug     # print the rendered prompts sent to the LLM (stderr)
skills-intros run --verbose           # enable DEBUG-level run logs
```

Re-runs resume for free: each prompt's output is committed to disk as soon as it is
generated, so only missing prompts cost LLM calls — even after a crash mid-run.
Results written before the per-prompt layout (a single `result.json` per skill) are
ignored and regenerated.

To redo work, invalidate the cache and run again — this is the same path `sync`
uses when an upstream skill's content hash changed:

```bash
skills-intros invalidate --prompts whitebox        # one prompt, for every skill
skills-intros invalidate --skill owner/repo/name   # every prompt of one skill
skills-intros invalidate --skill owner/repo/name --prompts whitebox
skills-intros invalidate --all                     # everything (needs --all)
```

## Adding a prompt

One markdown file under `prompts/` is one prompt; the file name is the prompt id.
The shared `_system.md` is the system prompt, rendered once per skill: it carries
the skill context every prompt sees — `{{ skill.name }}` and `{{ skill.description }}`
(both from `skills.jsonl`) and the full `{{ skill_md }}` source text (the per-skill
`SKILL.md`, fetched from the dist branch on demand) — so prompt files only describe the task.

```markdown
---
description: one line
output: IntroText          # a pydantic schema registered in models.py
depends_on: [scenario]   # DAG edges; omit for root prompts
---

请为下面的 skill 写……
{{ deps.scenario.text }}   # deps maps prompt ids to their parsed output objects
```

Then generate it for every skill (already-cached prompts are reused; only missing
ones are generated — invalidate first to regenerate):

```bash
skills-intros run --prompts my_angle --top 0
```

## Configuration

Settings resolve in order (highest first): `SKILLS_INTROS_*` env vars → local `.env` →
built-in defaults.

| Variable | Default | Description |
|---|---|---|
| `SKILLS_INTROS_MODEL` | `gpt-4.1-mini` | Any OpenAI-compatible chat model |
| `SKILLS_INTROS_BASE_URL` | – | Override for OpenAI-compatible endpoints |
| `SKILLS_INTROS_API_KEY` | – | API key for the endpoint |
| `SKILLS_INTROS_TOP_N` | `50` | Skills to process (`0` = all) |
| `SKILLS_INTROS_CONCURRENCY` | `8` | Max concurrent LLM calls |
| `SKILLS_INTROS_OUTPUT_DIR` | `output` | Generated intros: `hashes.json` + `skills/` |
| `SKILLS_INTROS_DATA_DIR` | `cache/skills-sh` | Upstream skills basic info: `skills.jsonl` + the cached `SKILL.md` files |
| `SKILLS_INTROS_PROMPTS_DIR` | `prompts` | Directory with one prompt markdown per file, plus `_system.md` |
