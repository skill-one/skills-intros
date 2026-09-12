# langchain-fundamentals (`langchain-ai/langchain-skills/langchain-fundamentals`)

## blackbox

**function**: 帮你写出「会动手干活的 AI 助手」代码：让 AI 能查数据、做计算、记住聊过的话，并在危险操作前先问你一声。

- input: 「帮我写一个能查天气/搜索资料的 AI 助手」, output: 一份可直接运行的 Python 或 JS 代码文件，AI 能实际调用工具回答『巴黎今天天气怎么样』这类问题
- input: 「我的机器人聊两句就忘事，要能记住上下文」, output: 带记忆功能的机器人代码：第二次对话问『我叫什么』，它还能答出你上一轮说过的名字
- input: 「AI 执行删库、转账这类操作前，必须让我人工点头」, output: 加入人工确认环节的代码：AI 要做危险动作时会暂停，等你批准后才继续
- input: 「我想让 AI 从一段文字里提取姓名、邮箱、电话，格式要规范」, output: 结构化提取代码：输入一段文本，得到干净的字段化数据（如 {姓名: …, 邮箱: …}），而不是一大段啰嗦的话
