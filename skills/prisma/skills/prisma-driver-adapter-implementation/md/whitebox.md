# prisma-driver-adapter-implementation (`prisma/skills/prisma-driver-adapter-implementation`)

## whitebox

- 1. 对照已安装的 Prisma 版本, 锁定精确匹配的 @prisma/driver-adapter-utils 类型定义, 再动手写代码
- 2. 按契约实现工厂与 SqlDriverAdapter: queryRaw / executeRaw / executeScript, 事务 startTransaction 独占一条连接
- 3. 映射层: 参数按 值+ArgType 逐个转换, 行结果用 array 模式保证列序, 元数据映射到 Prisma 的 ColumnType
- 4. 事务收尾: commit/rollback 只做释放连接的生命周期钩子 (不发第二条 COMMIT/ROLLBACK SQL), 错误包装为 DriverAdapterError 并保留原始 code/message
- 5. 跑验证清单: 按目标版本 typecheck + Prisma Client 集成/E2E 测试 (不只是适配器单测)

- 契约即边界: 类型兼容不等于行为正确 (仍可能损坏值、泄漏连接), 所以硬性规则是每事务独占连接、savepoint 挂在 Transaction 而非全局、工厂 dispose 只释放自己创建的连接池
- 错误保真: 已知错误映射成结构化 MappedError (如 23505 → UniqueConstraintViolation), 未知错误保留 originalCode/originalMessage 供 P2039 兜底, 非数据库错误原样 rethrow 以暴露代码 bug; 依赖 @prisma/driver-adapter-utils 的 DriverAdapterError 类型
- 参考实现对齐: 以官方 adapter-pg (pg 驱动) 的事务与错误映射源码为范本; shadow database (迁移用的隔离库) 必须与主库隔离、用加密随机名并在失败时清理, 才允许实现 SqlMigrationAwareDriverAdapterFactory
