# swift-concurrency (`avdlee/swift-concurrency-agent-skill/swift-concurrency`)

## whitebox

- 解析项目配置: 读 Package.swift / .pbxproj, 确认语言模式、严格并发级别、默认隔离、upcoming features; 配置未知则询问开发者, 绝不猜测 (即使 Xcode 26 新项目)。
- 捕获确切的诊断信息 (编译器/SwiftLint 报错) 和出错的符号。
- 判定隔离边界: @MainActor、自定义 actor、实例隔离还是 nonisolated, 并确认代码是否 UI 绑定、同步前缀该在哪个 actor 上启动 Task。
- 查'常见诊断'表 → 选最小安全修复; 满足 Quick Fix 条件 (单文件单类型、隔离边界清晰、1-2 步行为不变) 时直接给修复。
- Quick Fix 失败则: 收集配置 → 重估类型跨越的隔离边界 → 路由到对应 references/*.md 深挖; 变更后按 构建→修一类错→重建→测试 循环验证, 不批量修不相关错误。

- 配置先行: 任何诊断解读前, 必须先从 SwiftPM (.enableExperimentalFeature / .enableUpcomingFeature / .defaultIsolation) 或 Xcode (SWIFT_STRICT_CONCURRENCY / SWIFT_DEFAULT_ACTOR_ISOLATION / SWIFT_APPROACHABLE_CONCURRENCY) 提取并发行为设置——同一报错在不同配置下结论不同。
- 诊断路由表: 把报错按固定表匹配 (如 'Main actor-isolated...' → 检查是否真 UI 绑定 → 最小修复 → 升级到 references/actors.md); 附带守则: 禁止假 await、禁止 @MainActor 一把梭、迁移时不重构无关架构; references/*.md 是技能内置的深度参考路由 (async-await-basics / tasks / actors / sendable / migration 等 14 个文件)。
- 最小安全变更纪律: 优先行为保持的修复 (UI 状态→@MainActor, 共享可变状态→actor, Sendable 问题→不可变值); 逃生舱 (@preconcurrency / @unchecked Sendable / nonisolated(unsafe)) 必须附带文档化安全不变量 + 后续移除计划; 验证依赖外部工具: swift build / Xcode 构建、swift test / Cmd+U、Instruments (性能结论不许猜)。
