# appinsights-instrumentation (`microsoft/azure-skills/appinsights-instrumentation`)

## whitebox

- 采集上下文: 读工作区源码, 推断 (编程语言, 应用框架, 托管方式) 三元组; 托管位置必须主动向用户确认
- 意图分流: 用户要 "给应用加上 App Insights/改代码" → 转交 azure-prepare 编排器; 要 "怎么接入/概念讲解" → 留在本 skill 继续
- 优先自动埋点: 若是托管在 Azure App Service 的 ASP.NET Core 应用 → 走 references/auto.md 的自动埋点指南
- 否则手动接入: 先创建 App Insights 资源 (套用 examples/appinsights.bicep 或 scripts/appinsights.ps1 里的 Azure CLI 命令), 再按语言指南 (aspnetcore.md / nodejs.md / python.md) 修改应用代码
- 收尾建议: 把 App Insights 资源建在与托管应用相同、便于管理的资源组里

- 纯参考型 skill, 自身不改代码: 通过 "how(问方法) vs add(要改动)" 的意图判断路由请求, 实际组件改动由 azure-prepare 负责编排
- 分层文档检索: 按 (语言, 框架, 托管) 匹配 references/ 下的平台指南 (auto / aspnetcore / nodejs / python / container-apps) 与 OpenTelemetry SDK 速查表; 资源创建匹配 examples/appinsights.bicep 或 scripts/appinsights.ps1
- 外部依赖: Azure Application Insights / Azure Monitor 服务, Azure Monitor OpenTelemetry Distro (Python/TypeScript) 与 Exporter (Python/Java), Azure CLI, Bicep 模板
