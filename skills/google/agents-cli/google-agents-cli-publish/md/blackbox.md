# google-agents-cli-publish (`google/agents-cli/google-agents-cli-publish`)

## blackbox

**function**: 把你已经部署好的 AI agent (智能助手程序) 登记进 Google 的 Gemini Enterprise 平台, 让企业同事能直接在平台上找到并使用它; 也能帮你登记外部 MCP 服务器 (一种工具服务) 或查看/更新/删除平台上已登记的 agent。

- input: 一条注册命令, 如: agents-cli publish gemini-enterprise --gemini-enterprise-app-id projects/xxx/engines/my-app, output: 注册成功的确认结果: 你的 agent 出现在指定的 Gemini Enterprise 应用里, 同事打开平台即可对话使用; 重复执行不会产生重复条目, 只会原地更新
- input: 一段报错信息, 如注册时返回 "Session not found" 或 HTTP 403, output: 问题原因说明和对应的修复办法, 例如: 升级某个 SDK 后重新注册 / 给当前账号补上 Discovery Engine 编辑者权限
- input: 一句话请求, 如 "列出我项目里能注册的 Gemini Enterprise 应用", output: 当前项目下所有可用应用的清单 (含完整资源 ID), 你挑一个就能直接用于注册
