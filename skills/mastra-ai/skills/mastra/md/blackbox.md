# mastra (`mastra-ai/skills/mastra`)

## blackbox

**function**: 帮你用 Mastra (一套开发 AI 应用的工具) 从零搭出能跑的 AI 助手和自动化流程, 并解决过程中的一切报错。

- input: 一句话需求, 如「我要做一个能查天气、回答问题的 AI 客服」, output: 可直接运行的 TypeScript 代码 + 启动方法, 浏览器打开后能看到可视化的助手测试界面
- input: 一段报错信息, 如「Property 'memory' does not exist on type...」, output: 报错原因的通俗解释 + 改好后的代码片段
- input: 现有项目路径, 说「帮我升级到最新版」, output: 逐条需要改动的清单和改好的代码, 改完即可正常运行
- input: 「我想接 GPT-4o / 国产模型, 该怎么写?」, output: 验证过可用、名称准确的模型接入代码 (不会给你一个根本不存在的模型名)
