# azure-rbac (`microsoft/azure-skills/azure-rbac`)

## whitebox

- 解析用户意图: 要给哪个身份 (identity) 授予哪些权限
- 调用 azure__documentation 工具查 Azure 文档, 匹配满足这些权限的最小内置角色 (least privilege)
- 若无内置角色匹配, 调用 azure__extension_cli_generate 生成自定义角色定义 (custom role definition)
- 调用 azure__extension_cli_generate 生成把该角色分配给身份的 CLI 命令
- 调用 azure__bicepschema 与 azure__get_azure_bestpractices, 输出角色分配的 Bicep 代码片段

- 最小权限优先: 先靠 azure__documentation 匹配内置角色, 匹配不上才降级用 azure__extension_cli_generate 造自定义角色, 避免过度授权
- 双产物输出: CLI 分配命令由 azure__extension_cli_generate 生成; Bicep 片段由 azure__bicepschema (schema 参考) + azure__get_azure_bestpractices (最佳实践) 保障合规
- 内置前置知识兜底: 用户问『授予角色需要什么权限』时不查文档, 直接回答 — 需含 Microsoft.Authorization/roleAssignments/write 的角色 (User Access Administrator 最小权限推荐 / Owner / 含该权限的自定义角色)
