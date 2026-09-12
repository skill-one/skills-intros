# rust-async-patterns (`wshobson/agents/rust-async-patterns`)

## whitebox

- 接到与异步 Rust 相关的任务 (写 async 应用、并发网络服务、Tokio I/O、async 错误处理、调 async 代码), 按 skill 的适用场景触发
- 先用 Core Concepts 的执行模型定位问题: Future 惰性 → poll() → Ready/Pending, 由 Runtime 轮询和调度
- 从 Quick Start 取标准骨架: Cargo.toml 依赖清单 + #[tokio::main] + async fn/await 的最小可运行示例
- 需要更深模式 (channels/streams/async trait) 时, 按指引去读 references/details.md
- 产出前按 Best Practices 的 Do/Don't 清单逐条校验 (select! 竞速、channel 优先、禁止阻塞、锁不跨 await、Semaphore 限并发)

- 场景触发映射: skill 的 'When to Use This Skill' 五类场景决定激活与否及切入角度, 不猜用户意图
- 两层知识加载: skill.md 顶层只保留执行模型图、核心抽象表、Quick Start 和 Do/Don't 清单, 细节模式下沉到 references/details.md 按需读取
- 依赖栈 (全部是外部库, 无模型调用): Tokio 1.x (异步运行时, features=["full"])、futures 0.3、async-trait 0.1、anyhow (错误传播)、tracing + tracing-subscriber (日志与调试埋点)
