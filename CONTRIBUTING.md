# Contributing / Developer guide

Everything about developing `skills-intros` itself. User-facing docs live in
[README.md](README.md).

## How it works

```
skills.jsonl (dist branch) ──► Top N by installs ──► per-skill prompt DAG
                                                    ──► output/results/skills/<id>/result.json
                                                    ──► output/results/skills/<id>/<prompt>.md
```

Prompt DAG (edges = "depends on output of"):

```
domain ──┬── dev_intro ──┐
         ├── scenario_intro ──┼── comparison
         │                    └── trigger_guide
one_liner ── tagline
```

Key design decisions:

- **No orchestration framework.** The DAG is ordered with the stdlib
  [`graphlib.TopologicalSorter`](https://docs.python.org/3/library/graphlib.html).
- **Structured outputs.** Every prompt declares a pydantic schema (`output:` in frontmatter);
  LLM calls go through [instructor](https://python.useinstructor.com/) over an
  OpenAI-compatible client.
- **File-based resume.** Each skill's `result.json` is both the output and the cache: its
  presence short-circuits the LLM. Stale artifacts are pruned at `sync` time (upstream hash
  changed or skill dropped), so run never re-checks hashes. Resume granularity is per
  prompt — only missing or schema-invalid outputs are regenerated.
- **Prompts as files.** One markdown file per prompt under `prompts/` (override with
  `SKILLS_INTROS_PROMPTS_DIR`). YAML frontmatter carries metadata; the body is the jinja2
  user-prompt template. `_system.md` holds the shared system prompt. No code changes needed
  to add a prompt unless it needs a new output schema (then register it in `models.py`).

## Partial regeneration internals

`run --prompts <id>` computes the dependency closure of the target prompts. Target prompts
always rerun; their dependencies reuse stored outputs from `result.json` (regenerated only if
missing or `--force`); prompts outside the closure are carried over untouched, so
`result.json` stays complete after every run.

## Project layout

```
prompts/               # one markdown file per prompt (+ _system.md)
├── _system.md
├── domain.md
├── one_liner.md
├── scenario_intro.md
├── dev_intro.md
├── comparison.md
├── trigger_guide.md
└── tagline.md

src/skills_intros/
├── config.py        # settings (pydantic-settings)
├── data.py          # dist-branch tarball download + skills.jsonl parsing
├── models.py        # domain taxonomy + structured-output schemas
├── prompts.py       # frontmatter loader + DAG ordering + jinja2 rendering
├── llm.py           # instructor/openai client + offline FakeLLM
├── generate.py      # async DAG execution + file-based resume
├── outputs.py       # per-skill markdown rendering
└── cli.py           # typer commands (sync / run)
```

## Configuration resolution

`SKILLS_INTROS_*` env vars → local `.env` → built-in defaults. Implemented with
`pydantic-settings` in `config.py`.

## Testing

The whole pipeline is verified offline: dataset parsing, DAG ordering, template rendering,
resume skip/force, dependency passing, markdown rendering, and a full CLI dry-run — all
without network access (`llm.py` provides a `FakeLLM`).

```bash
uv run pytest
```

Docs rule: every English document has a Chinese counterpart (e.g. `README.md` /
`README.zh-CN.md`, `CONTRIBUTING.md` / `CONTRIBUTING.zh-CN.md`) — keep both in sync.
