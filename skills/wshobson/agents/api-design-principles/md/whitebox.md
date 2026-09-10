# api-design-principles (`wshobson/agents/api-design-principles`)

## whitebox

- 识别任务是否命中触发场景: 设计新 API、评审规范、制定团队标准、REST↔GraphQL 迁移等
- 按范式套用核心概念: REST 走资源导向 + HTTP 方法语义 (GET/POST/PUT/PATCH/DELETE), GraphQL 走 schema-first (Query/Mutation/Subscription)
- 判断 SKILL.md 导航层是否够用, 不够时读取 references/details.md 获取详细模式与示例
- 用 Best Practices 落地设计: REST 侧 (命名/无状态/状态码/版本化/分页/限流/文档), GraphQL 侧 (防 N+1/游标分页/结构化错误/@deprecated)
- 对照 Common Pitfalls 自查 (过度取数、破坏性变更、限流缺失、忽略 HTTP 语义、紧耦合等) 后输出方案

- 场景路由机制: 以 'When to Use This Skill' 的七类场景做触发判定, 再按任务范式分流到 REST 或 GraphQL 知识分支
- 分层知识加载: SKILL.md 只作导航层, 深度内容 (详细模式与实例) 按需懒加载 references/details.md, 不全量展开
- 清单式校验: 输出前用 Best Practices 与 Common Pitfalls 双清单核对; 本技能为纯知识规则驱动, 无外部工具/库/模型 API 依赖
