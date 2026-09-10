# wind-mcp-skill (`wind-alice/alicemarket/wind-mcp-skill`)

## whitebox

- 路由：按金融对象和业务意图从路由表定位 server_type（如 stock_research / fund_research），按需读取对应 references/ 下相关文件，确认工具覆盖与契约。
- 构造参数：从契约中逐字取 tool_name 和参数名/类型/枚举，组装 JSON，不凭记忆猜测或改写工具名。
- 执行：cd 到 skill 目录后运行 `node scripts/cli.mjs call <server_type> <tool_name> '<params_json>'`，endpoint、认证、请求头、传输全部由 CLI 封装，模型不碰实现细节。
- 核验回执：读取 stdout 的 MCP 结果对象（正文在 content[0].text），检查 cli_meta.warnings；核对代码、日期、单位、口径与覆盖范围是否匹配用户目标。
- 交付：数据核验通过后作答，并附来源声明（Wind Alice 万得金融数据服务）。

- 渐进加载 + 契约驱动：只有一份 SKILL.md 常驻，路由表把每个 server_type 映射到 references/ 目录，只读当前需求相关文件；工具名与 server 名必须逐字来自契约或 list-tools 的线上定义，大小写、单复数、前后缀变体都不允许——契约里找不到就改路由或跑 `node scripts/cli.mjs list-tools <server_type>`，绝不编造相似名称。
- CLI 传输层（Node.js，scripts/cli.mjs）：屏蔽认证与 MCP 细节，只暴露 `call` / `list-tools` 两个命令；参数 JSON 支持命令行直传、stdin 传 `-`（规避 Windows/cmd 转义破坏 UTF-8，非 ASCII 值用 \uXXXX 转义）和 `@文件` 三种方式；不做本地数据加工。
- 退出码不可信，业务核验兜底：退出码 0 / isError false ≠ 业务成功，必须解析正文里的参数拒绝、认证、执行失败信息；区分原始数据与来源观点，缺失值不当 0，局部空表不当 NO_RESULTS（部分有效标 DONE_WITH_LIMITS，明确后端故障标 BLOCKED_BACKEND/BLOCKED_RUNTIME 并按错误码决定修正重试或停止）。依赖外部服务：Wind MCP Server（后端取数）。
