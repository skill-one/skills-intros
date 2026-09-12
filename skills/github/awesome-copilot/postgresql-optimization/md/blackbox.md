# postgresql-optimization (`github/awesome-copilot/postgresql-optimization`)

## blackbox

**function**: 把你的 PostgreSQL 数据库相关问题变成可执行的解决方案: 慢查询帮你提速, 数据怎么存帮你设计, 报错卡顿帮你排查。

- input: 一段跑得很慢的查询语句 (SQL), 或它的 EXPLAIN 执行结果, output: 改写后更快的查询 + 一两条建索引的语句 + 简短说明慢在哪、能快多少
- input: 一段大白话需求, 如「存商品数据, 标签数量不固定, 还要按标签和价格区间搜索」, output: 可直接执行的建表 SQL (用对 JSONB/数组/范围等合适的数据结构) + 配套的查询示例
- input: 一条现象描述或报错, 如「高峰期偶尔卡几秒」「连接数满了」「这张表越来越大越来越慢」, output: 几条复制粘贴就能跑的排查语句 + 每个结果分别说明什么问题、怎么处理
