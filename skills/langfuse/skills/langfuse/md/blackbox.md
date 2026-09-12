# langfuse (`langfuse/skills/langfuse`)

## blackbox

**function**: 帮你用好 Langfuse (一款记录和评估 AI 应用运行情况的平台): 给你的 AI 应用加运行监控、查线上请求数据、管理和调试 prompt (给大模型的指令词)、搭建自动化质量评测。

- input: 一段调用大模型的代码 (如 Python 文件), output: 加好了监控埋点的同一份代码——之后每次 AI 调用的输入、输出、耗时、花费都能在 Langfuse 网页上看到
- input: 一条查询指令, 如「看看我们项目里最近一周哪些 AI 请求最慢、哪些报错了」, output: 一份具体的数据清单/报告: 列出慢请求和报错请求, 含耗时、错误原因、涉及的对话内容
- input: 一个关于 Langfuse 用法的问题, 如「怎么做 AI 回答质量打分?」「prompt 该放代码里还是平台上?」, output: 基于最新官方文档的准确答案 + 可直接照抄运行的示例代码
