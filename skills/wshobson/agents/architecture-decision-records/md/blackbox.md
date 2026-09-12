# architecture-decision-records (`wshobson/agents/architecture-decision-records`)

## blackbox

**function**: 把技术团队的重要决策 (选了什么技术、为什么这么选、有什么后果) 整理成一份结构清晰的决策记录文档，让半年后甚至新来的人都能看懂当时为什么这么做。

- input: 一段话描述决策背景, 如「我们在给电商项目选主数据库, 纠结 PostgreSQL 还是 MongoDB」, output: 一份完整的决策记录文档: 包含背景、各候选方案的优劣对比、最终结论、选定后的正负面影响, 以 .md 文件交付
- input: 一份旧的决策文档, 加一句「这个方案要淘汰了」, 如「我们不再用 MongoDB 存用户资料了」, output: 一份新的替代决策文档: 写明废弃旧方案的原因、与旧文档的对应关系, 以及分阶段的数据迁移计划
- input: 一个存满历次决策记录的文件夹路径, output: 一份总索引 (README): 表格列出每条决策的编号、标题、当前状态 (生效中 / 已废弃 / 已被取代) 和日期, 方便新成员快速了解项目决策史
