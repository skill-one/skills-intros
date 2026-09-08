# skills-intros

Generate multi-angle Chinese introductions for [agent skills](https://www.skills.sh) collected by
[skill-one/skills-sh-scraper](https://github.com/skill-one/skills-sh-scraper).

- Just want the results? See [Artifacts](#artifacts).
- Want to run it or add a prompt? See [Quickstart](#quickstart).
- Want to develop this software? See [CONTRIBUTING.md](CONTRIBUTING.md).

## Artifacts

Each skill gets one directory under `output/results/skills/`:

```
output/results/skills/<owner>/<repo>/<skill>/
├── result.json        # machine-readable record
├── domain.md          # one markdown per prompt, for easy browsing
├── one_liner.md
├── dev_intro.md
├── scenario_intro.md
├── comparison.md
├── trigger_guide.md
└── tagline.md
```

- The directory name is the skill `id` from `skills.jsonl`, mirroring the upstream `data/skills/` layout.
- `result.json` is `{"skill": <upstream record incl. content hash>, "intros": {<prompt_id>: <structured output>}}` — the single source of truth.
- Built-in prompts: `domain`, `one_liner`, `dev_intro`, `scenario_intro`, `comparison`, `trigger_guide`, `tagline`.

Freshness: `result.json` stores the upstream content hash for auditing, but validity is
decided at `sync` time — each sync compares stored results against the freshly downloaded
snapshot and immediately prunes those whose upstream hash changed or whose skill
disappeared. `run` itself just reuses whatever `result.json` is on disk.

## Quickstart

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/).

```bash
uv sync
# LLM credentials: put KEY / BASE_URL / MODEL in a local .env (see .env.example)
skills-intros sync            # download the latest dist-branch snapshot (prunes stale results)
skills-intros run --top 50    # generate intros for the top 50 skills by installs
```

More `run` options:

```bash
skills-intros run --top 0             # all usable skills
skills-intros run --force             # regenerate even if results exist
skills-intros run --prompts tagline   # (re)generate one prompt for all skills
skills-intros run --top 5 --dry-run   # offline smoke test with a fake LLM
skills-intros run --top 5 --debug     # print the rendered prompts sent to the LLM (stderr)
skills-intros run --verbose           # enable DEBUG-level run logs
```

Re-runs resume for free: only skills without an existing `result.json` cost LLM calls.

## Adding a prompt

One markdown file under `prompts/` is one prompt; the file name is the prompt id.
The shared `_system.md` is the system prompt, rendered once per skill: it carries
the skill context every prompt sees — `{{ skill.name }}` and `{{ skill.description }}`
(both from `skills.jsonl`) and the full `{{ skill_md }}` source text (the per-skill
`SKILL.md` file) — so prompt files only describe the task.

```markdown
---
description: one line
output: IntroText          # a pydantic schema registered in models.py
depends_on: [dev_intro]    # DAG edges; omit for root prompts
---

请为下面的 skill 写……
{{ deps.dev_intro.text }}   # deps maps prompt ids to their parsed output objects
```

Then generate it for every skill (already-cached prompts are reused; only missing
ones are generated — add `--force` to regenerate):

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
| `SKILLS_INTROS_WORKDIR` | `output` | Holds `data/` and `results/` |
| `SKILLS_INTROS_PROMPTS_DIR` | `prompts` | Directory with one prompt markdown per file, plus `_system.md` |
