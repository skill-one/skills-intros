# supabase-postgres-best-practices (`supabase/agent-skills/supabase-postgres-best-practices`)

## blackbox

**function**: 帮你处理一切 Postgres 数据库任务: 建表改表、写优化过的 SQL、排查慢查询和高负载、配置数据安全规则, 产出直接可用的 SQL 和改法。

- input: 「帮我建一张订单表, 要有用户、金额、状态这些字段」, output: 一段可直接执行的建表 SQL, 字段类型、主键、索引、约束都配好了
- input: 一条跑得很慢的查询 SQL + 「为什么这么慢?」, output: 诊断结论 + 改写后的查询 + 该加哪个索引的具体建议
- input: 「怎么保证用户 A 看不到用户 B 的数据?」, output: 对应的行级安全策略 SQL (RLS, 数据库层的访问控制), 以及验证它生效的测试
