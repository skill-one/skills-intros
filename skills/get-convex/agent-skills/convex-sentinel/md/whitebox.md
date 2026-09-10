# convex-sentinel (`get-convex/agent-skills/convex-sentinel`)

## whitebox

- 在 convex/convex.config.ts 中用 app.use(sentinel) 安装 @convex-dev/sentinel 组件 (安装可匿名完成)。
- 接入客户端 SDK: React error boundary + window.onerror/unhandledrejection + breadcrumbs (错误发生前的操作轨迹)。
- 错误写入前先脱敏 (默认开启), 存入用户自己部署里的数据表。
- 用 Convex CLI (convex data / run-once-query) 查看近期错误, 并通过 monitor 的 prod_error 事件对新错误作出反应。
- 可选: 开启自愈 cron —— triage 给每个错误分类, 反复出现的非瞬时错误交给 ai-runner 开修复 PR。

- 写入时脱敏 (强制、默认开启): 对 secret 键名和值模式做 default-deny (默认拒绝) 过滤, 永不存原始密钥 —— 因为 agent 读到的错误内容会送达模型 provider。
- 捕获三类信号进同一张表: 服务端函数失败、客户端 JS/React 崩溃 (error boundary + 全局 handler + breadcrumbs)、OCC (乐观并发冲突) 与扩容信号。
- 体量控制: 采样 (sample) + 上限 (cap) 控制成本; 外部依赖为 @convex-dev/sentinel 组件、Convex CLI、ai-runner (触达模型 API)。
