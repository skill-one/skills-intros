# to-spec (`mattpocock/skills/to-spec`)

## whitebox

- 前置检查: 若没拿到 issue tracker 与 triage 标签词表, 提示用户运行 /setup-matt-pocock-skills, 全程不采访用户
- 探索仓库了解代码现状, 沿用领域术语表词汇, 遵守相关 ADR (架构决策记录)
- 勾勒测试缝隙 (seam, 即测试注入点): 优先复用现有缝隙、取最高层级、数量越少越好, 并与用户确认
- 按固定模板撰写 spec: 问题陈述/方案/长编号用户故事/实现决策/测试决策/范围外/备注
- 发布到项目 issue tracker, 打上 ready-for-agent 标签, 不走额外 triage

- 只综合、不采访: 输入是当前对话上下文 + 代码库理解, 被明确禁止向用户提问, 只把已讨论内容重组为 spec
- 缝隙优先的测试设计: 测试切入点选'现有 > 新建、层级最高、全局最少 (理想 1 个)', 写入 spec 前先经用户确认这一步
- 模板硬约束: 必须套用固定模板; 用户故事为'As a... I want... so that...'句式的长列表; 禁止写具体文件路径与代码片段 (唯一例外: 原型产出的决策性代码, 如状态机/schema); 依赖外部工具: 项目 issue tracker + /setup-matt-pocock-skills 提供的词表
