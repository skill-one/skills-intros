# prisma-postgres-setup (`prisma/skills/prisma-postgres-setup`)

## blackbox

**function**: 给你的项目从零开通一个云端 Postgres 数据库, 并在本地项目里配好连接, 让你的代码能直接读写数据。

- input: 一句「帮我建个数据库」+ 一个 Prisma 服务令牌, output: 一个可用的云端数据库, 连接串已写进项目的 .env, 本地代码直接连上
- input: 用大白话描述数据, 如「我在做任务管理器, 有项目、任务、成员」, output: 生成好的 schema 文件 + 数据库里已建好的表, 代码可直接查询这些数据
- input: 一个还没接数据库的本地项目文件夹, output: 依赖装好、配置就绪的项目, 外加一条验证通过的连接测试和可浏览数据的链接
