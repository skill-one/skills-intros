# prisma-upgrade-v7 (`prisma/skills/prisma-upgrade-v7`)

## comments

- user: MongoDB 全栈, category: 坑, comment: 没看开头的提醒就照着升,Mongo 项目升完才发现 v7 没有 MongoDB connector,连夜回退 v6。用 Mongo 的停在 6.x,别走这条升级路。
- user: 第一次升级的新手, category: 坑, comment: 升完一直报连不上数据库,还以为是库挂了——其实是 v7 不再自动读 .env,装 dotenv 并在 prisma.config.ts 顶部 import 才好。
- user: 老 CJS 项目维护者, category: 注意, comment: 别被 ESM-first 吓到就把老项目改造成 ESM,generator 里加一行 moduleFormat = "cjs" 就能升,我差点动手重构整个代码库。
- user: 十年后端, category: 妙用, comment: Prisma.validator 换成 satisfies 后,我把公共 select 抽到共享文件,字段写错编辑器当场报错,比以前的泛型套娃清爽。
- user: 运维老哥, category: 坑, comment: 一台 Node 18 的老服务器升完直接起不来,白排障一小时。动手前先核对:Node 20.19+、TypeScript 5.4+,不满足先升运行时。
- user: 小团队主程, category: 注意, comment: client 不再生成进 node_modules,新同事拉代码必报 Cannot find module——要跑 prisma generate,我们加进了 postinstall。
