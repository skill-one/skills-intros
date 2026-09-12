# sql-optimization (`github/awesome-copilot/sql-optimization`)

## whitebox

- 锁定分析目标: 有选中代码就分析 ${selection}, 没有则面向整个项目
- 扫描 SQL, 逐一比对内置反模式清单: SELECT *、WHERE 里套函数、OFFSET 深分页、关联子查询、逐行插入、N+1 查询
- 按内置正反例重写: 索引友好的 WHERE、游标式分页、窗口函数替代子查询、批量操作、先过滤再 JOIN
- 输出配套索引 DDL (复合/覆盖/部分索引) 和性能监控查询 (MySQL/PostgreSQL/SQL Server 各自语法)
- 过一遍通用优化清单收尾, 提醒用真实数据量和执行计划验证效果

- 核心机制是内置的「反模式 → 修正」映射 (bad/good SQL 成对示例), 纯规则比对, 不解析 AST、不执行任何 SQL
- 跨库通用改写: 同一套优化技巧适用于 MySQL/PostgreSQL/SQL Server/Oracle, 仅监控查询按库给出专属视图 (mysql.slow_log / pg_stat_statements / sys.dm_exec_query_stats)
- 零外部依赖: 不连数据库、不调用外部工具或 API, 全部知识来自 skill 自带的示例、检查清单和优化方法论 (识别→分析→优化→测试→监控→迭代)
