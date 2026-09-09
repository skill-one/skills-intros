# azure-aigateway (`microsoft/azure-skills/azure-aigateway`)

## whitebox

- 触发匹配: 用户请求命中触发词表 (semantic caching / token limit / content safety / MCP rate limiting / 添加 AI 后端等)
- 采集网关信息: 用 az apim show / backend list / subscription keys list 取网关 URL、已有后端和订阅密钥 (前提: APIM 实例已由 azure-prepare skill 部署好)
- 挂载 AI 后端: az cognitiveservices account list 发现模型资源 → az apim backend create 注册为后端 → az role assignment create 给 APIM 托管身份授予 Cognitive Services User 角色
- 下发治理策略: 在 <inbound> 按固定顺序写入策略: 认证 → 语义缓存查找 → token 限额 → 内容安全 → 后端选择/负载均衡 → 指标上报
- 验证: curl 打网关的 /openai/deployments/<deployment>/chat/completions 端点, 按 429/无缓存命中/401 等已知症状表排障

- 执行通道只有 Azure CLI (az): 所有查询与变更都是 az apim / az cognitiveservices / az role assignment 命令; 测试用 curl + Ocp-Apim-Subscription-Key 请求头
- 治理能力 = APIM 策略 (XML policy) 组合, 顺序固定: 认证 → 语义缓存 → token 限额 → 内容安全 → 后端选择 → token 指标; 模板来自本地 references/policies.md 与 patterns.md, 不现场编造
- 排障走已知症状映射: 429→调大 tokens-per-minute 或加负载均衡; 缓存不命中→score-threshold 降到 0.7; 内容误判→调高类别阈值(5-6); 401→授予 Cognitive Services User 角色 (细节在 references/troubleshooting.md)
