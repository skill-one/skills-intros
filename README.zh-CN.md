# skills-intros

为 [skill-one/skills-sh-scraper](https://github.com/skill-one/skills-sh-scraper) 收录的
[agent skills](https://www.skills.sh) 批量生成多角度中文介绍词。

- 只想要产物？看[产物](#产物)。
- 想运行或新增 prompt？看[快速开始](#快速开始)。
- 想参与开发？看 [CONTRIBUTING.zh-CN.md](CONTRIBUTING.zh-CN.md)。

> English documentation: [README.md](README.md)

## 产物

每个 skill 在 `output/results/skills/` 下有一个独立目录：

```
output/results/
├── hashes.json                          # skill id -> 上游内容 hash (prune 索引)
└── skills/<owner>/<repo>/<skill>/
    ├── domain.json                      # 每个 prompt 一对 json+md
    ├── domain.md
    ├── one_liner.json
    ├── one_liner.md
    └── ...
```

- 目录名即 `skills.jsonl` 里的 `id`, 与上游 `data/skills/` 布局一致。
- 每个 prompt 的结构化输出存放在自己的 `<prompt_id>.json` 里(缓存的提交标记); 旁边的 `<prompt_id>.md` 用于浏览。
- 内置 prompt: `domain`、`one_liner`、`dev_intro`、`scenario_intro`、`blackbox`、`whitebox`、`comparison`、`trigger_guide`、`tagline`。

新鲜度: `hashes.json` 记录每个 skill 的输出是基于哪个上游内容 hash 生成的, 有效性判定发生在
`sync` 时——每次 sync 将该索引与刚下载的快照逐一对比, 上游 hash 变化(或 skill 已从上游消失)
的条目连同产物目录立即删除, 下次 `run` 重新生成; `run` 本身只信任磁盘上现有的输出文件。

## 快速开始

需要 Python 3.12+ 和 [uv](https://docs.astral.sh/uv/)。

```bash
uv sync
# LLM 凭据: 在本地 .env 中配置 KEY / BASE_URL / MODEL（参见 .env.example）
skills-intros sync            # 下载最新的 dist 分支快照（并清理失效产物）
skills-intros run --top 50    # 为安装量前 50 的 skill 生成介绍词
```

`run` 的更多选项:

```bash
skills-intros run --top 0             # 所有可用 skill
skills-intros run --force             # 无视已有结果强制重跑
skills-intros run --prompts tagline   # 只(重)生成一个 prompt
skills-intros run --top 5 --dry-run   # 用离线假 LLM 冒烟测试
skills-intros run --top 5 --debug     # 把最终发给 LLM 的 prompt 打印到 stderr
skills-intros run --verbose           # 开启 DEBUG 级别的执行日志
```

重跑天然支持断点续传: 每个 prompt 的输出一生成即落盘, 因此即使中途崩溃, 也只有缺失的
prompt 才会真正调用 LLM。拆分布局之前写入的结果(每个 skill 一个 `result.json`)会被忽略
并重新生成。

## 新增一个 prompt

`prompts/` 下一个 markdown 文件即一个 prompt, 文件名就是 prompt id。
共享的 `_system.md` 是 system prompt, 按 skill 逐次渲染: 它承载每个 prompt 都能看到的
skill 上下文——`{{ skill.name }}` 与 `{{ skill.description }}`(均取自 `skills.jsonl`)
和完整的 `{{ skill_md }}` 原文(每个 skill 目录下的 `SKILL.md` 文件)——因此各 prompt
文件只需描述任务本身。

```markdown
---
description: 一行说明
output: IntroText          # models.py 中注册的 pydantic schema
depends_on: [dev_intro]    # DAG 依赖; 根节点可省略
---

请为下面的 skill 写……
{{ deps.dev_intro.text }}   # deps 将 prompt id 映射到其解析后的输出对象
```

然后为所有 skill 生成（已缓存的 prompt 一律复用, 只生成缺失的——需要重算请加 `--force`）:

```bash
skills-intros run --prompts my_angle --top 0
```

## 配置

配置按优先级从高到低: `SKILLS_INTROS_*` 环境变量 → 本地 `.env` → 内置默认值。

| 变量                          | 默认值            | 说明                                         |
| --------------------------- | -------------- | ------------------------------------------ |
| `SKILLS_INTROS_MODEL`       | `gpt-4.1-mini` | 任意 OpenAI 兼容对话模型                           |
| `SKILLS_INTROS_BASE_URL`    | 无              | OpenAI 兼容端点覆盖                              |
| `SKILLS_INTROS_API_KEY`     | 无              | 端点对应的 API key                             |
| `SKILLS_INTROS_TOP_N`       | `50`           | 处理的 skill 数量（`0` = 全部）                     |
| `SKILLS_INTROS_CONCURRENCY` | `8`            | LLM 最大并发调用数                                |
| `SKILLS_INTROS_WORKDIR`     | `output`       | 存放 `data/` 与 `results/`                    |
| `SKILLS_INTROS_PROMPTS_DIR` | `prompts`      | prompt markdown 文件所在目录(含 `_system.md`)          |
