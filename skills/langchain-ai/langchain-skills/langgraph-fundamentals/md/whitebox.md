# langgraph-fundamentals (`langchain-ai/langchain-skills/langgraph-fundamentals`)

## whitebox

- 触发: 用户要求编写任何 LangGraph 代码 (建图、状态、路由、Send 并行、流式、错误处理) 时激活本技能
- 设计: 按内置 5 步法走 — 画流程拆节点 → 分类节点 (LLM/数据/动作/用户输入) → 设计共享状态 → 写节点函数 → 连边并 compile()
- 构建: 基于 StateGraph 写代码, 节点只返回部分更新 dict, 列表类字段靠 reducer 决定合并方式
- 校验: 图必须经 compile() 才能执行; 代码层面防止两类典型错误 — 忘加 reducer 导致覆盖、节点改动并返回整个 state
- 交付: 输出可运行代码, 用 invoke() 跑到底或 stream() 逐步观察 (values/updates/messages/custom 四种模式)

- 状态合并: State 用 TypedDict (Python) / StateSchema+zod (TS) 定义, 列表/累加字段必须挂 reducer (Annotated + operator.add / ReducedValue), 否则后写覆盖前写; 节点约定返回仅含变更字段的 dict
- 流程路由: 固定顺序用 add_edge; 按状态分支用 add_conditional_edges; 更新状态+选路合一步用 Command (goto); 动态扇出并行 worker 用 Send, 结果字段必须配 reducer 聚合
- 运行与容错: 依赖 langgraph (Python) / @langchain/langgraph (TS) 库及 typing_extensions、operator、zod; 图经 compile() 后才能 invoke/stream; 错误分四类处理 — 瞬时错误挂 RetryPolicy 重试, 工具报错交给 ToolNode 回传给 LLM 自愈, 缺信息用 interrupt 交还人类, 其余直接抛出
