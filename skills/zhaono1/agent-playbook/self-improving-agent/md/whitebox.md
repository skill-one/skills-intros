# self-improving-agent (`zhaono1/agent-playbook/self-improving-agent`)

## whitebox

- 捕获信号: 把一次失败/纠正/成功压缩成最小化、脱敏的可复用摘要+证据标签, 经 apb CLI 存入本地数据目录
- 评估可复用性: 检查是否描述未来行为、是否跨任务有用、是否与权威规则冲突、是否存在窄职责 owner 和可验证路径
- 验证: 为候选设计最小的可证伪验证, 编码为可执行 eval 工件, 用 apb self-improve eval 实际运行
- 裁决与应用: 用 review 记录 validate/reject; 若 apply, 先生成行为变更提案 (BEP), 只改动一个持久 owner 并记录 change-ref
- 证明闭环: 应用后重跑代表性任务, 报告候选状态、证据、owner、eval 结果哈希和回滚路径; 行为没变则回退/拒绝

- 状态机收敛: 每次运行必须以 7 种显式终态之一结束 (candidate/validated/applied/rejected/superseded 或 rolled_back/no-delta/open-question), 且 validate 只接受针对同一候选、由 CLI 生成的通过性 eval 结果, 工件存在≠行为已改进
- 证据分层+隐私边界: 捕获时只存脱敏事实 (不复制对话记录/凭据/私有路径/客户数据); 候选类型映射到不同最小证明 (提示词规则→代表场景+评分标准, CLI 行为→聚焦自动化测试, 安全规则→反向测试, 重复启发式→多独立事件), 改 owner 前强制生成含验收标准/回滚方案的提案文档
- 外部依赖: apb / agent-playbook CLI 负责存储与裁决, 数据落在 ~/.agent-playbook/self-improvement/ (可用 AGENT_PLAYBOOK_DATA_DIR 或 --data-dir 覆盖); Claude Code 失败钩子仅在显式 apb init --hooks 后生效, 其他宿主 (Codex/Gemini/DeepSeek) 分发可用但运行时接线未经证实前标为 unverified; Markdown 导出 (apb self-improve export) 只是不回流事实的导出终点
