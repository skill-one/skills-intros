# azure-aigateway (`microsoft/azure-skills/azure-aigateway`)

## blackbox

**function**: 给你的 AI 服务 (如 Azure OpenAI) 装一扇统一的"大门" (AI 网关): 谁能访问、用量多少、花多少钱、内容干不干净, 都由这扇门把关。

- input: "把我的 Azure OpenAI 模型接到网关上, 让团队统一调用", output: 一个可直接调用的网关地址 + 一次真实对话测试的成功回执 (证明链路已通)
- input: "AI 每天账单太贵, 帮我省钱; 另外别让某个应用把额度刷爆", output: 开启语义缓存 (相似问题直接复用之前的答案, 不再重复计费) 和单应用用量上限后的网关, 账单通常省 60%–80%
- input: "有人诱导 AI 输出有害内容、绕过使用规则, 帮我拦住", output: 带内容安全过滤的网关: 危险请求被自动挡下并返回拒绝原因, 正常请求照常通过
