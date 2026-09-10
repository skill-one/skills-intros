# azure-cost (`microsoft/azure-skills/azure-cost`)

## whitebox

- 解析用户意图, 按路由表分流到三条工作流之一: 查当前成本 / 降本优化 / 花费预测 (部署、诊断、安全审计等明确排除)
- 确定查询范围 scope: 按用户资源层级匹配订阅 / 资源组 / 管理组 / 计费账户四种模式
- 调用 Azure Cost Management REST API: 查历史成本用 query 接口, 预测未来用 forecast 接口 (POST {scope}/providers/Microsoft.CostManagement/...?api-version=2023-11-01)
- 优化场景下结合服务专属指南 (Redis / Storage) 定位浪费点 (如孤儿资源、VM 规格过大) 并给出缩减建议
- 汇总结果返回给用户

- 意图路由: 关键词匹配表 ('Azure costs'/'cost spike'/'forecast spending' 等触发词) 决定走哪条工作流, 附带反向排除条款避免误接管部署/安全类任务
- API 直调: 依赖 Azure Cost Management 官方 REST API (query + forecast, api-version 2023-11-01), 前提是目标 scope 上已授予 Cost Management Reader + Monitoring Reader + Reader 三个角色, 无权限即失败
- 范围与知识复用: scope 按 URL 模式拼装 (如 /subscriptions/<id>); 优化建议复用内置服务参考文档 (Redis / Storage) 及 MCP 工具与最佳实践参考
