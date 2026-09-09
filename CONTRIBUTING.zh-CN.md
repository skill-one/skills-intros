# 贡献指南 / 开发者文档

与开发 `skills-intros` 本身相关的一切。面向使用者的文档在
[README.zh-CN.md](README.zh-CN.md)。

> English documentation: [CONTRIBUTING.md](CONTRIBUTING.md)

## 工作原理

```
dist 分支 tarball ──► cache/skills-sh (skills.jsonl + skills/<id>/SKILL.md)
                             │
                             └─► 按安装量取 --limit 个仍有缺失的 ──► 每 skill 执行 prompt DAG
                                                    ──► output/skills/<id>/<prompt>.json
                                                    ──► output/skills/<id>/md/<prompt>.md
                                                    ──► output/hashes.json
```

`output/`(生成的介绍)与 `cache/skills-sh`(上游 skills 基本信息)是两个独立根目录——参见
[配置解析](#配置解析): 从上游取到的东西永远不会写进产物目录。

Prompt DAG（边表示"依赖其输出"）:

```
domain   scenario   blackbox   whitebox   tagline   persona   comments
# 当前无依赖边: 每个内置 prompt 都是根节点
# 在 frontmatter 里加 `depends_on: [scenario]` 即可串联
```

关键设计决策:

- **不引入编排框架。** DAG 排序使用 Python 标准库
  [`graphlib.TopologicalSorter`](https://docs.python.org/3/library/graphlib.html)。
- **结构化输出。** 每个 prompt 在 frontmatter 的 `output:` 中声明一个 pydantic schema;
  LLM 调用通过 [instructor](https://python.useinstructor.com/) 走 OpenAI 兼容客户端。
- **基于文件的断点续跑。** 每个 prompt 的输出是自己的 `<prompt_id>.json` (另有 markdown 副本
  放在 `md/` 下), 生成后立即提交——既是产物也是缓存: 存在且通过 schema 校验即不调用 LLM。`hashes.json`
  (skill id -> 上游内容 hash, 仅在本次 run 真正生成内容时写入) 是 `sync` 的清理依据(上游 hash
  变化或 skill 消失即删除), `run` 不再做 hash 比对。续跑粒度是 prompt 级, 中途崩溃已完成
  的 prompt 全部保留。
- **一次请求拿整个快照。** `sync` 把 dist 分支作为一个 tarball 整体下载(codeload)并完整解压到
  `cache/skills-sh`, 整包替换上一次的快照——没有逐文件下载, 也不需要额外的缓存失效逻辑;
  之后 `read_skill_md` 直接读本地文件。
- **Prompt 即文件。** 每个 prompt 是 `prompts/` 下的一个 markdown 文件（可用
  `SKILLS_INTROS_PROMPTS_DIR` 覆盖）。YAML frontmatter 存元数据, 正文是 jinja2 用户提示词
  模板; `_system.md` 是共享的 system prompt。新增 prompt 通常无需改代码, 除非需要新的输出
  schema（那就在 `models.py` 注册）。

## 局部重跑的实现

`run --prompts <id>` 会先计算目标 prompt 的依赖闭包, 只生成闭包里缺失的部分。依赖属于输入,
因此复用各自的 `<prompt_id>.json`, 仅在缺失或 schema 校验失败时重新生成。闭包之外的 prompt
完全不动——因此选择之外的输出绝不会意外重算。

重算从来不是 `run` 的参数: `invalidate` 删掉缓存的 json(以及它的 `md/` 副本), `run` 再把
缺口补上。某 skill 若一个输出都不剩, 会从 `hashes.json` 中除名, 即重新视为全新 skill。
`sync` 对上游 hash 变化的 skill 调用的也是同一个 `invalidate`, 手动与自动失效是同一条代码路径。

## 项目结构

```
prompts/               # 每个 prompt 一个 md 文件（+ _system.md）
├── _system.md
├── domain.md
├── scenario.md
├── blackbox.md
├── whitebox.md
├── tagline.md
├── persona.md
└── comments.md

src/skills_intros/
├── config.py        # 配置（pydantic-settings）
├── data.py          # dist 分支 tarball 下载 + skills.jsonl 解析 + SKILL.md 读取
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
markdown 渲染, 以及完整的 CLI dry-run——全部不需要网络（`llm.py` 提供 `FakeLLM`;
`conftest.py` 会把 `data._download` 换成本地假服务, 返回由 fixture 构造的快照 tarball）。

```bash
uv run pytest
```

文档规范: 每份英文文档都要有对应的中文版（如 `README.md` / `README.zh-CN.md`、
`CONTRIBUTING.md` / `CONTRIBUTING.zh-CN.md`）, 两者需保持同步。
