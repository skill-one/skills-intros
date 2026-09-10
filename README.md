# skills-profiles

Chinese multi-angle profiles for the [agent skills](https://www.skills.sh) collected by
[skill-one/skills-sh-mirror](https://github.com/skill-one/skills-sh-mirror): a queryable index
(`skills.jsonl`) carrying each skill's category and persona, plus all seven written profiles per
skill (`skills/`). Profiles are LLM-generated from each skill's `SKILL.md` and published as whole
snapshots — a snapshot is self-contained, so nothing else is needed to read it.

中文: [README.zh-CN.md](README.zh-CN.md) · Dev guide (produce / extend this data): [DEVELOPING.md](DEVELOPING.md)

## What the data is

```
├── skills.jsonl   one row per profiled skill, sorted by id — filter / join / rank here
├── stats.json     how far generation has got: per-prompt coverage, complete/remaining/stale
└── skills/        one directory per skill, named after its id
    └── vercel-labs/skills/find-skills/   ({owner}/{repo}/{slug})
        ├── domain.json  scenario.json  blackbox.json  whitebox.json
        ├── tagline.json persona.json   comments.json
        └── md/          the same seven rendered as markdown, for reading
```

Each `skills.jsonl` row (a real one):

```json
{
  "id": "vercel-labs/skills/find-skills",
  "hash": "b146008599c31057cef1c145774cea5d5afb30e8f43fa802e47a4b461419aaaf",
  "domain": {
    "domain": "开发编程",
    "reason": "面向开发者的技能包检索与安装工具, 属于 agent 开发工具链生态"
  },
  "persona": {
    "tool": "npx skills",
    "role": "技能猎头",
    "scene": "你说「这活你不会吧」时,我出门找一个现成的技能装上"
  }
}
```

| Field     | Meaning                                                                                        |
| --------- | ---------------------------------------------------------------------------------------------- |
| `id`      | the skills.sh skill id, `{owner}/{repo}/{slug}` — identical to the mirror's ids                |
| `hash`    | SHA-256 of the skill's files, as recorded upstream: the profile describes exactly this content |
| `domain`  | `domain`: one of 13 fixed usage-scenario categories; `reason`: one line of justification       |
| `persona` | the skill as an occupation — `tool` it lives by, `role` it plays, `scene` it shows up in       |

`domain.domain` is a closed enum, so it is directly filterable: 开发编程 · 测试与质量 · 数据分析 ·
运维与安全 · 办公效率 · 内容创作 · 设计多媒体 · 知识管理 · 商业运营 · 支付金融 · 教育学习 · 生活服务 · 其他.

The index folds in only the two angles you actually filter on. The other five are per-skill files,
each with its own schema — seven angles in total:

| Prompt     | Shape                                    | Content                                                               |
| ---------- | ---------------------------------------- | --------------------------------------------------------------------- |
| `domain`   | `{domain, reason}`                       | category + why — also in the index                                    |
| `persona`  | `{tool, role, scene}`                    | occupational portrait — also in the index                             |
| `scenario` | `{text}`                                 | one ≤100-character pitch, built on the user's pain point              |
| `tagline`  | `{taglines[3]}`                          | three slogans, ≤20 characters each                                    |
| `blackbox` | `{function, input_output[3–5]}`          | outside view: what you hand it → what you get back, no internals      |
| `whitebox` | `{execution_flow[3–5], mechanisms[2–3]}` | inside view: happy path, key mechanisms, real dependencies            |
| `comments` | `{comments[4–6]}`                        | first-person user notes; `category` typically 妙用 / 坑 / 注意 / 启发 |

`{...[n–m]}` = an array of that many entries; `input_output` items are `{input, output}`, `comments`
items `{user, category, comment}`. An excerpt of one `comments.json`:

```json
{
  "comments": [
    {
      "user": "后端老兵",
      "category": "妙用",
      "comment": "用 --owner 锁定官方源: npx skills find react --owner vercel-labs, 结果只剩 Vercel 家的, 不会被野包污染。"
    },
    {
      "user": "团队技术负责人",
      "category": "坑",
      "comment": "只看搜索第一页就装, 换来个 80 安装量的弃坑包, 出问题没人管。现在先看安装量和 GitHub stars, 低于 100 的直接 pass。"
    }
  ]
}
```

Every published skill carries all seven angles; `stats.json` adds how many skills there are and says
what the profiles were built against:

```json
{
  "prompts": {
    "blackbox": 334,
    "comments": 334,
    "domain": 334,
    "persona": 334,
    "scenario": 334,
    "tagline": 334,
    "whitebox": 334
  },
  "skills": { "complete": 334, "remaining": 8625, "stale": 0, "total": 8959 },
  "snapshot": { "ref": "dist-2026-09-09", "fetched_at": "2026-09-09T02:01:24Z" }
}
```

`skills.total` is the upstream snapshot's size, `skills.complete` the part already profiled — the
rest is still queued. `snapshot.ref` names the mirror tag these hashes belong to (see
[Join with the mirror](#join-with-the-mirror)). The counters are rewritten at the end of each
`generate` publish, so a `sync` that only drops invalidated profiles can leave them slightly ahead
of the tree; when an exact count matters, count `skills.jsonl` lines.

Two guarantees the layout itself enforces:

- The index is a projection of the per-skill files, re-derived from disk on every rewrite: a row
  exists if and only if its directory exists, and its `domain` / `persona` can never disagree with
  the json on disk.
- `hash` is the content the profiles were generated from. When upstream rewrites a skill, its
  profiles are dropped rather than left describing something else — a published row is always
  honest about which version of the skill it talks about.

`*.json` is the machine form and the cache marker; `md/*.md` is the same text laid out for humans.
Everything but ids, paths and field names is Chinese.

## How to get the data

Published to the [`dist` branch](../../tree/dist) — the branch root _is_ the profile snapshot, so every
commit is a complete state, and the same tree is browsable on the web. Coverage grows publish by
publish — count `skills.jsonl` lines for the exact number — and the profiles are under 1 MB
compressed. Individual files pull over HTTP; the whole branch clones in one request. Note that `dist`
also carries an internal `cache/skills-sh/` dataset mirror (the upstream `SKILL.md` files) that CI
restores so `generate` never re-fetches upstream — it is not part of the profile API, but a full
branch clone/tarball does include it (~120 MB of text). Fetching files by path is unaffected.

### Fetch individual files

No clone, no auth. Start from the index to pick ids, then fetch any angle of any skill by path:

```bash
curl -sO https://raw.githubusercontent.com/skill-one/skills-profiles/dist/skills.jsonl

# dist/skills/<id>/<prompt>.json — or md/<prompt>.md to read it in the terminal
curl -s https://raw.githubusercontent.com/skill-one/skills-profiles/dist/skills/vercel-labs/skills/find-skills/md/persona.md
```

The index is small (≈130 KB at today's coverage), so pulling it whole is cheap.
GitHub serves these with a ~5-minute cache, so `dist` URLs always track the latest publish.

Filtering needs nothing beyond jq — every 设计多媒体 skill with its persona's role:

```bash
curl -s https://raw.githubusercontent.com/skill-one/skills-profiles/dist/skills.jsonl |
  jq -r 'select(.domain.domain == "设计多媒体") | [.id, .persona.role] | @tsv'
```

### Clone the whole snapshot

```bash
git clone --depth 1 -b dist https://github.com/skill-one/skills-profiles.git

# or one request, no git history at all:
curl -sL https://codeload.github.com/skill-one/skills-profiles/tar.gz/refs/heads/dist |
  tar -xz --strip-components=1
```

### Pin a snapshot

Each publish is tagged, and tags are immutable — pin one and your view never changes under you:
`dist-YYYY-MM-DD` is a day's dataset baseline (written by `sync`, force-updated within the day),
`dist-YYYY-MM-DD-N` the Nth batch of profiles on top of it (written by `generate`). Retention is a
rolling window (default one month); publishes predating the sync/generate split carry a
`dist-YYYYMMDDHHMM` form instead, which the resolver below handles the same way.

```bash
# newest published tag
latest=$(git ls-remote --tags --refs https://github.com/skill-one/skills-profiles.git 'refs/tags/dist-*' \
         | awk -F/ '{print $NF}' | sort -Vr | head -1)
curl -sO "https://raw.githubusercontent.com/skill-one/skills-profiles/$latest/skills.jsonl"
git clone --depth 1 -b "$latest" https://github.com/skill-one/skills-profiles.git
```

Cache by tag and re-fetch only when a newer one appears — a tag's content never changes, so this is
the cheap way to stay near-current without re-downloading on every poll.

### Join with the mirror

Install counts, stars, descriptions and the `SKILL.md` sources themselves are deliberately not
duplicated here — they live in [skills-sh-mirror](https://github.com/skill-one/skills-sh-mirror),
whose dataset this one was generated from. The keys are the same: `id` joins the rows, `hash`
proves the content matches. To join on hash too, pin upstream to the tag named in `stats.json`
(`snapshot.ref`) — against a moving `dist` branch, a few hashes will always have drifted:

```bash
curl -sO https://raw.githubusercontent.com/skill-one/skills-profiles/dist/stats.json
up=$(jq -r .snapshot.ref stats.json)   # e.g. dist-2026-09-09
curl -s "https://raw.githubusercontent.com/skill-one/skills-sh-mirror/$up/skills.jsonl" -o up.jsonl
curl -s https://raw.githubusercontent.com/skill-one/skills-profiles/dist/skills.jsonl -o mine.jsonl

# id  installs  category  role
jq -r --slurpfile up up.jsonl '($up | map({(.id): .installs}) | add) as $i
  | [.id, $i[.id], .domain.domain, .persona.role] | @tsv' mine.jsonl
```

The same `id` also resolves to the skill's skills.sh page
(`https://www.skills.sh/<id>`) and, in the mirror, to its upstream files.

Profiles are built by this repository's `sync` and `generate` workflows (manually triggered on
GitHub Actions: `gh workflow run generate.yml -f limit=50`). To run the pipeline yourself, add an
angle, or regenerate a skill: [DEVELOPING.md](DEVELOPING.md).
