# performance-optimization (`addyosmani/agent-skills/performance-optimization`)

## comments

- user: 后端老兵, category: 妙用, comment: 线上接口集体变慢、数据库会话却空闲,照这句一查,是长事务占死了连接池。以前只会调大 max,现在先找谁占着连接。
- user: 第一次用的新手, category: 坑, comment: 查询慢我直接建索引,跑完没变化还拖慢了写入。后来先 EXPLAIN ANALYZE 才发现列上有函数,普通索引根本用不上。
- user: 独立开发者, category: 坑, comment: 缓存接口响应时 key 里没放用户 ID,结果 A 用户看到 B 的数据。凡是影响返回内容的输入,都必须进缓存键。
- user: 运维老哥, category: 注意, comment: 热 key 一过期,并发请求同时打穿到数据库,缓存反而变成事故。要么先回旧值再刷新,要么让一个请求重算、其余等待。
- user: 前端工程师, category: 注意, comment: 我拿冷缓存的基线对比热缓存的优化结果,测的是缓存不是改动。重测必须同条件同命令,并且一次只改一处。
- user: 带四人小团队的技术负责人, category: 启发, comment: "没变差就留着吧"让我们攒了一堆白维护的代码。现在中性优化一律回滚,失败尝试记进 PERF.md,不再重跑旧实验。
