# developing-genkit-python (`firebase/agent-skills/developing-genkit-python`)

## blackbox

**function**: 用 Python 帮你开发接入 AI 能力 (如 Gemini) 的应用:从零写一个、给现有的加功能、或把报错修好。

- input: 一句话需求,如「用 Python 写个脚本,我问一句、Gemini 答一句」, output: 一个能直接运行的 Python 项目:代码文件 + 怎么启动的说明
- input: 粘贴一段报错信息或跑不起来的代码, output: 出错原因的一句话解释 + 修好的代码
- input: 「给我的 AI 应用加功能:流式回答 / 返回规定格式的结果 (JSON) / 让 AI 能查我自己的数据」, output: 对应功能的 Python 代码片段,可直接放进项目里用
- input: 「做个网页服务,别人发请求就能调 AI」, output: 带接口的完整应用 + 一个能在浏览器里点开调试的界面
