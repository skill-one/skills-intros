# azure-messaging (`microsoft/azure-skills/azure-messaging`)

## whitebox

- 从用户 prompt 识别 SDK (Event Hubs / Service Bus) 及版本; 无线索则先诊断、后补问
- 调用 mcp_azure_mcp_resourcehealth 检查命名空间资源健康, 排除平台侧故障
- 拿报错去匹配对应语言的 troubleshooting 指南 (位于 azure-diagnostics skill 的 troubleshooting/messaging/ 目录)
- 调用 mcp_azure_mcp_documentation 搜索 Microsoft Learn, 同时核对连接字符串、实体名、consumer group 等配置
- 给出修复方案, 并引用检索到的官方文档作依据

- 错误对号入座: 报错映射到分类排障指南, 覆盖连接失败/认证错误/AMQP link detach、消息锁与会话锁丢失或过期、空闲超时与慢重连、重复事件与 checkpoint offset 重置、批处理与 receive 行为, 并按语言 (Python/Java/JS/.NET) 区分
- MCP 工具链实证: mcp_azure_mcp_eventhubs / mcp_azure_mcp_servicebus 列举命名空间、队列、主题等资源; mcp_azure_mcp_monitor 的 logs_query 用 KQL 查诊断日志; mcp_azure_mcp_documentation 搜官方文档
- 证据闭环 + 配置校验: 每条修复建议须引用检索到的文档; 配置类问题核对连接字符串、实体名、consumer group 及 SDK 参数 (retry、prefetch、batch size、receive batch)
