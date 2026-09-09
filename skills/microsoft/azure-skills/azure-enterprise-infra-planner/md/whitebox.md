# azure-enterprise-infra-planner (`microsoft/azure-skills/azure-enterprise-infra-planner`)

## whitebox

- 分诊输入：纯新需求走 greenfield 主干；若引用了已有资源/IaC/文档，则先盘点存量并全程"引用不重建" (referenced-workload.md)
- Phase 1~4：提取环境洞察 → 检索最佳实践 → 检索资源约束 → 生成基础设施计划 (.azure/infrastructure-plan.json，状态 draft)
- Phase 5 门禁：计划必须经用户明确批准，未批准则打回 Phase 4 修改
- Phase 6 硬门禁：生成 IaC 后本地校验 (az bicep build / terraform validate 零错误) + checkov 扫描 (无未解决高危)，展示命令输出并自检后才放行
- Phase 7：用户风险确认后部署——greenfield 用 az deployment / terraform apply；referenced 只做增量部署 (what-if 预览，不改动/不销毁已引用资源)

- 门控流水线：7 个阶段逐一过闸，每阶段产出落盘为状态文件 (.azure/insights.json、.azure/infrastructure-plan.json，status 沿 draft→approved→deployed 流转)，最终交付 infra/main.bicep+modules 或 infra/main.tf+modules；出错即停在该闸口 (未批准/校验失败/部署缺确认均不前进)
- 研究靠 MCP 工具链：insights_get (用户现有 Azure 环境)、get_azure_bestpractices_get、wellarchitectedframework_serviceguide_get (WAF 对齐)、microsoft_docs_search/fetch (微软文档)、bicepschema_get (Bicep 最新 API 版资源 schema)；MCP 失败重试一次，仍失败则回退到本地参考文件并告知用户
- 外部 CLI 做校验与执行：Azure CLI (az bicep build、az deployment group create)、Terraform CLI (validate/plan/apply)、checkov (IaC 安全扫描)——校验结果必须展示原始命令输出，构成 Phase 6 的自证门禁
