# vercel-react-best-practices (`vercel-labs/agent-skills/vercel-react-best-practices`)

## whitebox

- 触发判定: 任务落在 When to Apply 五类场景之一 (写新组件/页面、实现数据获取、性能 review、重构、bundle/加载优化)
- 按优先级表定位规则: 先查 CRITICAL (async- 消除瀑布、bundle- 体积), 逐级到 LOW, 每类规则用前缀作检索键
- 读取具体规则文件 rules/<前缀-规则名>.md, 获取详细解释与代码示例
- 依据规则文件中的正确示例执行重构或代码生成, 需全量上下文时查 AGENTS.md

- 优先级路由: 70 条规则按 8 类组织, 表格内 CRITICAL→LOW 排序 + 前缀 (async-/bundle-/server-/client-/rerender-/rendering-/js-/advanced-) 直接把任务类型映射到具体规则
- 正误对照转换: 每条规则文件内置 incorrect 代码示例 (附问题解释) 与 correct 代码示例 (附修正解释), 重构时以 correct 示例为目标模式套用
- 两级知识源, 零外部依赖: 细粒度查 rules/ 单条规则文件, 全量查 AGENTS.md 编译文档; 不依赖任何外部工具、库或模型 API, 知识全部由 Vercel Engineering 维护的规范文件承载
