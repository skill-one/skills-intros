# airunway-aks-setup (`microsoft/azure-skills/airunway-aks-setup`)

## whitebox

- 校验集群: 检查 kubeconfig 上下文、盘点节点、探测 GPU, 逐项报告 ✓/✗ 状态
- 安装控制器: 经用户确认后, 部署 AI Runway 的 CRD 与 controller
- 评估 GPU: 识别 GPU 型号, 标记 dtype/attention 约束 (如 T4/V100 不支持 bfloat16 → 用 --dtype float16)
- 选择并安装推理 provider: 从 KAITO / Dynamo / KubeRay 中推荐其一并安装
- 首次部署: 选模型 → 部署 → 验证 Ready, 收尾做冒烟测试并给出下一步建议

- Runbook 式执行, 零 MCP 工具: 按顺序逐个加载 references/steps/step-N-*.md 参考文档执行, 集群操作全部经 kubectl / make / curl 直接完成
- 状态门控 + 断点续跑: 每步校验并报告 ✓/✗, 已完成的步骤自动跳过; 支持 skip-to-step N 从指定步骤恢复; 一切安装/部署动作前强制用户确认 (含 GPU 节点池的成本确认)
- 外部依赖: 无集群时移交前置技能 azure-kubernetes 建集群 (含 GPU 节点池); 推理 provider 生态为 KAITO / Dynamo / KubeRay; 排障依赖内置 troubleshooting.md 与 azure-diagnostics 技能
