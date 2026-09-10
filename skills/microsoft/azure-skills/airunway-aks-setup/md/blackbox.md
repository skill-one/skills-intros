# airunway-aks-setup (`microsoft/azure-skills/airunway-aks-setup`)

## blackbox

**function**: 把你的 Azure AKS 集群 (微软云上用来跑服务的容器集群) 变成一台能运行 AI 大模型的服务器 —— 从体检集群、装好 AI Runway, 到部署出第一个能真正对话的模型, 全程带你走完。

- input: 「我有一个现成的 AKS 集群, 帮我装上 AI Runway 并跑起一个模型」, output: 一份逐步状态清单 (每一步 ✓ 正常 / ✗ 缺失), 每次安装前先跟你确认再动手; 最终交付: 集群上运行就绪 (Ready) 的模型服务
- input: 「我集群里的 GPU 能跑什么模型?」, output: GPU 型号盘点结果 + 兼容性提醒 (如某些卡不支持特定精度、需要换参数) + 推荐的模型和部署方案
- input: 「把 Qwen2.5-7B 部署上去」, output: 部署完成确认 (模型 Ready) + 一次冒烟测试: 实际调用模型并拿到一条真实回复, 外加后续运维与排障建议
