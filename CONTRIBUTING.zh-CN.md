# 贡献指南 / 开发者文档

与开发 `skills-intros` 本身相关的一切。面向使用者的文档在
[README.zh-CN.md](README.zh-CN.md)。

> English documentation: [CONTRIBUTING.md](CONTRIBUTING.md)

## 工作原理

```
skills.jsonl (dist 分支) ──► 按安装量取 Top N ──► 每 skill 执行 prompt DAG
                                                ──► output/results/skills/<id>/<prompt>.json
                                                ──► output/results/skills/<id>/md/<prompt>.md
```

Prompt DAG（边表示"依赖其输出"）:

```
scenario_intro ──┬── comparison
                 └── trigger_guide
```

关键设计决策:

- **不引入编排框架。** DAG 排序使用 Python 标准库
  [`graphlib.TopologicalSorter`](https://docs.python.org/3/library/graphlib.html)。
- **结构化输出。** 每个 prompt 在 frontmatter 的 `output:` 中声明一个 pydantic schema;
  LLM 调用通过 [instructor](https://python.useinstructor.com/) 走 OpenAI 兼容客户端。
- **基于文件的断点续跑。** 每个 prompt 的输出是自己的 `<prompt_id>.json` (另有 markdown 副本
  放在 `md/` 下), 生成后立即提交——既是产物也是缓存: 存在且通过 schema 校验即不调用 LLM。`results/hashes.json`
  (skill id -> 上游 hash, 仅在本次 run 真正生成内容时写入) 是 `sync` 的清理索引(上游 hash
  变化或 skill 消失即删除), `run` 不再做 hash 比对。续跑粒度是 prompt 级, 中途崩溃已完成
  的 prompt 全部保留。
- **Prompt 即文件。** 每个 prompt 是 `prompts/` 下的一个 markdown 文件（可用
  `SKILLS_INTROS_PROMPTS_DIR` 覆盖）。YAML frontmatter 存元数据, 正文是 jinja2 用户提示词
  模板; `_system.md` 是共享的 system prompt。新增 prompt 通常无需改代码, 除非需要新的输出
  schema（那就在 `models.py` 注册）。

## 局部重跑的实现

`run --prompts <id>` 会先计算目标 prompt 的依赖闭包, 只生成闭包里缺失的部分。依赖属于输入,
因此复用各自的 `<prompt_id>.json`, 仅在缺失或 schema 校验失败时重新生成。闭包之外的 prompt
完全不动——因此选择之外的输出绝不会意外重算。

重算从来不是 `run` 的参数: `invalidate` 删掉缓存的 json(以及它的 `md/` 副本), `run` 再把
缺口补上。某 skill 若一个输出都不剩, 会从 `results/hashes.json` 中除名, 即重新视为全新 skill。
`sync` 对上游 hash 变化的 skill 调用的也是同一个 `invalidate`, 手动与自动失效是同一条代码路径。

## 项目结构

```
prompts/               # 每个 prompt 一个 md 文件（+ _system.md）
├── _system.md
├── domain.md
├── scenario_intro.md
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
├── outputs.py       # 每 prompt 的 json 输出 + md/ 渲染 + 缓存失效
└── cli.py           # typer 命令（sync / invalidate / run）
└── logging.py       # --verbose 日志配置
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
