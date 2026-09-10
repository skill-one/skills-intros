# dbs-save (`dontbesilent2025/dbskill/dbs-save`)

## whitebox

- 校验可存内容：对话里没有诊断结论时拒绝写入，不存空文件
- 确定标题：用户指定则直接用，否则从对话提取 ≤20 字的名词短语
- 解析存档根目录并拼路径：读 cwd 下 `.dbs/config.json`（无配置则默认 `~/.dbs/`），生成 `{root}/sessions/{slug}/{YYYYMMDD-HHMMSS}-{title-slug}.md`，目录不存在则 `mkdir -p`
- 写入存档文件：固定格式的 YAML frontmatter（slug/timestamp/title/source_skill/status/next_skill）+ 6 段结构的 markdown 正文
- 输出一行回执：文件路径 + 当前项目下存档总数 + 下次 `/dbs-restore` 接续的提示

- 存档根目录解析与校验：读取 cwd 下 `.dbs/config.json` 的 `mode` 字段（default→`~/.dbs/`；project→cwd 下 `.dbs/`；custom→`root` 字段，展开开头 `~`，相对路径按 cwd 解析）。配置无法解析、mode 非法、root 为空或指向 `/`、家目录、项目根目录时，中止操作并报告配置问题，绝不静默回退默认位置；配置文件只在用户显式执行 `location` 子命令时写入，写入前必须展示解析结果并获用户确认
- 路径与命名规则：项目名（slug）默认取 `basename $(pwd)` 并把所有非 `[a-z0-9-]` 字符替换为 `-`，可用 `--slug` 参数覆盖；title-slug 把空格和标点替换为 `-`、保留中英文字符；同一秒出现同名文件时追加 4 位随机后缀（如 `-a7k2`）防冲突
- 时间戳生成：要求 ISO 8601 带时区格式（如 `2026-05-01T14:23:15+08:00`），通过 shell 调用本机 `python3` 的 `datetime.now().astimezone().isoformat(timespec='seconds')` 生成；文件名中的时间戳（YYYYMMDD-HHMMSS）用本地时间
