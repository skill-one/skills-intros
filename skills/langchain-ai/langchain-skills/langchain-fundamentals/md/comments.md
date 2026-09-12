# langchain-fundamentals (`langchain-ai/langchain-skills/langchain-fundamentals`)

## comments

- user: 后端老兵, category: 妙用, comment: 给删数据、发邮件这类危险工具加 HumanInTheLoopMiddleware，agent 执行前会暂停等人批准，生产上才敢真放手。记得要配 checkpointer 和 thread_id，不然恢复不了。
- user: 第一次写 agent 的新手, category: 坑, comment: 拿 result.content 打印回答，直接 AttributeError，折腾一下午。正确写法是 result["messages"][-1].content，取最后一条消息。新手第一坑，先记住这句。
- user: 转行学 AI 的产品经理, category: 坑, comment: 连着两次 invoke，第二次它就忘了我说过什么，还以为模型坏了。原来是没加 checkpointer，补上 MemorySaver() 并每次传同一个 thread_id 才有记忆。
- user: 做数据抽取的算法工程师, category: 妙用, comment: 简单抽取任务根本不用建 agent，model.with_structured_output(Pydantic 模型) 一行拿到带类型校验的结果，比让模型吐 JSON 再自己解析稳太多了。
- user: 全栈独立开发者, category: 坑, comment: 让 agent 查资料它会一直循环烧 token，直到我在 invoke 的 config 里设了 recursion_limit: 10 才刹住车。跑长任务前先想好步数上限。
- user: 从老版本迁移过来的用户, category: 注意, comment: 网上老教程还在教 initialize_agent，照抄就是过时写法。现在统一用 create_agent()，模型直接传 "openai:gpt-4.1" 这种字符串就行，不用先建实例。
