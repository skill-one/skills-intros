# dbs-report (`dontbesilent2025/dbskill/dbs-report`)

## whitebox

- 解析当前工作目录的 .dbs/config.json，确定存档根目录（默认 ~/.dbs/，或 project/custom 模式指定的目录）
- 列出 sessions/{项目名}/*.md，有 --since 先按日期过滤；少于 2 份存档则停止并提示，≥2 份继续
- 按文件名时间戳 YYYYMMDD-HHMMSS 排序读取全部存档，解析 frontmatter 字段 + body 六段（主诉/结论/否决/假设/下一步/备注）
- 合并去重分类，写入 reports/{项目名}/{时间戳}-{项目名}.md（目录不存在先 mkdir -p，永不覆盖旧报告）
- 回执：文件路径 + 合并的存档数量 + 时间跨度，结束

- 配置解析与 dbs-save 同一套规则：mode=default→~/.dbs/、project→工作目录 .dbs/、custom→root 指定路径；配置无法解析或路径非法时停止生成，不静默回退默认位置
- 解析与合并规则：按时间戳排序；字段缺失不中断、用现有内容续写；结论语义去重、新的在前，被修正的旧结论保留并加标注；未解决问题 = in-progress 假设 + 早期提出但从未被后续处理的方向；报告内容必须逐条可追溯到存档字段，禁止凭对话发挥
- 输出与依赖：每次生成带时间戳的新文件、永不覆盖；纯本地文件读写 + Markdown 拼装，无外部库、无模型 API 依赖
