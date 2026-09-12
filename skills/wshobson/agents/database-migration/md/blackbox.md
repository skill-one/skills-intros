# database-migration (`wshobson/agents/database-migration`)

## blackbox

**function**: 帮你安全地改动数据库结构——加字段、改类型、搬迁整理数据、升级版本,服务不中断,出问题能一键退回原样。

- input: 一句话需求:"给用户表加一个 status 字段,默认值 active"(附上你项目用的框架,如 Prisma / TypeORM), output: 能直接运行的迁移文件,自带正向执行和"一键撤销"两个版本,附上对应的执行与回滚命令
- input: "线上有百万条数据,要把 age 列从文本改成数字,不能停服务", output: 一套分步执行的零停机改造方案:先加新列→搬数据→切换→删旧列,用户全程无感知
- input: "把 address_string 这一列拆成街道、城市、省份三列", output: 自动把旧地址数据拆分搬进新列的迁移脚本,中途失败会自动恢复到改动前的样子
