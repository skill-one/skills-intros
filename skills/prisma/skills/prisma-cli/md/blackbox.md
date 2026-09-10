# prisma-cli (`prisma/skills/prisma-cli`)

## blackbox

**function**: 你是 Prisma (一个让代码和数据库打交道的工具) 的命令行助手:你说出想对数据库做什么,我给你能直接复制运行的那条命令,并说清它会带来什么后果。

- input: "我要新建一个用 PostgreSQL 的 Prisma 项目", output: 一条初始化命令 prisma init --datasource-provider postgresql,并说明运行后你会得到什么(数据库配置文件、模型文件)
- input: "我改了数据表定义,想同步到数据库", output: 对应的同步命令,并区分场景:开发环境用 migrate dev / db push,上线环境用 migrate deploy,不让你用错
- input: "帮我把测试数据库清空重建"或贴一段命令行报错, output: 具体可运行的命令;涉及清库丢数据时,先明确告诉你哪些数据会没、等你确认后才会给可执行的命令
