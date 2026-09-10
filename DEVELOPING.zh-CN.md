# 开发 skills-profiles

[README.zh-CN.md](README.zh-CN.md) 里那份数据的生成器：它从
[skills-sh-mirror](https://github.com/skill-one/skills-sh-mirror) 读取每个 skill 的 `SKILL.md`，
按八个角度让 OpenAI 兼容的 LLM 产出结构化档案，从其中一个角度渲染出封面配图，并发布到本仓库的
`dist` 分支。只要数据的请先看 README。

English: [DEVELOPING.md](DEVELOPING.md)

## 快速开始

需要 Python 3.12+ 和 [uv](https://docs.astral.sh/uv/)；LLM 凭据放在本地 `.env`
（复制 [`.env.example`](.env.example)——除了镜像、你自己的端点，以及渲染配图时用到的图像端点外，
不访问任何网络）。

```bash
uv sync
skills-profiles sync            # 下载上游快照（tag 未变则跳过）
skills-profiles run --limit 10  # 生成档案，按安装量从高到低；已缓存的不花钱
skills-profiles covers --limit 10       # 渲染它们的封面配图，按安装量从高到低
```

想离线走通全流程、不调任何 API：`skills-profiles run --limit 5 --dry-run` 以及
`skills-profiles covers --limit 5 --dry-run`（后者会写出一张占位 png）。

## 命令行

| 命令 | 作用 |
|---|---|
| `sync [--refresh]` | 把镜像的 `dist` 分支作为一个 tarball 拉到 `cache/skills-sh`，只解压 `skills.jsonl` 和每个 `SKILL.md`。tag 记在 `SNAPSHOT.json`，未变则跳过下载（`--refresh` 强制）。从不碰产物。 |
| `run [--limit N] [--prompts a,b] [--concurrency C] [--dry-run] [--debug] [--verbose]` | 只补缺口：按安装量排序取 N 个仍有缺失的 skill（`0` = 全部）。已缓存以及快照里没有 `SKILL.md` 的 skill 会被跳过且不占名额。 |
| `covers [--limit N] [--concurrency C] [--dry-run] [--verbose]` | 为已经写好 `cover` prompt 的 skill 渲染 `cover.png`，取 N 个（`0` = 所有待渲染的）。不画任何文字，已有配图的绝不再渲染；需要 `SKILLS_PROFILES_IMAGE_API_KEY`。 |
| `invalidate [--skill ID]... [--prompts a,b] [--stale] [--all]` | 删除缓存输出，让下一次 `run` 重算。`--stale` 选上游 hash 变化或已从快照消失的 skill（先 `sync`）。无任何筛选条件时必须显式 `--all`。失效 `cover` 会连同它的 `cover.png` 一起删掉，这正是重画一张配图的唯一途径。 |

重算从来不是 `run` 的参数：`invalidate` 删，`run` 补。每次 run 打印计时汇总并覆盖
`output/stats.json`（描述产物现状，而非单次执行）。单个 skill 的失败（余额、连接等）会被隔离：
run 继续，已完成的 prompt 保留并随本轮发布，只有全军覆没（所有选中 skill 都失败）才以非零码退出。
`covers` 出于同样的原因，遵循同样的规则。

两条命令都工作在同一道数据集封顶之内，即 `SKILLS_PROFILES_TOTAL_LIMIT`（默认 1000）：无论单次 run 的
`--limit` 多大，只有安装量最高的前 N 个 skill 会被生成档案或绘制配图。它是一个排名窗口，而非「已完成了多少个」
的计数——排在前面但配方还没写好、或渲染失败的 skill 会占着名额而不让位给后面的，所以重跑和 `invalidate`
重画都复用同一批 N 个。由于它只是一个设置，它就同时封顶了档案与配图（也封顶了 `dist` 能装下的配图总重量，
因为每张约 1.7 MB）；而 `--limit` 与 `SKILLS_PROFILES_IMAGE_LIMIT` 仍是这道封顶*之内*的单次预算，
CI 则从默认值继承这道封顶。

## 工作原理

```
镜像 dist 分支 tarball ──► cache/skills-sh (skills.jsonl + skills/<id>/SKILL.md)
                                 │
                                 └─► 按安装量取 --limit 个仍有缺失的 ──► 每 skill 执行 prompt DAG
                                        ──► output/skills/<id>/<prompt>.json
                                        ──► output/skills/<id>/md/<prompt>.md
                                        ──► output/skills.jsonl (id + hash + domain + persona)
                        cover.json + domain.json ──► `covers` 调用图像端点
                                                ──► output/skills/<id>/cover.png
```

`output/`（产物）与 `cache/skills-sh`（上游数据）是两个独立根目录：从上游取到的东西永远不会
写进产物目录。

Prompt DAG（边表示「依赖其输出」）：

```
domain   scenario   blackbox   whitebox   tagline   comments      （根节点）
persona ──► cover                                                 （配图由职业画像推导而来）
# 在 frontmatter 里加 `depends_on: [scenario]` 即可串联
```

关键设计决策：

- **不引入编排框架。** DAG 排序用 Python 标准库
  [`graphlib.TopologicalSorter`](https://docs.python.org/3/library/graphlib.html)。
- **结构化输出。** 每个 prompt 在 frontmatter 的 `output:` 声明一个 pydantic schema；LLM 调用经
  [instructor](https://python.useinstructor.com/) 走 OpenAI 兼容客户端。schema 都在 `models.py`，
  13 个取值的 `Domain` 分类体系也定义在那里——每个分类都带着自己的 emoji、分类提示，以及它的配图所共用的风格。
- **基于文件的断点续跑。** 每个 prompt 的输出是自己的 `<prompt_id>.json`（`md/` 下有 markdown
  副本），一生成即落盘——一个文件同时是产物和缓存：存在且通过 schema 校验就不调 LLM。先写 markdown
  再写 json，所以崩溃只会留下多余的 markdown，不会出现没有副本的 json。续跑粒度是 prompt 级。
- **配图 = 配方 + 渲染两半。** `cover` 是一个普通 prompt，因此继承了 DAG、缓存、markdown 副本和
  `invalidate`；`images.py` 再把画面由三部分拼出来，而其中只有第一部分是模型的活：**主体**
  （`cover.json`——把职业画像画成一个正在干活的人；`ImagePrompt` 会**校验**它确实像样：纯英文、逗号短语、
  限字数，所以模型交回中文营销文案时 instructor 会重试，而不是让渲染器照着画）、**取景**（`CHARACTER`：一个全身人物居于画面中央，
  它是常量，所以任何配方都不可能把人丢掉）、**画风**（每个分类的 `Domain.cover_style`，刻意只写
  媒介/配色/光线、**不写道具**：实测过，风格里一出现道具就会抢掉主体，画出来成了静物画）。两半分开，
  也就把两种成本分开：重渲染不花 LLM 调用，重跑 DAG 也绝不会重画配图。配图的缓存就是文件本身是否存在
  （`cover.png`），因为接口返回的是一个一小时后就过期的 url——存下来的是字节，url 从不保存。
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

闭包只向依赖走，从不向依赖它的人走：失效 `persona` 之后，`cover` 配方——以及由它渲染出的
`cover.png`——仍描述着那幅旧的职业画像。这是刻意让失效保持显式，不该因为上游动了就自动重算；
真需要连带重做时把它说出来即可，例如 `invalidate --prompts persona,cover`，配图会随它的配方一起被删掉。

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

如果一个 prompt 还会产出非 json 的文件，就在 `outputs.py` 的 `PROMPT_ASSETS` 里登记它对应的后缀——
`cover` 就是这样持有 `cover.png` 的；也正因如此，失效这个 prompt 时会连同配方一起丢弃渲染出的产物，
两者永远不会对不上。

## 项目结构

```
prompts/               # 每个 prompt 一个 md 文件（+ _system.md）
src/skills_profiles/
├── config.py          # 配置（pydantic-settings）
├── data.py            # 镜像 tarball 下载 + 索引解析 + 过期判定
├── models.py          # 领域分类体系 + 结构化输出 schema
├── prompts.py         # frontmatter 加载 + DAG 排序 + jinja2 渲染
├── llm.py             # instructor/openai client + 离线 FakeLLM
├── images.py          # 文生图客户端 + 配图选择 + 离线 FakeImages
├── generate.py        # 异步 DAG 执行 + 文件断点续跑 + 覆盖率统计
├── outputs.py         # 每 prompt 的 json 输出 + md/ 渲染 + 附带文件 + 索引 + 失效
├── logging.py         # --verbose 日志配置
└── cli.py             # typer 命令（sync / invalidate / run / covers）
.github/actions/publish-dist/   # 三条工作流共用的发布步骤
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
| `SKILLS_PROFILES_TOTAL_LIMIT` | `1000` | 整条管道服务的 skill 数，按安装量从高到低——是对数据集的封顶、不是单次 run：`run` 和 `covers` 都止步于此（`0` = 全部） |
| `SKILLS_PROFILES_CONCURRENCY` | `2` | LLM 调用 / 图像请求的最大并发数，跨 skill 及 skill 内 prompt 共享 |
| `SKILLS_PROFILES_OUTPUT_DIR` | `output` | 产物目录 |
| `SKILLS_PROFILES_DATA_DIR` | `cache/skills-sh` | 上游数据目录 |
| `SKILLS_PROFILES_PROMPTS_DIR` | `prompts` | prompt markdown 目录（含 `_system.md`） |
| `SKILLS_PROFILES_IMAGE_BASE_URL` | `https://api.siliconflow.cn/v1` | 文生图端点；配图由一个自成一套的服务绘制 |
| `SKILLS_PROFILES_IMAGE_API_KEY` | 无 | 它的 key（缺了它 `covers` 拒绝运行；`--dry-run` 则不需要） |
| `SKILLS_PROFILES_IMAGE_MODEL` | `Kwai-Kolors/Kolors` | 端点提供的任意模型 |
| `SKILLS_PROFILES_IMAGE_SIZE` | `1024x1024` | 会对照端点按模型文档化的尺寸来校验 |
| `SKILLS_PROFILES_IMAGE_STEPS` | `20` | `num_inference_steps`（1–100）；填 `0` 表示不发送该字段 |
| `SKILLS_PROFILES_IMAGE_GUIDANCE` | `7.5` | `guidance_scale`（≤ 20，接口文档标注仅 Kolors 支持）；换其他模型时填 `0` 省略该字段 |
| `SKILLS_PROFILES_IMAGE_LIMIT` | `10` | 每次 run 渲染的配图数（`0` = 所有待渲染的）；对数据集的封顶由 `SKILLS_PROFILES_TOTAL_LIMIT` 决定 |

## 发布（GitHub Actions）

三条手动触发的工作流共用同一个发布锁（`concurrency: publish-dist`），按职责拆分：

| 工作流 | 流水线 | Tag |
|---|---|---|
| [`sync`](.github/workflows/sync.yml) | 恢复 dist → 同步上游 → `invalidate --stale` → 发布 | `dist-YYYY-MM-DD`（同日内 force 覆盖） |
| [`generate`](.github/workflows/generate.yml) | 恢复 dist → `run --limit <输入，默认 10>` → 发布 | `dist-<base>-N`（base = 最近一次 sync 的 tag，N 递增） |
| [`covers`](.github/workflows/covers.yml) | 恢复 dist → `covers --limit <输入，默认 20>` → 发布 | `dist-<base>-N`（与 `generate` 共用同一个计数器） |

三条工作流共用两个 composite action：[`restore-dist`](.github/actions/restore-dist/action.yml)
（一个 codeload 请求把分支拉回到 `output/` 和 `cache/`）与
[`publish-dist`](.github/actions/publish-dist/action.yml)（把工作目录镜像回 `dist`、打 tag、按时间窗
剪枝）。`dist` 是唯一的原子快照：根目录是档案，外加 `cache/skills-sh/` 数据集镜像。正因为数据集随
快照一起走，**只有 `sync` 会碰上游**——恢复来的 marker 落后于最新 tag 时才重新下载；`generate` 和
`covers` 只读上一次 `sync` 发布的数据集，绝不回源。历史按滚动时间窗剪枝（默认 `1 month`；无论多久没更新，最新 1 条
commit 和每种 pattern 最新 1 个 tag 始终保底）。

`covers` 是唯一会往快照里增加二进制体积的工作流，而它被双重封顶：`limit` 输入封顶单批数量，
`SKILLS_PROFILES_TOTAL_LIMIT` 封顶数据集（`covers` 只为安装量最高的前 N 个 skill 绘图）。每张配图实测约
1.7 MB（1024x1024），且之后每一轮都会把整棵分支再拉回来——所以是这道封顶（而非任何单次 run）决定了
`dist` 最多能装多少张配图：已存在的 `cover.png` 会被恢复并保留，绝不重新渲染。

```bash
gh workflow run generate.yml -f limit=50 -f concurrency=8   # 跑一批档案
gh workflow run covers.yml -f limit=20                       # 跑一批配图
gh workflow run sync.yml                                    # 刷新上游，丢弃过期档案
```

需在 Settings → Secrets and variables → Actions 配置：

| 位置 | 名称 | 示例 |
|---|---|---|
| Secret | `SKILLS_PROFILES_API_KEY` | 端点对应的 API key |
| Secret | `SKILLS_PROFILES_IMAGE_API_KEY` | 文生图端点的 key（只有 `covers` 需要它） |
| Variable | `SKILLS_PROFILES_BASE_URL` | `https://api.b.ai/v1` |
| Variable | `SKILLS_PROFILES_MODEL` | `GLM-5.3-Flash` |
| Variable | `SKILLS_PROFILES_IMAGE_BASE_URL`、`SKILLS_PROFILES_IMAGE_MODEL`、`SKILLS_PROFILES_IMAGE_SIZE` | 可选；默认用文档里那个 Kolors 端点、`1024x1024` |
| Variable | `SKILLS_PROFILES_TOTAL_LIMIT` | 可选；内置的 `1000` 已经同时封顶了本地和 CI，只有想改动这道封顶时才需要设置 |

## 测试

整条管道均离线验证：数据解析、DAG 排序、模板渲染、续跑跳过、失效、依赖传递、markdown 渲染、配图配方的
prompt/种子/请求体构造、端点的重试规则，以及 `run` 和 `covers` 两条完整的 CLI dry-run——都不需要网络
（`llm.py` 和 `images.py` 提供 `FakeLLM` / `FakeImages`；`conftest.py` 把 `data.download_file` 换成由
fixture 构造快照 tarball 的假服务，图像端点则只通过一个打了桩的 `urlopen` 触达）。

```bash
uv run pytest
```

文档规范：每份英文文档都要有对应中文版（`README.md` / `README.zh-CN.md`、
`DEVELOPING.md` / `DEVELOPING.zh-CN.md`），同一轮改动里保持同步。
