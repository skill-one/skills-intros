# mcp-builder (`anthropics/skills/mcp-builder`)

## blackbox

**function**: 帮你打造「AI 助手的外挂工具包」: 你说想让 AI 能操作哪个外部服务 (如查订单、建工单、管日历), 我交付一套可安装的连接服务, 让 AI 真正能读写那个系统。

- input: 一句话需求, 如「我想让 AI 能查和创建 GitHub issue」, output: 一个可安装运行的连接服务包 + 使用说明, 装好后 AI 即可直接查询、创建 issue
- input: 某外部服务的 API 文档链接 (如快递查询、内部数据库), output: 对接该服务的完整程序包, 内含一系列 AI 可调用的工具, 并附带错误提示优化和分页等细节
- input: 一份已写好的连接服务代码, output: 质量检查和测试后的代码 + 一份 10 道题的验收测试卷及标准答案, 用来验证 AI 用它答题是否可靠
