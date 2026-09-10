# entra-agent-id (`microsoft/azure-skills/entra-agent-id`)

## whitebox

- 判定任务是否落在技能范围内 (Agent Identity Blueprint / fmi_path 令牌交换 / agent OBO / SDK sidecar), 范围外的 (如普通应用注册) 不接
- 先用 mcp_azure_mcp_documentation 检索 Microsoft Learn, 核对当前 Graph 端点与请求体的最新形态
- 建立凭证: PowerShell Connect-MgGraph 带显式 Agent Identity 委派权限, 或 Python ClientSecretCredential 换 Graph bearer token (Azure CLI / DefaultAzureCredential 被 API 硬拒, 直接排除)
- 按核心工作流依次调用类型化端点: 建 Blueprint → 显式补建 BlueprintPrincipal (不会自动生成) → 逐个建 Agent Identity
- 收尾配置: 凭证挂在 Blueprint 上, 执行两步 fmi_path 交换, 按单个 Agent Identity 授予 appRoleAssignments / oauth2PermissionGrants

- 文档核验先行: 所有请求体/端点先经 mcp_azure_mcp_documentation (Microsoft Learn 检索) 对照再执行, 因为 Graph API 形态会演进; 技能本身无专用 MCP server, 靠直连 Microsoft Graph v1.0 REST (PowerShell 模块或 Python requests) 发请求
- 结构化调用模型: 强制类型化端点 (如 /applications/microsoft.graph.agentIdentityBlueprint) + 每个请求带 OData-Version: 4.0 头, 遵循 Blueprint → BlueprintPrincipal → Agent Identity 三层对象模型; 脚本写成幂等 — 即使 Blueprint 已存在也要检查 BlueprintPrincipal
- 纠错表驱动: 常见错误码直接映射修复动作 (AADSTS82001 → 改用 fmi_path 而非 RFC 8693; AADSTS700211 → 步骤一须指向 Agent Identity 的 home tenant); fmi_path 交换、OBO、sidecar 等深水区按需加载 references/*.md — 依赖: Microsoft.Graph.Applications (PowerShell), azure-identity + requests (Python), Microsoft.Identity.Web.AgentIdentities (.NET 快捷路径), Microsoft Entra SDK for AgentID (多语言 sidecar 容器)
