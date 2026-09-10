# neon-postgres (`neondatabase/agent-skills/neon-postgres`)

## blackbox

**function**: 帮你从零搭建并连接 Neon Postgres 数据库, 排查线上变慢的原因, 安全地变更表结构, 还能给应用加上语义/全文搜索。

- input: 「帮我建个 Neon 数据库, 接到我的 Vercel 项目里」, output: 数据库建好, .env 里写好可直接使用的 DATABASE_URL, 应用立刻能正常读写数据
- input: 「线上数据库最近查询特别慢」+ 一段慢查询或报错信息, output: 一份诊断报告: 指出最耗时的 SQL、缺失或无用的索引、缓存命中情况, 并给出可直接执行的修复建议
- input: 「我要给 users 表加一列, 但不敢直接动生产库」, output: 先在生产数据的瞬时副本上完成迁移并验证结果, 确认无误后才应用到真实生产库, 全程零风险
