# sql-optimization-patterns (`wshobson/agents/sql-optimization-patterns`)

## whitebox

- 接收任务: 慢查询调试、表结构设计或应用响应优化 (SKILL.md 适用场景清单)
- 用 EXPLAIN 获取查询执行计划, 重点读扫描方式 (Seq Scan → Index Scan → Index Only Scan)、cost、rows、actual time
- 对照已知陷阱清单定位瓶颈: 缺索引、WHERE 里包函数、前导通配符 LIKE '%x'、隐式类型转换、OR 条件、N+1 查询
- 施加优化: 改写查询 (去 SELECT *、先过滤再 JOIN) + 建匹配的索引 (B-Tree / 组合 / 部分 / 表达式 / 覆盖 / GIN)
- 复跑 EXPLAIN ANALYZE 验证效果, 转入持续监控; 若主文档不够用, 再读 references/details.md 补细节

- 执行计划分析机制: 依赖 PostgreSQL 的 EXPLAIN / EXPLAIN ANALYZE / EXPLAIN (ANALYZE, BUFFERS, VERBOSE), 以扫描类型和实际耗时为准做诊断——只认计划输出, 不靠猜
- 查询↔索引映射机制: 按访问模式选型——B-Tree (等值/范围, 默认)、Hash (仅 =)、GIN (全文/JSONB/数组)、GiST (几何)、BRIN (超大表); 索引列顺序、部分索引 WHERE 条件、INCLUDE 列都严格对齐查询写法
- 监控与维护机制: 依赖 PostgreSQL 系统视图 pg_stat_statements (最慢的 10 条)、pg_stat_user_tables (全表扫描频次=缺索引信号)、pg_stat_user_indexes (idx_scan=0=无用索引), 配合 ANALYZE / VACUUM / REINDEX 常规保养; 唯一外部依赖是目标 PostgreSQL 数据库, 无外部模型 API
