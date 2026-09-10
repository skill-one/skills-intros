# convex-seed (`get-convex/agent-skills/convex-seed`)

## comments

- user: 全栈独立开发者, category: 妙用, comment: seed 函数写成先清后插, 改完 schema 跑一遍 npx convex run, 表立刻回到干净数据, 不用去 dashboard 手删行。
- user: 第一次用的新手, category: 坑, comment: 我把 seed 连跑了两遍, 数据直接翻倍。开头加清表逻辑后才敢重跑, 现在随时能刷出干净环境。
- user: 后端老兵, category: 注意, comment: 共享部署别灌真实数据: 我导过一份带手机号的用户表, 部署里同事全看得到。演示数据一律脱敏或造假。
- user: 前端转全栈, category: 坑, comment: npx convex import 的字段必须和 schema 校验器一一对应, 少个字段或类型不符整批被拒, 先照 schema 改好数据再导。
- user: QA 测试工程师, category: 妙用, comment: 我在 seed 里顺手塞了空字符串、超长昵称这类边界行, 每次重跑环境自带测试用例, 不用手动造数据。
- user: 带新人的技术负责人, category: 注意, comment: 导完别急着关终端, 对比源文件行数和表里实际条数, 我遇到过尾部空行导致数量对不上才发现漏导。
