# sql-optimization-patterns (`wshobson/agents/sql-optimization-patterns`)

## comments

- user: 后端老兵, category: 妙用, comment: 先跑 pg_stat_statements 捞出最慢的 10 条,按真实耗时排优先级,不再凭感觉乱优化,半天就清完积压的慢查询。
- user: 第一次用的新手, category: 坑, comment: 给 email 建了索引却还是全表扫描——WHERE 里写了 LOWER(email),函数会让索引失效,得改建成 LOWER(email) 的表达式索引。
- user: 运维老哥, category: 注意, comment: VACUUM FULL 会锁表,我曾在业务高峰跑过一次,线上直接卡住。只在维护窗口执行,日常用 VACUUM ANALYZE 就够。
- user: 电商后端, category: 妙用, comment: 千万级订单表只给 status='active' 建了部分索引,索引体积小了一个量级,热查询照样走索引,写入几乎无感。
- user: 接手祖传库的, category: 坑, comment: 接手祖传库时给每个字段都补索引,后台写入慢了一倍。用 pg_stat_user_indexes 查出 idx_scan=0 的废索引删掉才恢复。
- user: 数据工程师, category: 注意, comment: 联合索引 (user_id, status) 匹配不上只查 status 的条件,建之前先列清楚常跑的查询组合;另外 LIKE '%词' 这种开头通配符也吃不到索引。
