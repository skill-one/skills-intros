# mcp-integration (`anthropics/claude-code/mcp-integration`)

## whitebox

- 解析配置: 读取插件根目录的 .mcp.json (推荐) 或 plugin.json 内嵌的 mcpServers 字段, 校验 JSON 语法与必填字段
- 展开变量: 将 ${CLAUDE_PLUGIN_ROOT} 替换为插件实际目录, 从用户 shell 读取 ${API_KEY} 等环境变量
- 建立连接: stdio 类型由 Claude Code 拉起本地子进程 (stdin/stdout 通信), SSE/HTTP/ws 类型直接连接远程 URL; 连接懒加载, 首次用工具时才触发
- 注册工具: 自动发现服务器提供的工具, 统一命名为 mcp__plugin_<插件名>_<服务名>__<工具名>
- 执行调用: 命令/子代理经 frontmatter 中 allowed-tools 白名单放行后调用工具, 结果返回用户 (hosted 服务的 OAuth 在首次使用时浏览器完成)

- 双配置入口 + 变量展开: .mcp.json 独立文件或 plugin.json 内嵌两种方式; ${CLAUDE_PLUGIN_ROOT} 保证路径可移植, 密钥只经环境变量注入, 不硬编码不进 git
- 四种传输适配: stdio (执行外部命令如 npx @modelcontextprotocol/server-filesystem、python -m <server> 作为子进程, Claude Code 管理生灭, 退出即终止) / SSE (托管服务, OAuth 自动处理) / HTTP (REST + Authorization header) / ws (实时双向流)
- 命名与授权控制: 工具自动加 mcp__plugin_... 前缀; allowed-tools 只放行显式工具名, 禁用通配符 *; 用 /mcp 命令验证注册结果, claude --debug 排查连接与认证问题
