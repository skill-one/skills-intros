# prisma-upgrade-v7 (`prisma/skills/prisma-upgrade-v7`)

## blackbox

**function**: 帮你的 Prisma ORM (一种数据库开发工具) 项目从 v6 升级到 v7: 给出改好的配置和代码, 并解决升级后出现的各种报错。

- input: 项目里的 schema.prisma 文件内容 (v6 旧写法), output: 升级后的完整写法 + 需要在终端执行的具体安装命令
- input: 升级后的一段报错, 如 "Cannot find module" 或数据库连不上, output: 报错原因说明 + 修好的代码 / 命令, 照抄即可通过
- input: v6 的旧代码片段, 如 new PrismaClient() 的初始化写法, output: 改成 v7 语法的对应代码, 替换原位置即可运行
