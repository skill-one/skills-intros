# langgraph-human-in-the-loop (`langchain-ai/langchain-skills/langgraph-human-in-the-loop`)

## whitebox

- 图编译时挂载 checkpointer (状态存档器)，之后每次调用都带同一个 thread_id，用于定位某次暂停的执行。
- 节点执行到 interrupt(value) 时暂停，value 被透传给调用方——出现在 invoke 结果的 __interrupt__ 字段里。
- 人工审阅后，调用方用 Command(resume=人工输入) + 同一 thread_id 再次 invoke。
- 图从存档点恢复，该节点从头重跑，interrupt() 的返回值就是人工输入。
- 节点返回状态更新，图继续走（比如按人工决定路由到发送或直接结束）。

- interrupt() / Command(resume=...) 配对机制：interrupt 抛出暂停并把 value 暴露在 __interrupt__；恢复时 resume 的值直接成为 interrupt() 的返回值；两侧 payload 必须可 JSON 序列化。
- Checkpointer + thread_id 撑起暂停-恢复：状态在暂停期间被持久化（开发用 InMemorySaver，生产用 PostgresSaver，这是 LangGraph 自带能力，不依赖任何 LLM API）；换 thread_id 等于开新线程，续不上旧执行。
- 重跑语义 + 幂等约束：恢复时节点从第一行重新执行（子图场景下父节点和子图节点都会重跑），因此 interrupt() 之前只能放幂等操作（upsert / 先查再建），真正的副作用应放在 interrupt() 之后。
