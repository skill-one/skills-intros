# gemini-api-dev (`google-gemini/gemini-skills/gemini-api-dev`)

## blackbox

**function**: 你说想要一个用到 Gemini AI 的程序, 我直接交付能跑的 Python / TypeScript 代码 (填上密钥就能运行)。

- input: "帮我写个脚本: 我贴一段长文, 它用 Gemini 总结出 3 个要点" → , output: 一个可直接运行的 .py 文件 + 运行说明, 跑起来后终端里输出 3 条要点
- input: "我要一个客服聊天机器人, 得记住之前聊过的内容" → , output: 多轮对话的完整代码, 连续提问 "我叫什么?" 也能答对, 而不是每次都失忆
- input: "我的旧代码报错说 gemini-1.5-pro 已弃用, 帮我修" → , output: 改好的新代码, 模型换成当前可用的版本, 并附一句改动说明
