# langgraph-human-in-the-loop (`langchain-ai/langchain-skills/langgraph-human-in-the-loop`)

## comments

- user: 第一次用的新手, category: 坑, comment: 断点后续跑,传普通 dict 图会从头重跑,传 Command(update=) 会直接卡死。只认 Command(resume=...)。
- user: 后端老兵, category: 坑, comment: 在 interrupt 前写 db.insert 建审批单,每次恢复就多一条重复记录。改成前面只 upsert,写库挪到 resume 之后才干净。
- user: 从自研审批迁移来的全栈, category: 注意, comment: 上手前先记住:不配 checkpointer 会直接报错;每次 invoke 都要带同一个 thread_id,换新的不是续跑,是另开一条线。
- user: 做表单机器人的开发者, category: 妙用, comment: 把 interrupt 放进 while 循环做输入校验,答错就把原值拼进提示语再问一次,前端重试逻辑一行不用写。
- user: 用并行分支攒审批的, category: 妙用, comment: 两个节点同时挂起不用 resume 两次:遍历 __interrupt__ 取每个 id 拼成 map,一次 Command(resume=map) 全续上。
- user: 运维老哥, category: 启发, comment: 以前不敢让自动化碰删库改配置,现在把 interrupt 卡在危险操作前当审批闸,有人把关才敢真正放手。
