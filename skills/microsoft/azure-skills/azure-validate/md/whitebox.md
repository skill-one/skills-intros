# azure-validate (`microsoft/azure-skills/azure-validate`)

## whitebox

- 前置检查: 确认 azure-prepare 已跑完——`.azure/deployment-plan.md` 存在且状态为 `Approved` 或之后, 否则立即停止并先调用 azure-prepare
- 首次运行工作流脚本 (workflow.ps1 / workflow.sh), 不带 completed-step 参数, 脚本打印下一个待执行动作和需回传的值
- 按脚本指示执行该动作, 再带 `-CompletedStep <value>` (pwsh) / `--completed-step <value>` (bash) 重跑脚本, 循环直到脚本报告 azure-validate 完成
- 每步细节按需查阅 references/recipes/README.md (检查配方) 与 references/role-verification.md (RBAC 角色验证)
- 全部通过后记录证据、把计划状态置为 `Validated` 并汇报结果; 若用户明确要求部署, 转调 azure-deploy, 否则就此停止

- 脚本驱动状态机: 核心是工作流脚本 references/scripts/workflow.ps1 (Windows, 需 pwsh) 与 workflow.sh (macOS/Linux); 每次运行输出下一步动作和回传值, agent 据此循环调用, 脚本是唯一推进器
- 状态持久化 + 验证权威: 进度实时记录在 `.azure/validate-status.json`; 只有走完脚本全程才允许把计划状态设为 `Validated`, 严禁跳过脚本直接标 Validated
- 校验范围与安全闸: 检查 azure.yaml、Bicep/Terraform 基础设施、RBAC 角色分配、托管标识权限、部署前置条件; 破坏性操作必须先 ask_user (询问用户) 征得同意; 本技能不执行部署 (不跑 azd up/deploy), 部署一律委托给 azure-deploy
