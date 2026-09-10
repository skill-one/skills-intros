# entra-agent-id (`microsoft/azure-skills/entra-agent-id`)

## blackbox

**function**: 帮你在微软 Entra (微软的企业账号与权限体系) 里为 AI 智能体开设专用身份, 并交付让它们能安全登录、按需调用微软服务 (如 Outlook、Teams、Graph) 的可直接运行的认证代码。

- input: 一段需求, 如: 「我有 3 个客服 AI 助手, 想让每个助手有自己独立的身份, 各自只能读邮件发邮件」, output: 可一键运行的创建脚本 + 操作说明; 执行后租户里出现 3 个独立身份, 每个已配好邮件收发权限, 出了问题能定位到具体哪个助手
- input: 一段报错信息, 如: 「AADSTS700211: No matching federated identity record found」, output: 用人话讲清错在哪 (如登录指向了错误的租户) + 改好的参数/代码, 照做即可跑通
- input: 技术栈描述, 如: 「我的 agent 用 Python 写, 部署在容器里, 需要以某个用户的名义代他操作日历」, output: 适配该场景的接入方案与代码: 部署配置 + 调用示例, agent 拿到就能替用户安全地读写日历
