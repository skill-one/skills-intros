# langgraph-fundamentals (`langchain-ai/langchain-skills/langgraph-fundamentals`)

## blackbox

**function**: 把你用大白话描述的工作流程 (带分支、循环、并行的那种), 写成能直接跑起来的 LangGraph 代码, 也能帮你修好跑不通的 LangGraph 代码。

- input: 一句话流程描述: 「客服消息先做分类, 投诉类转人工, 咨询类让 AI 回答」, output: 一个完整的 Python 代码文件, 里面是实现了这条流程的 LangGraph 图, 拿到就能运行
- input: 一段跑不对的 LangGraph 代码 + 报错信息或「结果不对」的描述 (如: 并行任务的结果只剩最后一个), output: 修好的代码, 附一句说明哪里错、为什么 (如: 结果列表被覆盖了, 已改为累加)
- input: 一个需求: 「我要 100 篇文章同时做摘要, 最后汇总成一份报告」, output: 带并行处理的 LangGraph 代码: 任务分发、同时执行、结果汇总, 直接可用
- input: 现有一段 LangGraph 代码, 想加功能: 「流程里加一步人工审核, 审核不过就重来」, output: 改好的代码, 新增了暂停等人工确认、确认后继续或回到上一步的逻辑
