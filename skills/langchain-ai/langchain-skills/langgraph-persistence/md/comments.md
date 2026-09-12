# langgraph-persistence (`langchain-ai/langchain-skills/langgraph-persistence`)

## comments

- user: 刚上手的新手, category: 坑, comment: 第一次跑忘了传 thread_id, 机器人每次 invoke 都失忆。查了半天代码才发现: 不带 thread_id 就完全不存状态。
- user: 做客服机器人的后端, category: 妙用, comment: 拿 get_state_history 翻历史 checkpoint, update_state 回上一步改消息后 invoke(None, config) 重跑, 用户的「重新生成」分支就这么做出来了。
- user: 前端转全栈, category: 坑, comment: 我的 messages 用了 operator.add 做 reducer, update_state 想整体替换, 结果全被追加。想覆盖必须包一层 Overwrite(["新内容"])。
- user: 运维老哥, category: 注意, comment: 开发用 InMemorySaver 没问题, 上生产一重启会话全丢。换 PostgresSaver 后 setup() 只在部署时跑一次建表, 别写进应用启动流程。
- user: 多 Agent 系统开发者, category: 坑, comment: 在同一个节点里循环调同一个 checkpointer=True 的子图, 两次调用写同一个命名空间直接串台。要么改 False, 要么给每次调用套不同节点名。
- user: 全栈独立开发者, category: 启发, comment: 记忆要拆两层: checkpointer 只记当前对话, 用户偏好跨对话得靠 Store。两个都要传给 compile, 节点里从 runtime.store 取, 别直接引用外部变量。
