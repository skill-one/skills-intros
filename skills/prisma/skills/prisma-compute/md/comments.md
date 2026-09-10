# prisma-compute (`prisma/skills/prisma-compute`)

## comments

- user: 后端老兵, category: 妙用, comment: 上线前用 `app deploy --no-promote` 先出一个候选部署，它有独立 URL，自测通过再 `app promote` 切换。全程不碰线上，等于免费灰度。
- user: 第一次用的新手, category: 坑, comment: 部署后一直 504，本地却正常。原因是我监听写死了 localhost。平台要求绑 0.0.0.0 并读 process.env.PORT，改这两行立刻通了。
- user: 运维老哥, category: 坑, comment: CI 残留的 PRISMA_SERVICE_TOKEN 让我 `auth workspace use` 死活不生效——这个变量存在（哪怕空值）就只认它。切工作区前先 unset。
- user: 全栈独立开发, category: 注意, comment: 重新部署不会自动跑数据库迁移和 seed，我上线后新字段全空才反应过来。`prisma migrate deploy` 要自己单独执行，别指望部署帮你做。
- user: 接手老项目的前端, category: 坑, comment: PR 合并到默认分支本身就是生产部署，别再手动重发那个分支（我就重发过，状态全乱）。查构建失败用 `build logs`，它和 `app logs` 是两套 ID。
- user: 小团队技术负责人, category: 启发, comment: region、框架、端口这些非敏感默认值写进 `prisma.compute.ts`，密钥只走环境变量，配置就能进 git。队友 clone 下来一条 `compute:deploy` 就对齐了。
