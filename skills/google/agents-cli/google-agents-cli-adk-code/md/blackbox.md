# google-agents-cli-adk-code (`google/agents-cli/google-agents-cli-adk-code`)

## blackbox

**function**: 用 Google ADK (Google 出品的 AI 智能体开发框架) 帮你写 Python 智能体代码 —— 你说清想要一个什么样的 AI 助手, 我给出能直接运行的代码。

- input: 一句话需求, 如「写一个能查天气、并建议穿什么的智能体」, output: 一个 .py 文件, 里面是定义好的智能体 (模型 + 提示词 + 查天气工具), 可直接运行
- input: 你已有的智能体代码 + 改动要求, 如「在删库这类危险操作前加人工确认」, output: 改好的代码: 危险动作执行前会先停下来等你批准
- input: 协作需求描述, 如「三个智能体串联: 先翻译→再审校→最后润色」或「多个智能体并行干活再汇总」, output: 对应的多智能体编排代码 (按顺序执行 / 并行执行 / 循环执行)
