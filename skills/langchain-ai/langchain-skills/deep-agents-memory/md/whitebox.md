# deep-agents-memory (`langchain-ai/langchain-skills/deep-agents-memory`)

## whitebox

- 调用方发起 agent.invoke(消息, thread_id), 会话建立
- Agent 需要文件操作时, 使用 FilesystemMiddleware 注入的工具 (ls / read_file / write_file / edit_file / glob / grep)
- 文件请求进入 Backend 层, 由 backend 配置决定落点: 默认 StateBackend; 若为 CompositeBackend 则按路径前缀路由
- Backend 执行实际读写: StateBackend 写线程内临时状态, StoreBackend 写持久 store, FilesystemBackend 直接写本地磁盘
- 结果返回; 命中持久路由 (如 /memories/) 的文件跨 thread 可读, 其余随线程结束丢失

- 前缀路由: CompositeBackend 按 path 前缀匹配分发到子 backend, 最长前缀优先 (如 /mem/temp/ 优先于 /mem/); 只有命中持久路由的文件才能跨线程存活
- 存储抽象: StateBackend (线程内临时, 零配置) / StoreBackend (跨线程持久, 必须显式传入 store 实例, 生产环境换 PostgresStore) / FilesystemBackend (真实磁盘, 开启 virtual_mode 限制路径逃逸), 三者对上层工具透明
- 外部依赖: deepagents 库 (Python / TypeScript 双端) + LangGraph (提供 InMemoryStore / PostgresStore 存储与 MemorySaver 检查点); thread_id 由调用方 config 传入, 底层由 create_deep_agent 指定的 LLM API 驱动推理
