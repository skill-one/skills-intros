# azure-diagnostics (`microsoft/azure-skills/azure-diagnostics`)

## whitebox

- 识别症状: 从用户描述提取服务类型与故障现象 (如 App Service 高 CPU、AKS pod CrashLoop、AMQP 连接失败)
- 先查资源健康: 调 Resource Health 确认 Azure 平台侧是否正常, 排除平台故障后再深入
- AI 诊断: 可用时调 AppLens MCP 自动检测问题, 输出根因分析与修复建议
- 查日志/指标: 通过 Azure Monitor MCP 用 KQL 查询日志与指标 (套用内置 KQL 查询库)
- 输出结论: 记录根因、证据与已尝试的修复步骤

- 关键词触发路由: skill.md 的 Triggers 列表 (如 'pod pending'、'image pull failures'、'message lock lost') 决定激活时机; 命中后按 Routing 规则分流 — Container Apps/App Service/Functions 留在本 skill 内处理, AKS/VM 连接/消息 SDK 转发到各自的专属排障文档
- MCP 工具链 (外部依赖): mcp_azure_mcp_resourcehealth (健康检查)、mcp_azure_mcp_applens (AI 根因诊断)、mcp_azure_mcp_monitor (logs_query + KQL); MCP 不可用时降级为 az CLI 命令 (az resource show、az monitor activity-log list、az containerapp logs show 等)
- 分层排障协议: 固定顺序 '症状 → 资源健康 → 日志 → 指标 → 近期变更', 强制先排除平台侧故障再查应用侧; 诊断时按服务类型加载 references/ 下对应的排障手册与 KQL 查询模板
