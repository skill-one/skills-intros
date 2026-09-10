# azure-reliability (`microsoft/azure-skills/azure-reliability`)

## whitebox

- 圈定范围: 向用户确认资源组/订阅/应用名, 用 Azure Resource Graph (az graph query + 范围过滤) 发现资源并按服务类型分类, 仅对 Functions / App Service 深入, 未支持服务 (如 Container Apps) 标 ⚪ 跳过
- 两层评估: 先跑平台级检查 (计算区冗余、存储冗余 SKU、健康探测、多区域/负载均衡), 再按资源类型加载对应 per-service reference 文件核对计划/SKU 规则
- 输出 feature-pivoted 评估表: 固定 4 行可靠性特性 (计算区冗余 / ZRS 存储 / 健康探测 / 多区域故障转移), 每行一个 🟢/🟡/🔴 状态 + 相关资源, 结尾只问一个 yes/no 问题
- 用户确认后分阶段修复: 先做快速项 (计算计划区冗余、健康探测), 路径二选一 — A) 直接对线上跑 az CLI, 或 B) 给 Bicep/Terraform 打补丁并由 skill 自己执行部署 (azd up / az deployment group create / terraform apply)
- 每阶段完成后自动重跑评估, 展示同款表并标注每项的变化 (如 🔴 OFF → 🟢 ON)

- 查询层: 依赖 Azure CLI + resource-graph 扩展 (az graph query) 做资源发现; Azure MCP 工具辅助 (mcp_azure_mcp_extension_cli_generate 生成 az 命令, subscription_list / group_list 列范围); 前提是用户已 az login, 评估需 Reader、改配置需 Contributor 权限
- 参考文件分发: 每个服务的计划/SKU 规则、评估查询、CLI 命令、IaC 补丁 (Bicep / Terraform / AVM) 全部来自对应 reference 文件, 作为单一事实来源; 未支持的服务只出现在汇总表里标 ⚪ not assessed, 绝不臆造命令或补丁
- 风险分级 + 双部署 + 同意门: 所有改动前必须停下向用户确认; 补丁按风险分级 (🟢 安全 / 🟡 需预迁移 / ⚪ 仅代码); 存储 LRS→ZRS 不能和安全补丁一起部署 — 必须先跑 az storage account migration start (耗时数小时~天) 完成, 再补 IaC SKU 做第二次部署; FC1/Consumption 的健康检查路径是代码改动, 动源码前必须获用户明确同意
