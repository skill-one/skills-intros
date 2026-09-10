# convex-insights (`get-convex/agent-skills/convex-insights`)

## whitebox

- 守门: 确认并宣告正在读取哪个 Convex 部署 (status), 全程只读, 不开任何变更开关
- 先探明再查: 用 functionSpec 列出真实函数名、status 拿部署/版本 — 从不猜标识符
- 按问题三选一视图 (failures / health / trace), 用 logs --history <n> --jsonl 或 insights 拉取有界的近期窗口
- 本地过滤聚合: 按函数 + 错误信息分组, 给出计数和首个代表性堆栈, 不倾倒原始日志
- 回答 = 一行结论 + 证据 + 自拼的 dashboard 深链; findings 发上总线, 性能/成本以指针移交 convex-advisor

- 外部依赖: 官方 Convex MCP 的只读工具 (logs / insights / functionSpec / status); 已知约束 — logs 只有 --history 条数参数, 无服务端的状态/函数/requestId/时间过滤, insights 仅限云端部署, 所以统一策略是'拉有界窗口 + 客户端侧过滤', 不假装有不存在的参数
- 三视图纪律: 每个问题只选一个视图 — failures (失败分组计数, 回答'什么在报错/部署后坏了什么')、health (insights 的 72h 类型化限流/OCC 事件)、trace (本地按 requestId/函数切出单次执行); 靠分组聚合而非逐行 dump 控制输出体积
- 答案组装与移交: 无任何工具返回链接, 深链由部署名 + 函数名自行拼到 dashboard.convex.dev 供人一键核验; '部署是否引入故障'用日志时间戳对照 status 版本做关联而非断言; 产出按 finding schema 主要走 observability, 性能/成本作为指针 finding 让 convex-advisor 独占修复框架, 前瞻反应交给 monitor/sentinel
