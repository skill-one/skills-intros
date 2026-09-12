# microsoft-foundry (`microsoft/azure-skills/microsoft-foundry`)

## whitebox

- 先跑依赖检查脚本 (check-and-setup-dependencies.sh/.ps1), 只补装缺失依赖, 完成前不进入任何子流程
- 按用户意图查"意图→工作流"映射表, 路由到对应子技能 (create/deploy/invoke/observe/trace…), 并必须先读完该子技能文档再动手
- 若涉及 Foundry MCP 操作, 先调用 Azure MCP 的 `foundry` 工具做发现, 列出可用工具与参数
- 解析项目上下文: 从 azure.yaml (azd agent 服务) 或 .foundry/agent-metadata.yaml 定位 agent root, 用 `azd env get-values` 取 endpoint/agent 名/版本等, 仍缺的值按优先级规则推导或向用户询问
- 严格按子技能文档逐步执行 (任何 azd 命令前必读 azd-guidance 并遵守 AZURE_DEV_USER_AGENT 规则), 最后汇报所选 agent root、环境及上下文来源

- 强制文档闸门: 每条触发不同工作流的新消息都要重新遵守"先读对应子技能文档再执行", 即使已知 MCP 工具参数也不跳过——前置检查和校验逻辑都写在文档里
- 上下文解析与归一化: 环境选择按"用户显式指定 > AZURE_ENV_NAME > azd 默认环境 > 会话已选"; metadata 同样有优先级链; 旧版 testSuites[]/testCases[] 在内存中归一化为 evaluationSuites[] 形状, legacy P0/P1/P2 优先级映射为 tags.tier 的 smoke/regression/coverage; azd 提供的值是 source of truth, 不重复写入 metadata 文件
- 外部依赖清单: 依赖检查脚本 (bash/pwsh); Foundry MCP 工具经 Azure MCP 暴露 (含 evaluator_catalog_get 校验 evaluator、prompt_optimize 做提示词优化); azd CLI (部署/环境), Azure CLI (资源/配额/RBAC); Application Insights (trace 用 customEvents 把评估结果关联到具体响应); 模型部署/微调均通过 Foundry 侧工作流完成, 不直接调用第三方模型 API
