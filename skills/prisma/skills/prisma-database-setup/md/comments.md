# prisma-database-setup (`prisma/skills/prisma-database-setup`)

## comments

- user: 第一次用的新手, category: 坑, comment: 改完 schema 忘跑 `prisma generate`, 新字段查不到还满屏类型错。现在改完立刻 generate, 再没折腾过。
- user: Mongo 五年老用户, category: 坑, comment: 照 Prisma 7 教程给 Mongo 装 SQL adapter, 项目直接起不来。Mongo 留在 6.x, URL 写在 schema 里就行。
- user: Bun 党, category: 注意, comment: Bun 项目里敲 `npx prisma` 会悄悄回退到 Node。记得换 `bunx --bun prisma`, 才真跑在 Bun 上。
- user: 后端老兵, category: 妙用, comment: 本地拿 SQLite 秒起开发库, 上线前把 provider 换 postgresql、adapter 换 pg, 业务代码几乎不动。
- user: 运维老哥, category: 注意, comment: CI 的 Node 还停在 18, generate 当场报版本错。先升 Node ≥ 20.19、TS ≥ 5.4, 省一次深夜排查。
- user: 独立开发者, category: 注意, comment: 新 generator 必须写 output 路径, 我漏了直接报错。照抄 `output = "../generated"` 就好。
