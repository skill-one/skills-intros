# skills-profiles

为 [skill-one/skills-sh-mirror](https://github.com/skill-one/skills-sh-mirror) 收录的
[agent skills](https://www.skills.sh) 批量生成多角度中文档案。

> English documentation: [README.md](README.md)

## 快速开始

需要 Python 3.12+ 和 [uv](https://docs.astral.sh/uv/)；LLM 凭据放在本地 `.env`
（参见 `.env.example`）。

```bash
uv sync
skills-profiles sync            # 下载上游快照（tag 未变则跳过）
skills-profiles run --limit 10  # 生成档案，按安装量从高到低；已缓存的跳过不占额度
```

`run` 的更多选项：

```bash
skills-profiles run --limit 0           # 所有缺 prompt 的 skill
skills-profiles run --prompts tagline   # 只生成这一个 prompt
skills-profiles run --limit 5 --dry-run # 离线冒烟测试（假 LLM，无 API 调用）
skills-profiles run --limit 5 --debug   # 打印渲染后的 prompt 到 stderr
skills-profiles run --concurrency 3     # 限制 LLM 并发调用数（默认 2）
skills-profiles run --verbose           # DEBUG 日志
```

重跑天然断点续传：每个 prompt 一生成即落盘，只有缺失的才会调 LLM，中途崩溃也不丢进度。
需要重算时先失效再跑：

```bash
skills-profiles invalidate --prompts whitebox        # 所有 skill 的这一个 prompt
skills-profiles invalidate --skill owner/repo/name   # 某个 skill 的全部 prompt
skills-profiles invalidate --stale                   # 上游内容变化（或消失）的 skill
skills-profiles invalidate --all                     # 全部清空（需显式 --all）
```

## 产物

```
output/                                      # 生成结果，可独立发布
├── skills.jsonl                             # skill 索引: id、上游内容 hash、聚合的 domain/persona
├── stats.json                               # 产物现状: 已完成/剩余/过期 skill 数、每个 prompt 的覆盖率
└── skills/<owner>/<repo>/<skill>/           # 目录名即 skills.jsonl 里的 id
    ├── domain.json                          # 每个 prompt 一个 json，生成即落盘（缓存标记）
    └── md/domain.md                         # 供浏览的 markdown 副本

cache/skills-sh/                             # 上游数据，与产物分离
├── skills.jsonl                             # 索引: 每个 skill 一行 json
└── skills/<owner>/<repo>/<skill>/SKILL.md   # 每个 skill 的源文件
```

内置 prompt: `domain`、`scenario`、`blackbox`、`whitebox`、`tagline`、`persona`、`comments`。

- `sync` 只下载数据，从不碰产物：整包 tarball 下载、只解压索引与 SKILL.md；
  最新 tag 记在 `cache/skills-sh/SNAPSHOT.json`，未变则跳过下载。
- 失效是显式操作：`invalidate --stale` 把记录 hash 与快照不一致（或已消失）的
  skill 全部失效（先 `sync` 保证快照最新）；`run` 只信任磁盘上现有的输出。
- 每次 `run` 结束打印计时汇总并覆盖 `stats.json`——它描述产物现状而非单次执行；
  `sync` 汇报对齐的 tag 与下载耗时。

## 持续生成（GitHub Actions）

`.github/workflows/generate.yml` 手动触发（Actions → generate → Run workflow）：

```
恢复 dist 分支 → sync → invalidate --stale → run --limit <输入，默认 10> → 发布到 dist
```

`dist` 分支既是发布产物也是缓存，根目录与 `output/` 一致。需在
Settings → Secrets and variables → Actions 配置：

| 位置 | 名称 | 示例 |
|---|---|---|
| Secret | `SKILLS_PROFILES_API_KEY` | 端点对应的 API key |
| Variable | `SKILLS_PROFILES_BASE_URL` | `https://api.b.ai/v1` |
| Variable | `SKILLS_PROFILES_MODEL` | `GLM-5.3-Flash` |

## 新增一个 prompt

`prompts/` 下一文件一 prompt，文件名即 prompt id；`_system.md` 是共享 system
prompt（提供 `{{ skill.name }}`、`{{ skill.description }}` 与完整 `{{ skill_md }}`），
因此各 prompt 文件只需描述任务本身：

```markdown
---
description: 一行说明
output: IntroText          # models.py 中注册的 pydantic schema
depends_on: [scenario]     # DAG 依赖; 根节点可省略
---

请为下面的 skill 写……
{{ deps.scenario.text }}   # deps 将 prompt id 映射到其解析后的输出对象
```

然后为所有 skill 生成（已缓存的复用，只补缺失；重算先 `invalidate`）：

```bash
skills-profiles run --prompts my_angle --limit 0
```

## 配置

优先级从高到低：`SKILLS_PROFILES_*` 环境变量 → 本地 `.env` → 内置默认值。

| 变量 | 默认值 | 说明 |
|---|---|---|
| `SKILLS_PROFILES_MODEL` | `gpt-4.1-mini` | 任意 OpenAI 兼容模型 |
| `SKILLS_PROFILES_BASE_URL` | 无 | OpenAI 兼容端点 |
| `SKILLS_PROFILES_API_KEY` | 无 | 端点 API key |
| `SKILLS_PROFILES_LIMIT` | `10` | 每次 run 生成的 skill 数（`0` = 全部；已缓存的跳过不计数） |
| `SKILLS_PROFILES_CONCURRENCY` | `2` | LLM 最大并发调用数（跨 skill 及 skill 内 prompt 共享；也可用 `--concurrency`） |
| `SKILLS_PROFILES_OUTPUT_DIR` | `output` | 产物目录 |
| `SKILLS_PROFILES_DATA_DIR` | `cache/skills-sh` | 上游数据目录 |
| `SKILLS_PROFILES_PROMPTS_DIR` | `prompts` | prompt markdown 目录（含 `_system.md`） |

想参与开发？看 [CONTRIBUTING.zh-CN.md](CONTRIBUTING.zh-CN.md)。
