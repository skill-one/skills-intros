# langchain-fundamentals (`langchain-ai/langchain-skills/langchain-fundamentals`)

## whitebox

- 用 @tool (Python) / tool() (TypeScript) 定义工具函数, 写清 docstring 描述和参数类型
- 调用 create_agent() 装配 agent: 传入模型 (如 "anthropic:claude-sonnet-4-5")、工具列表、system_prompt
- agent.invoke({"messages": [...]}) 触发 agent 循环, create_agent 内部托管: 模型推理 → 执行工具 → 结果回传继续推理, 直到产出最终回答
- 从 result["messages"][-1].content 读取最后一条消息作为输出 (不能直接访问 result.content)
- 如需跨调用记忆, invoke 时带 checkpointer + thread_id, agent 能记住同 thread 的历史对话

- 循环托管: create_agent() 负责整个 agent loop、工具执行和状态管理, 模型推理走外部模型 API (LangChain 集成的 anthropic:*/openai:* 字符串或模型实例, 底层为 langchain_anthropic / langchain_openai)
- 工具绑定: @tool 把普通函数转成模型可调用工具, 函数 docstring + Args 注解就是模型看到的'说明书' — 描述含糊模型就不知道何时/怎么调用; TypeScript 侧用 tool() + zod schema 定义
- 状态与控制: checkpointer (langgraph 的 MemorySaver) 按 thread_id 持久化对话状态; middleware 挂载在 agent 循环上拦截流程 — HumanInTheLoopMiddleware 可在指定工具执行前暂停等人工审批 (依赖 checkpointer + thread_id), 恢复用 Command(resume=...)
