# convex-monitor (`get-convex/agent-skills/convex-monitor`)

## whitebox

- 调用 wait_for_event (project_dir, event_kinds, timeout_ms), 阻塞等待下一个事件而非轮询
- 竞速三路信号源: 本地错误日志、Convex 部署订阅、Sentinel prod 错误行, 谁先触发返回谁; 都没触发则返回 quiet 心跳
- 按事件类型分派: convex_error/next_error → 解码并修复; prod_error → 经 Sentinel 分诊后修复; feature_request → 直接实现
- kind=quiet 时回到第 1 步继续循环等待

- 阻塞优先、轮询兜底: 优先用 blocking MCP 工具 wait_for_event; 仅当 harness 没有阻塞式 MCP (如 Copilot cloud) 时退化为 poll loop, 但两者使用同一事件契约 — 行为一致, 只是机制不同
- 固定且版本化的事件 schema: 每种触发映射到同一类型化事件 (typed event), kind 枚举为 convex_error / next_error / prod_error / feature_request / quiet
- 外部依赖: prod_error 事件要求已部署的云端 Convex 应用 + Sentinel (prod 错误监控); dev 路径依赖本地错误日志与 deployment 订阅
