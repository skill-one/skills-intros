# extension-querying-oql (`caffeinelabs/skills/extension-querying-oql`)

## comments

- user: 第一次用的新手, category: 坑, comment: 第一次把 JSON 原样粘进命令,解析报错卡半天。execute 的参数必须包成 ("..."),里面每个双引号都要写成 \"。照指南里的例子抄格式,别自己手改。
- user: 后端老兵, category: 注意, comment: 字段名拼错不会报错,会被当成 null_,查询静默返回空。我先跑一次 schema(),对着它报的字段名抄,大小写和 __1、__2 后缀都别改,一次就过。
- user: 数据分析师, category: 妙用, comment: 要去重的公司名列表,本来想拉全量本地去重,后来发现 groupBy 不带 aggregate 就是服务端 DISTINCT,一条命令直接回去重结果,大表也不怕。
- user: 运维老哥, category: 注意, comment: 验收时查出来的数据跟线上对不上,折腾半天才想起默认读的是 draft 草稿版,加 --branch live 才是已部署的正式数据。上线验收前记得切。
- user: 踩过统计坑的业务分析, category: 坑, comment: 算各部门平均预算,从 employee 写 avg(department.budget) 数字偏大——聚合按 start 实体的行数加权。要按部门算,得换 department 当起点。
- user: 兼职写报表的前端, category: 启发, comment: 以前习惯拉全表到本地筛,现在先想服务端能否一步出数:用户手打的搜索词用 icontaints 忽略大小写,计数用 count 只回一行,省得来回搬数据。
