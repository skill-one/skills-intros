# postgresql-optimization (`github/awesome-copilot/postgresql-optimization`)

## comments

- user: 后端老兵, category: 妙用, comment: 把慢 SQL 和 EXPLAIN 输出一起贴, 它靠执行计划里的成本数字定位到全表扫描, 给了部分索引方案, 8 秒查询降到 200ms。只贴 SQL 不够, 记得连执行计划一起给。
- user: 第一次用的新手, category: 坑, comment: 只贴报错不贴建表语句, 它猜的字段名和我的表对不上, 建索引直接失败。后来先贴 CREATE TABLE 再贴慢查询, 一次就准。
- user: 运维老哥, category: 注意, comment: EXPLAIN ANALYZE 是真跑一遍查询的, 我在 2000 万行的生产表上直接执行, 卡了半天。先用不带 ANALYZE 的版本看计划, 或去从库跑。
- user: 数据分析师, category: 妙用, comment: 累计值、月度排名这种需求, 我原来嵌三层子查询, 它一版窗口函数直接通过, 还主动补了环比写法。描述清楚业务需求比贴烂 SQL 效果更好。
- user: 独立开发者, category: 坑, comment: 它让我用 pg_stat_statements 找最耗时的 SQL, 但我的库没装这个扩展, 查询直接报 relation 不存在。先 CREATE EXTENSION 装好再查。
- user: 全栈开发, category: 启发, comment: 看到它把 OFFSET 分页列为反面例子才醒悟, 我 10 万行的列表越翻越慢。改成记住上一页末尾 id 的翻法, 翻到深处也不卡了。
