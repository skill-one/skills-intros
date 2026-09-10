# developing-genkit-js (`genkit-ai/skills/developing-genkit-js`)

## blackbox

**function**: 用 Node.js/TypeScript 帮你写出能真正跑起来的 AI 应用代码 (聊天机器人、智能助手等), 并修好 AI 相关的报错。

- input: 一句话需求, 如「用 TypeScript 写一个把中文新闻标题翻译成英文的小服务」, output: 可直接运行的代码 + 简短的启动说明, 运行后输入中文标题即输出英文
- input: 一段报错的 AI 代码和错误信息 (如 404、类型错误、参数校验失败), output: 修正后的代码 + 一句话说明错在哪、为什么
- input: 对现有 Node.js 项目的需求, 如「给我的后端加一个能记住上下文的 AI 客服」, output: 在你项目里改好的代码 + 运行验证结果 (能看到 AI 实际的调用过程和回答)
