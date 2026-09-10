# 开发 skills-profiles

[README.zh-CN.md](README.zh-CN.md) 里那份数据的生成器：它从
[skills-sh-mirror](https://github.com/skill-one/skills-sh-mirror) 读取每个 skill 的 `SKILL.md`，
按七个角度让 OpenAI 兼容的 LLM 产出结构化档案，并发布到本仓库的 `dist` 分支。
只要数据的请先看 README。

English: [DEVELOPING.md](DEVELOPING.md)

## 快速开始

需要 Python 3.12+ 和 [uv](https://docs.astral.sh/uv/)；LLM 凭据放在本地 `.env`
（复制 [`.env.example`](.env.example)——除镜像和你自己的端点外，不访问任何网络）。

```bash
uv sync
skills-profiles sync            # 下载上游快照（tag 未变则跳过）
skills-profiles run --limit 10  # 生成档案，按安装量从高到低；已缓存的不花钱
```

想离线走通全流程、不调任何 API：`skills-profiles run --limit 5 --dry-run`。

## 命令行

| 命令 | 作用 |
|---|---|
| `sync [--refresh]` | 把镜像的 `dist` 分支作为一个 tarball 拉到 `cache/skills-sh`，只解压 `skills.jsonl` 和每个 `SKILL.md`。tag 记在 `SNAPSHOT.json`，未变则跳过下载（`--refresh` 强制）。从不碰产物。 |
| `run [--limit N] [--prompts a,b] [--concurrency C] [--dry-run] [--debug] [--verbose]` | 只补缺口：按安装量排序取 N 个仍有缺失的 skill（`0` = 全部）。已缓存以及快照里没有 `SKILL.md` 的 skill 会被跳过且不占名额。 |
| `invalidate [--skill ID]... [--prompts a,b] [--stale] [--all]` | 删除缓存输出，让下一次 `run` 重算。`--stale` 选上游 hash 变化或已从快照消失的 skill（先 `sync`）。无任何筛选条件时必须显式 `--all`。 |

重算从来不是 `run` 的参数：`invalidate` 删，`run` 补。每次 run 打印计时汇总并覆盖
`output/stats.json`（描述产物现状，而非单次执行）。单个 skill 的失败（余额、连接等）会被隔离：
run 继续，已完成的 prompt 保留并随本轮发布，只有全军覆没（所有选中 skill 都失败）才以非零码退出。

## 工作原理

```
镜像 dist 分支 tarball ──► cache/skills-sh (skills.jsonl + skills/<id>/SKILL.md)
                                 │
                                 └─► 按安装量取 --limit 个仍有缺失的 ──► 每 skill 执行 prompt DAG
                                        ──► output/skills/<id>/<prompt>.json
                                        ──► output/skills/<id>/md/<prompt>.md
                                        ──► output/skills.jsonl (id + hash + domain + persona)
```

`output/`（产物）与 `cache/skills-sh`（上游数据）是两个独立根目录：从上游取到的东西永远不会
写进产物目录。

Prompt DAG（边表示「依赖其输出」）：

```
domain   scenario   blackbox   whitebox   tagline   persona   comments
# 当前无依赖边: 每个内置 prompt 都是根节点
# 在 frontmatter 里加 `depends_on: [scenario]` 即可串联
```

关键设计决策：

- **不引入编排框架。** DAG 排序用 Python 标准库
  [`graphlib.TopologicalSorter`](https://docs.python.org/3/library/graphlib.html)。
- **结构化输出。** 每个 prompt 在 frontmatter 的 `output:` 声明一个 pydantic schema；LLM 调用经
  [instructor](https://python.useinstructor.com/) 走 OpenAI 兼容客户端。schema 都在 `models.py`，
  13 个取值的 `Domain` 分类体系也定义在那里。
- **基于文件的断点续跑。** 每个 prompt 的输出是自己的 `<prompt_id>.json`（`md/` 下有 markdown
  副本），一生成即落盘——一个文件同时是产物和缓存：存在且通过 schema 校验就不调 LLM。先写 markdown
  再写 json，所以崩溃只会留下多余的 markdown，不会出现没有副本的 json。续跑粒度是 prompt 级。
- **索引是投影。** `skills.jsonl` 每次全量重写、内容来自磁盘——`id`、生成时的 `hash`，以及从各自
  json 重读的 `domain`/`persona`——所以行不可能与文件漂移，聚合字段写入早于该 prompt 存在的行也会在
  下次重写时自愈。它是 `invalidate --stale` 比对 hash 的依据；`run` 和 `sync` 都不做比对。
- **一次请求拿整个快照。** `sync` 用 codeload 把分支作为一个 tarball 下载，并整包替换上一次快照
  ——没有逐文件下载，也不需要额外的失效逻辑。解压的只有真正会读的内容；分支里还镜像了完整 skill
  仓库（README、evals、manifest 等），约 70 倍体积且从不读取。上游每天为抓取结果打
  `dist-<日期>` tag，因此重复 sync 只花一次很小的请求。在 CI 里，快照从我们自己的 `dist`
  （其中镜像了数据集）恢复，所以 `sync` 只有当恢复来的 marker 落后于最新上游 tag 时才会重新下载。
- **Prompt 即文件。** `prompts/` 下一个 markdown 文件一个 prompt，文件名即 prompt id；YAML
  frontmatter 存元数据，正文是 jinja2 用户提示词模板，`_system.md` 是共享 system prompt。

### 局部重跑

`run --prompts <id>` 先算目标 prompt 的依赖闭包，只生成闭包里缺失的部分。依赖属于输入，因此复用
已存的 json，仅在缺失或 schema 校验失败时重算。闭包之外的 prompt 完全不动——选择之外的输出绝不会
意外重算。某 skill 若一个输出都不剩，会从 `skills.jsonl` 除名，即重新视为全新 skill。

## 新增一个 prompt

一个 markdown 文件就是一个 prompt——除非需要新的输出 schema（那就在 `models.py` 注册），不必改代码：

```markdown
---
description: 一行说明
output: IntroText          # models.py 中注册的 pydantic schema
depends_on: [scenario]     # DAG 依赖; 根节点可省略
---

请为下面的 skill 写……
{{ deps.scenario.text }}   # deps 将 prompt id 映射到其解析后的输出对象
```

`_system.md` 提供 `{{ skill.name }}`、`{{ skill.description }}` 和完整的 `{{ skill_md }}`
（截断到 20,000 字符），因此 prompt 文件只需描述任务本身。然后为所有 skill 补这一角度——已缓存的
角度会复用，只有新角度花钱：

```bash
skills-profiles run --prompts my_angle --limit 0
```

要不要进索引由你决定：把 prompt id 加进 `outputs.py` 的 `AGGREGATED_PROMPTS`，从下一次重写起它就会
折进每一行 `skills.jsonl`。

## 项目结构

```
prompts/               # 每个 prompt 一个 md 文件（+ _system.md）
src/skills_profiles/
├── config.py          # 配置（pydantic-settings）
├── data.py            # 镜像 tarball 下载 + 索引解析 + 过期判定
├── models.py          # 领域分类体系 + 结构化输出 schema
├── prompts.py         # frontmatter 加载 + DAG 排序 + jinja2 渲染
├── llm.py             # instructor/openai client + 离线 FakeLLM
├── generate.py        # 异步 DAG 执行 + 文件断点续跑 + 覆盖率统计
├── outputs.py         # 每 prompt 的 json 输出 + md/ 渲染 + 索引 + 失效
├── logging.py         # --verbose 日志配置
└── cli.py             # typer 命令（sync / invalidate / run）
.github/actions/publish-dist/   # 两条工作流共用的发布步骤
tests/                 # 离线 fixture + 端到端 CLI 测试
```

## 配置

优先级从高到低：`SKILLS_PROFILES_*` 环境变量 → 本地 `.env` → 内置默认值。

| 变量 | 默认值 | 说明 |
|---|---|---|
| `SKILLS_PROFILES_MODEL` | `gpt-4.1-mini` | 任意 OpenAI 兼容模型 |
| `SKILLS_PROFILES_BASE_URL` | 无 | OpenAI 兼容端点 |
| `SKILLS_PROFILES_API_KEY` | 无 | 端点 API key |
| `SKILLS_PROFILES_LIMIT` | `10` | 每次 run 生成的 skill 数（`0` = 全部；已缓存的跳过不计数） |
| `SKILLS_PROFILES_CONCURRENCY` | `2` | LLM 最大并发调用数，跨 skill 及 skill 内 prompt 共享 |
| `SKILLS_PROFILES_OUTPUT_DIR` | `output` | 产物目录 |
| `SKILLS_PROFILES_DATA_DIR` | `cache/skills-sh` | 上游数据目录 |
| `SKILLS_PROFILES_PROMPTS_DIR` | `prompts` | prompt markdown 目录（含 `_system.md`） |

## 发布（GitHub Actions）

两条手动触发的工作流共用同一个发布锁（`concurrency: publish-dist`），按职责拆分：

| 工作流 | 流水线 | Tag |
|---|---|---|
| [`sync`](.github/workflows/sync.yml) | 恢复 dist → 同步上游 → `invalidate --stale` → 发布 | `dist-YYYY-MM-DD`（同日内 force 覆盖） |
| [`generate`](.github/workflows/generate.yml) | 恢复 dist → `run --limit <输入，默认 10>` → 发布 | `dist-<base>-N`（base = 最近一次 sync 的 tag，N 递增） |

两条工作流共用两个 composite action：[`restore-dist`](.github/actions/restore-dist/action.yml)
（一个 codeload 请求把分支拉回到 `output/` 和 `cache/`）与
[`publish-dist`](.github/actions/publish-dist/action.yml)（把工作目录镜像回 `dist`、打 tag、按时间窗
剪枝）。`dist` 是唯一的原子快照：根目录是档案，外加 `cache/skills-sh/` 数据集镜像。正因为数据集随
快照一起走，**只有 `sync` 会碰上游**——恢复来的 marker 落后于最新 tag 时才重新下载；`generate` 只读
上一次 `sync` 发布的数据集，绝不回源。历史按滚动时间窗剪枝（默认 `1 month`；无论多久没更新，最新 1 条
commit 和每种 pattern 最新 1 个 tag 始终保底）。

```bash
gh workflow run generate.yml -f limit=50 -f concurrency=8   # 跑一批档案
gh workflow run sync.yml                                    # 刷新上游，丢弃过期档案
```

需在 Settings → Secrets and variables → Actions 配置：

| 位置 | 名称 | 示例 |
|---|---|---|
| Secret | `SKILLS_PROFILES_API_KEY` | 端点对应的 API key |
| Variable | `SKILLS_PROFILES_BASE_URL` | `https://api.b.ai/v1` |
| Variable | `SKILLS_PROFILES_MODEL` | `GLM-5.3-Flash` |

## 测试

整条管道均离线验证：数据解析、DAG 排序、模板渲染、续跑跳过、失效、依赖传递、markdown 渲染，以及
完整的 CLI dry-run——都不需要网络（`llm.py` 提供 `FakeLLM`；`conftest.py` 把 `data._download`
换成由 fixture 构造快照 tarball 的假服务）。

```bash
uv run pytest
```

文档规范：每份英文文档都要有对应中文版（`README.md` / `README.zh-CN.md`、
`DEVELOPING.md` / `DEVELOPING.zh-CN.md`），同一轮改动里保持同步。
