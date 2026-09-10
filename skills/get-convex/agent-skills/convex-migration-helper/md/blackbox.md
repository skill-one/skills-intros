# convex-migration-helper (`get-convex/agent-skills/convex-migration-helper`)

## blackbox

**function**: 帮你安全地改动 Convex 数据库 (应用的后台数据存储) 的表结构——给出不中断线上服务、不丢数据的迁移方案和可直接使用的代码。

- input: 一句需求描述, 如「users 表要把 email 字段改成必填, 线上已有 50 万条旧数据」, output: 一份分步迁移计划: 先改哪个文件、后改哪个文件、中途执行什么命令, 每步附可直接粘贴的代码
- input: 现在的表结构定义代码 + 想做的改动, 如「加一个必填的 status 字段」, output: 结论: 这个改法现在直接上线会不会报错, 以及改过之后能直接替换使用的新表结构代码
- input: 一个问题, 如「怎么给已有的几万条旧数据补上新建的字段?」, output: 一段可运行的回填代码, 附带先演练验证、再正式执行、最后查看进度的具体命令
