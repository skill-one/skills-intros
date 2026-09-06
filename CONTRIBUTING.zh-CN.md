# 贡献指南 / 开发者文档

与开发 `skills-intros` 本身相关的一切。面向使用者的文档在
[README.zh-CN.md](README.zh-CN.md)。

> English documentation: [CONTRIBUTING.md](CONTRIBUTING.md)

## 工作原理

```
skills.jsonl (dist 分支) ──► 按安装量取 Top N ──► 每 skill 执行 prompt DAG
                                                ──► output/results/skills/<id>/result.json
                                                ──► output/results/skills/<id>/<prompt>.md
```

Prompt DAG（边表示"依赖其输出"）:

```
domain ──┬── dev_intro ──┐
         ├── scenario_intro ──┼── comparison
         │                    └── trigger_guide
one_liner ── tagline
```

关键设计决策:

- **不引入编排框架。** DAG 排序使用 Python 标准库
  [`graphlib.TopologicalSorter`](https://docs.python.org/3/library/graphlib.html)。
- **结构化输出。** 每个 prompt 在 frontmatter 的 `output:` 中声明一个 pydantic schema;
  LLM 调用通过 [instructor](https://python.useinstructor.com/) 走 OpenAI 兼容客户端。
- **基于文件的断点续跑。** 每个 skill 的 `result.json` 既是产物也是缓存: 存在即短路跳过
  LLM。失效清理在 `sync` 时完成（上游 hash 变化或 skill 消失即删除）, `run` 不再做 hash
  比对。续跑粒度是 prompt 级——只重新生成缺失或未通过当前 schema 校验的输出。
- **Prompt 即文件。** 每个 prompt 是 `prompts/` 下的一个 markdown 文件（可用
  `SKILLS_INTROS_PROMPTS_DIR` 覆盖）。YAML frontmatter 存元数据, 正文是 jinja2 用户提示词
  模板; `_system.md` 是共享的 system prompt。新增 prompt 通常无需改代码, 除非需要新的输出
  schema（那就在 `models.py` 注册）。

## 局部重跑的实现

`run --prompts <id>` 会先计算目标 prompt 的依赖闭包。目标 prompt 总是重跑; 其依赖复用
`result.json` 里已存的输出（缺失或传 `--force` 时才重新生成）; 闭包之外的 prompt 原样
保留——因此每次运行后 `result.json` 始终完整。

## 项目结构

```
prompts/               # 每个 prompt 一个 md 文件（+ _system.md）
├── _system.md
├── domain.md
├── one_liner.md
├── scenario_intro.md
├── dev_intro.md
├── comparison.md
├── trigger_guide.md
└── tagline.md

src/skills_intros/
├── config.py        # 配置（pydantic-settings）
├── data.py          # dist 分支 tar 包下载 + skills.jsonl 解析
├── models.py        # 领域分类体系 + 结构化输出 schema
├── prompts.py       # frontmatter 加载 + DAG 排序 + jinja2 渲染
├── llm.py           # instructor/openai client + 离线 FakeLLM
├── generate.py      # 异步 DAG 执行 + 文件断点续跑
├── outputs.py       # 每 skill 的 markdown 渲染
└── cli.py           # typer 命令（sync / run）
```

## 配置解析

`SKILLS_INTROS_*` 环境变量 → 本地 `.env` → 内置默认值。由 `config.py` 中的
`pydantic-settings` 实现。

## 测试

整条管道均可离线验证: 数据解析、DAG 排序、模板渲染、续跑跳过/强制、依赖传递、
markdown 渲染, 以及完整的 CLI dry-run——全部不需要网络（`llm.py` 提供 `FakeLLM`）。

```bash
uv run pytest
```

文档规范: 每份英文文档都要有对应的中文版（如 `README.md` / `README.zh-CN.md`、
`CONTRIBUTING.md` / `CONTRIBUTING.zh-CN.md`）, 两者需保持同步。
