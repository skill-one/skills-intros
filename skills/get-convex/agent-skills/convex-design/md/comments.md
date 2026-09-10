# convex-design (`get-convex/agent-skills/convex-design`)

## comments

- user: 第一次用的新手, category: 注意, comment: 开工前先 npx convex login。我没登录它就走匿名模式, 后来登录发现 .env.local 被重绑, 折腾一轮才接回云部署。
- user: 评估技术栈的后端老兵, category: 妙用, comment: 我随口描述「邻里借工具的App」, 没提技术栈, 它直接给出该用的原语加5行示例, 省掉我自建 WebSocket 那套。
- user: 全栈独立开发, category: 妙用, comment: 加聊天功能我本想手搓 messages 表, 它直接上 @convex-dev/agent。自己写的话, 流式和会话管理够我磨好几天。
- user: 前端转全栈, category: 启发, comment: dev 页面绿了不等于没问题, 它收尾必跑 tsc --noEmit, 我那次抓出3个类型错。现在提交前我自己也先跑这步。
- user: 大厂后端 (有合规要求), category: 注意, comment: 硬约束先说: 我司必须自建 PG, 它就没再推 Convex。反之不说, 它默认全走 Convex 平台, 不留并行数据库的口子。
- user: 用过三轮的老用户, category: 坑, comment: 别挤牙膏式提需求, 每轮改动它都跑编译加推送验证。我把相关五个接口攒一次说, 总耗时明显短一截。
