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
output/results/skills/<owner>/<repo>/<skill>/
├── result.json        # 机器可读的完整记录
├── domain.md          # 每个 prompt 一个 markdown, 方便浏览
├── one_liner.md
├── dev_intro.md
├── scenario_intro.md
├── comparison.md
├── trigger_guide.md
└── tagline.md
```

- 目录名即 `skills.jsonl` 里的 `id`, 与上游 `data/skills/` 布局一致。
- `result.json` 的结构是 `{"skill": <上游记录, 含内容 hash>, "intros": {<prompt_id>: <结构化输出>}}`——它是唯一的事实来源。
- 内置 prompt: `domain`、`one_liner`、`dev_intro`、`scenario_intro`、`comparison`、`trigger_guide`、`tagline`。

新鲜度: `result.json` 中保存上游内容 hash 仅供审计, 有效性判定发生在 `sync` 时——每次
sync 将磁盘上的结果与刚下载的快照逐一对比, 上游 hash 变化(或 skill 已从上游消失)的产物
立即删除, 下次 `run` 重新生成; `run` 本身只信任磁盘上现有的 `result.json`。

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

重跑天然支持断点续传: 只有缺少 `result.json` 的 skill 才会真正调用 LLM。

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
