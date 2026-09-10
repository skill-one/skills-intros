# caveman-manage (`juliusbrussee/caveman/caveman-manage`)

## whitebox

- 用 MCP 读数据: caveman_context 拿项目上下文, caveman_experiment_get 拉实验详情与结果; 用户未给 id 则先 list (备选 CLI caveman cloud experiments show/results)
- 校验可得性: 登录、项目、实验、结果任一不可得即中止; 证据必需字段缺失判为 evidence incomplete, 不视为通过
- 评估证据: 报告生命周期状态与安全级别、对照/候选样本量、质量评测、延迟/错误/成本等护栏、结果是否 pending/failed/promotable
- 提出唯一建议动作 (start/approve/cancel/rollback) 及理由, 并注明执行被阻塞直至服务端权威门禁上线
- 不执行任何生命周期变更; 若操作者声称已执行命令, 重新读取服务端详情与结果并回报前后状态对比

- 只读访问层: 数据来自 Caveman Cloud control-api, agent 侧 MCP 工具 (caveman_context / caveman_experiment_get) 与 CLI 备选路径均只暴露读操作, 因服务端尚未原子化强制完整的状态迁移表与证据门禁
- fail-closed 校验: 未知状态与服务端错误一律拒绝并透传 cave_snake_code; 缺字段不算通过; 严禁把实验 lift 转成 verified_savings——只有活跃真实流量加 provider 因果、provider 完整的账本证据才有资格
- 变更拦截: 即使有用户口头批准也不发出可执行的生命周期命令——`<action>:<experiment_id>` 这类字符串可由 agent 自行生成, 不构成人类意图证明; 组织 id 永不由 agent 提供, 项目/租户范围来自登录身份与服务端 RBAC
