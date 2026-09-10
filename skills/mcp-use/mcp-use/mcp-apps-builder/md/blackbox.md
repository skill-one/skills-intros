# mcp-apps-builder (`mcp-use/mcp-use/mcp-apps-builder`)

## blackbox

**function**: 帮你从零搭建、修复或升级「MCP 服务器 / MCP 应用」(一种让 AI 助手能连接外部工具和数据的小型服务), 你给出想法或现有代码, 我交付能直接跑起来的项目。

- input: 一句话需求, 如「做一个让 AI 查询 GitHub PR 状态的 MCP 服务器」, output: 一个完整可运行的项目文件夹: 服务端代码 + 配置文件 + 启动说明, 接上 AI 助手即可用
- input: 一个报错的 MCP 项目路径 + 报错信息, output: 修好的代码, 附错误原因说明和「已验证能正常跑」的结果
- input: 旧版本写的 MCP 项目代码, output: 升级到新版后能正常运行的代码, 附一份改动清单
- input: 指令「帮我审查这个 MCP 服务器的安全性和代码质量」, output: 一份审查报告: 列出具体问题 (如权限漏洞、结果格式错误) 和对应的修改建议
