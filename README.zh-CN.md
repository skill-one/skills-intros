# skills-intros

为 [skill-one/skills-sh-scraper](https://github.com/skill-one/skills-sh-scraper) 收录的
[agent skills](https://www.skills.sh) 批量生成多角度中文介绍词。

- 只想要产物？看[产物](#产物)。
- 想运行或新增 prompt？看[快速开始](#快速开始)。
- 想参与开发？看 [CONTRIBUTING.zh-CN.md](CONTRIBUTING.zh-CN.md)。

> English documentation: [README.md](README.md)

## 产物

每个 skill 在 `output/skills/` 下有一个独立目录：

```
output/
├── hashes.json                          # skill id -> 生成该产物时对应的上游内容 hash
└── skills/<owner>/<repo>/<skill>/
    ├── domain.json                      # 每个 prompt 一个 json
    ├── scenario.json
    └── md/                              # 供浏览的 markdown 副本
        ├── domain.md
        └── ...
```

- 目录名即 `skills.jsonl` 里的 `id`, 与上游 `skills/` 布局一致。
- 每个 prompt 的结构化输出存放在自己的 `<prompt_id>.json` 里(缓存的提交标记); 供浏览的 markdown 副本放在 `md/<prompt_id>.md`, 目录本身只放 json。
- 内置 prompt: `domain`、`scenario`、`blackbox`、`whitebox`、`tagline`、`persona`、`comments`。

`hashes.json` 为每一个已生成产物的 skill 记下生成时的上游内容 hash。有效性判定
发生在 `sync` 时——每次 sync 把记录的 `hash` 与刚下载的快照逐一对比, 上游 hash 变化
(或 skill 已从上游消失)的条目连同产物目录立即删除, 下次 `run` 重新生成; `run` 本身只信任
磁盘上现有的输出文件。

## 数据

生成的介绍词与其所依据的上游 skills 数据分处两个独立的根目录
(`output/` 与 `cache/skills-sh`, 均可通过环境变量覆盖), 两个来源互不混淆,
介绍词产物还可以单独发布:

```
cache/skills-sh/                            # SKILLS_INTROS_DATA_DIR: 上游 skills 基本信息
├── skills.jsonl                            # 索引: 每个 skill 一行 json
└── skills/<owner>/<repo>/<skill>/SKILL.md  # 每个 skill 的源文件
```

`sync` 一次请求把整个 dist 分支打包下载(tarball)并完整解压到这里, 不再逐个文件懒下载。
`cache/skills-sh` 下的一切都只是 dist 分支的可重下副本: 每次 sync 整包替换, 索引与源文件
因此不可能出现版本错位。

## 快速开始

需要 Python 3.12+ 和 [uv](https://docs.astral.sh/uv/)。

```bash
uv sync
# LLM 凭据: 在本地 .env 中配置 KEY / BASE_URL / MODEL（参见 .env.example）
skills-intros sync            # 下载 dist 分支快照（并清理失效产物）
skills-intros run --limit 50  # 为 50 个 skill 生成介绍词（按安装量从高到低）
```

`--limit` 限制的是「本次真正生成的数量」: 已缓存完全的 skill 会被跳过且不占用额度,
因此反复执行会沿着列表持续推进。

`run` 的更多选项:

```bash
skills-intros run --limit 0           # 所有还有缺失 prompt 的 skill
skills-intros run --prompts tagline   # 只为所有 skill 生成这一个 prompt
skills-intros run --limit 5 --dry-run # 用离线假 LLM 冒烟测试
skills-intros run --limit 5 --debug   # 把最终发给 LLM 的 prompt 打印到 stderr
skills-intros run --verbose           # 开启 DEBUG 级别的执行日志
```

重跑天然支持断点续传: 每个 prompt 的输出一生成即落盘, 因此即使中途崩溃, 也只有缺失的
prompt 才会真正调用 LLM。拆分布局之前写入的结果(每个 skill 一个 `result.json`)会被忽略
并重新生成。

需要重算时先让缓存失效再跑——这与 `sync` 发现上游内容 hash 变化时走的是同一条路径:

```bash
skills-intros invalidate --prompts whitebox        # 所有 skill 的这一个 prompt
skills-intros invalidate --skill owner/repo/name   # 某个 skill 的全部 prompt
skills-intros invalidate --skill owner/repo/name --prompts whitebox
skills-intros invalidate --all                     # 全部清空(需显式 --all)
```

## 持续生成（GitHub Actions）

`.github/workflows/generate.yml` 定时（也可手动）执行, 让 `dist` 分支始终与生成的介绍保持同步:

```
恢复（dist 分支 tarball）→ sync → run → 发布
```

每次执行都是全新 runner, 因此先把上一次的产物从 `dist` 拉回来: 这个分支既是发布产物, 也是缓存。
顺序很关键——`sync` 的失效清理依赖刚恢复回来的那些产物。`SKILLS_INTROS_LIMIT`（手动运行时是 `limit`
输入, 默认 2）限制单次生成量, 反复执行就能逐步覆盖整个数据集。

`dist` 分支的根目录与 `output/` 一致: `hashes.json` + `skills/`（参见[产物](#产物)）。

需要在仓库 Settings → Secrets and variables → Actions 里配置:

| 位置        | 名称                       | 示例                    |
| --------- | ------------------------ | --------------------- |
| Secret    | `SKILLS_INTROS_API_KEY`  | 端点对应的 API key         |
| Variable  | `SKILLS_INTROS_BASE_URL` | `https://api.b.ai/v1` |
| Variable  | `SKILLS_INTROS_MODEL`    | `GLM-5.3-Flash`       |

定时为 `*/10 * * * *`, 可与 limit 一起调整。

## 新增一个 prompt

`prompts/` 下一个 markdown 文件即一个 prompt, 文件名就是 prompt id。
共享的 `_system.md` 是 system prompt, 按 skill 逐次渲染: 它承载每个 prompt 都能看到的
skill 上下文——`{{ skill.name }}` 与 `{{ skill.description }}`(均取自 `skills.jsonl`)
和完整的 `{{ skill_md }}` 原文(每个 skill 的 `SKILL.md`, 按需从 dist 分支下载)——因此各
prompt 文件只需描述任务本身。

```markdown
---
description: 一行说明
output: IntroText          # models.py 中注册的 pydantic schema
depends_on: [scenario]   # DAG 依赖; 根节点可省略
---

请为下面的 skill 写……
{{ deps.scenario.text }}   # deps 将 prompt id 映射到其解析后的输出对象
```

然后为所有 skill 生成（已缓存的 prompt 一律复用, 只生成缺失的——需要重算请先 `invalidate`）:

```bash
skills-intros run --prompts my_angle --limit 0
```

## 配置

配置按优先级从高到低: `SKILLS_INTROS_*` 环境变量 → 本地 `.env` → 内置默认值。

| 变量                          | 默认值            | 说明                                         |
| --------------------------- | -------------- | ------------------------------------------ |
| `SKILLS_INTROS_MODEL`       | `gpt-4.1-mini` | 任意 OpenAI 兼容对话模型                           |
| `SKILLS_INTROS_BASE_URL`    | 无              | OpenAI 兼容端点覆盖                              |
| `SKILLS_INTROS_API_KEY`     | 无              | 端点对应的 API key                             |
| `SKILLS_INTROS_LIMIT`       | `50`           | 每次 run 生成的 skill 数量（按安装量，`0` = 全部）; 已缓存的跳过不计数      |
| `SKILLS_INTROS_CONCURRENCY` | `8`            | LLM 最大并发调用数                                |
| `SKILLS_INTROS_OUTPUT_DIR`  | `output`       | 生成的介绍: `hashes.json` + `skills/`              |
| `SKILLS_INTROS_DATA_DIR`    | `cache/skills-sh`  | 上游 skills 基本信息: `skills.jsonl` + 缓存的 `SKILL.md`      |
| `SKILLS_INTROS_PROMPTS_DIR` | `prompts`      | prompt markdown 文件所在目录(含 `_system.md`)          |
