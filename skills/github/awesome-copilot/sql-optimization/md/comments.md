# sql-optimization (`github/awesome-copilot/sql-optimization`)

## comments

- user: 后端老兵, category: 妙用, comment: 把慢 SQL 连 EXPLAIN 结果一起贴进去，它逐条对着执行计划指出哪步全表扫描，改写理由直接搬进代码评审文档就能过。
- user: 第一次用的新手, category: 坑, comment: 照抄它的游标分页示例，但排序字段 created_at 有重复值，翻页漏数据。加 id 做第二排序字段才修好，别用单时间戳做游标。
- user: 接手老项目的后端, category: 注意, comment: 先说清自己用的数据库。它给的部分索引（带 WHERE 条件的索引）语法在 MySQL 直接报错，那是 PostgreSQL 的写法。
- user: DBA 老哥, category: 坑, comment: 它建议的索引别照单全收。我们没查现有索引一口气加了三个单列索引，订单表写入高峰 CPU 立涨，先合并重复索引再上。
- user: 数据分析师, category: 妙用, comment: 后台十几个订单状态各查一遍 COUNT，按它说的改成单条 CASE WHEN 聚合，一次查询全出结果，报表页直接快一个量级。
- user: 技术组长, category: 启发, comment: 最大收获是排查顺序：先从慢日志找靶子，再看执行计划，最后才改 SQL。以前我们凭感觉上来就加索引，白建了一堆。
