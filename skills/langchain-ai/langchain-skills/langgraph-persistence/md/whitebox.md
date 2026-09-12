# langgraph-persistence (`langchain-ai/langchain-skills/langgraph-persistence`)

## whitebox

- 用户任务命中技能描述 (LangGraph 状态持久化 / 记住对话 / 时间旅行 / 子图 checkpointer 配置) 时被触发
- 先判定记忆类型: 线程内短期记忆用 checkpointer, 跨线程长期记忆用 store
- 按场景选 checkpointer: 测试开发用 InMemorySaver, 本地开发用 SqliteSaver, 生产用 PostgresSaver
- 产出代码: 在 compile(checkpointer=...) 时注入, invoke 时始终携带 thread_id 配置; 需要跨线程记忆时再加 store 并同时编译
- 按边界清单收尾校验: thread_id 必填、生产禁用内存版、update_state 会经过 reducer (替换需用 Overwrite)、store 须经 runtime.store 访问、子图按三档模式选 scoping

- 检查点机制: checkpointer 在每个 super-step 保存图状态, thread_id 隔离不同对话序列; 时间旅行 = get_state_history 遍历历史 checkpoint, 再 invoke(None, past_config) 回放, 或 update_state 后分叉续跑
- 双存储分工: 短期记忆 (checkpointer) 只在 thread 内生效; 长期记忆 (store) 用 put/get/search/delete 读写用户偏好等事实, 跨所有 thread 共享
- 外部依赖: langgraph 库 (Python / TypeScript 双语言 API); PostgresSaver 依赖外部 PostgreSQL 数据库, 部署时需一次性 setup() 建表
