# neon-postgres (`neondatabase/agent-skills/neon-postgres`)

## whitebox

- 确认项目归属: 用 Neon CLI (默认) 或 MCP 列出组织/项目, 先读 `.neon` 文件看是否已关联项目和分支, 由用户选定或新建
- 取连接串: 通过 CLI 或 `neon env pull` 拿到 `DATABASE_URL`, 写入 `.env` 前先读原文件避免覆盖已有值
- 按运行时选驱动和连接方式: 默认配 Drizzle ORM; Vercel 用 node-postgres、Netlify 等 serverless/edge 用 @neondatabase/serverless; 同时决定走池化还是直连
- schema 以代码管理: 迁移只通过 ORM (如 Drizzle Kit) 执行, 不对数据库做临时 ad hoc 变更; 上线前先在生产的分支上用类生产数据试跑迁移
- 出问题时跑预置只读诊断: 按症状对照表选最小的 `neon inspect db <check>` 或 MCP `inspect_database` 检查, 改动后重跑同一检查验证

- 连接分流: 同一库有两个连接串——带 `-pooler` 后缀的走 PgBouncer (连接池, 事务模式), 供应用流量; 迁移、pg_dump、逻辑复制、依赖会话状态的 SET / LISTEN-NOTIFY 必须用无后缀直连, 用错会出现 prepared statement 已存在、relation 不存在等不指明原因的报错
- 预置诊断替代手写 SQL: CLI 与 MCP 跑同一套只读检查 (outliers/calls 依赖 pg_stat_statements 扩展, lfc-hit-rate/working-set 依赖 neon 扩展, 装扩展前需先询问); 解释结果有安全守则——unused-indexes 只是候选列表, 统计数据在计算重启/休眠后清零
- Neon 专属执行计划: 标准 EXPLAIN 看不到缓存行为, 加 `PREFETCH, FILECACHE` 参数可观察本地文件缓存命中与预取指标 (只读且无需扩展); 由于 ANALYZE 会真实执行语句, 仅对安全的只读 SQL 使用; 涉及通用 Postgres 优化时再加载 postgres-best-practices 子技能
