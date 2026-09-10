# vercel-composition-patterns (`vercel-labs/agent-skills/vercel-composition-patterns`)

## whitebox

- 识别触发场景:任务涉及 boolean prop 堆积的组件重构、组件库设计、复合组件 / context provider 架构,或 React 19 API 变更
- 按优先级表选规则:先查 Quick Reference,优先套用 HIGH 级 Component Architecture 规则 (architecture-),再依次看 state- / patterns- / react19- 三组 MEDIUM 规则
- 读规则细则:打开 rules/<规则名>.md,获取该条规则的原因说明 + 错误代码示例 + 正确代码示例 + 补充上下文
- 应用组合式改法:去 boolean props 改复合组件、状态提升到 provider、用显式变体替代布尔模式、children 替代 render props
- 需要全量规则时查编译版全文 AGENTS.md 收尾

- 规则索引 + 优先级驱动:能力来自 Quick Reference 列出的 8 条具名规则,分 4 类 (architecture / state / patterns / react19),严格执行 HIGH → MEDIUM 的优先顺序,不自由发挥
- 正反代码对照改造:每条规则文件固定结构为『为什么重要 / 错误示例 / 正确示例 / 补充上下文』,重构以错误→正确的前后对照为准绳
- React 19 版本门控 + 零外部依赖:react19- 组规则 (弃用 forwardRef、用 use() 替代 useContext()) 仅在 React 19+ 生效,18 及以下整节跳过;全程不调用任何外部工具、库或模型 API,只依赖自带的 rules/*.md 与 AGENTS.md
