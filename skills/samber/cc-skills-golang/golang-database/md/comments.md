# golang-database (`samber/cc-skills-golang/golang-database`)

## comments

- user: 第一次用的新手, category: 坑, comment: 我对 UPDATE 也用了 db.Query, 跑两天连接池耗尽报错——Query 返回的 Rows 不关, 连接回不了池. 改用 Exec 才好.
- user: 后端老兵, category: 妙用, comment: 接手老项目时让它走 review 模式, 并行扫出 rows.Close 漏关、没传 context 的查询, 一轮就把历史欠账列成清单.
- user: 运维老哥, category: 注意, comment: 它明确不写建表和迁移 SQL, 这反而是对的——索引缺失上线才炸. 表结构用 golang-migrate 自己写, 只让它写访问层.
- user: 踩过超卖事故的后端, category: 坑, comment: 之前先查库存再扣减, 高并发下超卖. 让它照指南包事务加 SELECT FOR UPDATE, 锁住行再改, 再没复现过.
- user: 从 GORM 迁移过来的, category: 启发, comment: 迁移后所有 SQL 显式写在代码里, 之前 ORM 偷偷生成的 N+1 查询一眼就能看出来, 慢接口当场定位.
- user: 兼职写接口的实习生, category: 坑, comment: 表里 nullable 的 phone 扫进 string 字段直接报错, 改成 *string 后解决, 连 JSON 输出都顺带正确了.
