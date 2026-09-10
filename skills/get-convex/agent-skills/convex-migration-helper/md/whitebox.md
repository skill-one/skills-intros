# convex-migration-helper (`get-convex/agent-skills/convex-migration-helper`)

## whitebox

- 识别任务类型: 是否属于 skill.md 列出的适用场景 (加必填字段/改类型/拆表/重命名/删除字段等破坏性变更), 排除无需迁移的 Greenfield 场景
- 按 widen-migrate-narrow 规划多阶段部署: 先扩 schema (新增字段设为 optional) 并让代码兼容读写新旧两种格式
- 用 @convex-dev/migrations 组件定义迁移, 先以 dryRun: true 空跑验证逻辑
- 通过 npx convex run migrations:xxx 正式执行批量回填, 监控进度并确认所有文档已迁移
- 收窄 schema (新字段改为必填), 清理旧格式处理代码并部署, 确认稳定后再删迁移代码

- 核心约束: Convex 的 schema 校验会拒绝与存量数据不匹配的部署 (无法给缺字段的旧文档加必填字段), 因此一切迁移都走「扩 schema → 迁数据 → 收 schema」的三段式多部署模式
- 批量执行依赖外部组件 @convex-dev/migrations: 内部递归调度实现批处理 + 游标分页 + 状态跟踪 + 失败续跑 + dry run + 进度监控, 避免大表用 .collect() 触发事务限制
- 安全策略: 优先新增字段而非改类型, 不删数据 (用 v.optional + 注释标记废弃); 迁移窗口期内代码必须同时兼容新旧两种数据格式; 仅已知的小表可跳过组件用单个 internalMutation 简化处理
