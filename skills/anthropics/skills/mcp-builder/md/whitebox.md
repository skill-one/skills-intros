# mcp-builder (`anthropics/skills/mcp-builder`)

## whitebox

- 调研: 用 WebFetch 拉取 MCP 协议文档 (先取 sitemap 再抓 .md 页面) 和所选 SDK 的 README, 同时查目标服务的 API 文档, 规划要实现的工具清单 (优先覆盖全部 API 端点)
- 实现: 按语言指南搭项目结构 (推荐 TypeScript, 远程用 Streamable HTTP 无状态 JSON, 本地用 stdio), 写共享基础设施 (带鉴权的 API client、错误处理、响应格式化、分页), 再逐个注册工具
- 审查测试: 检查代码质量 (无重复、类型全覆盖、描述清晰), 编译验证 (npm run build / python -m py_compile), 用 MCP Inspector 实测
- 产出评估: 加载评估指南, 生成 10 个复杂、只读、可字符串比对的问答对, 每题自己先解一遍验证答案, 输出 XML 评估文件

- 文档驱动: 外部依赖为 WebFetch (抓取 modelcontextprotocol.io 规范页和 GitHub 上的 TypeScript/Python SDK README)、参考文件库 (mcp_best_practices.md 及语言实现指南), 先加载知识再动手
- 工具定义三件套: 输入用 Zod (TS) / Pydantic (Python) 声明带约束和示例的 schema; 输出尽量定义 outputSchema 并用 structuredContent 返回结构化数据; 附注解提示 (readOnlyHint / destructiveHint / idempotentHint / openWorldHint)
- 校验闭环: 静态验证靠编译器 (tsc 构建 / py_compile), 动态验证靠 npx @modelcontextprotocol/inspector; 评估阶段要求问答答案可验证 (字符串比对) 且稳定 (不随时间变化)
