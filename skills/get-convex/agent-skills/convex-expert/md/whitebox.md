# convex-expert (`get-convex/agent-skills/convex-expert`)

## whitebox

- 接到涉及 convex/ 目录的编码任务后， 先读 convex/schema.ts (如存在 _generated/ai/guidelines.md 也一并读)， 摸清表结构与既有约定再动手
- 按对象形式写/改函数： 每个 query/mutation/action 都带 args + returns 校验器； 读路径一律 .withIndex(...)， 禁止 .filter() 全表扫描
- 默认用 internalQuery/internalMutation/internalAction， 仅当客户端 hook 需要才提升为 public； LLM/聊天和多步流程直接用 @convex-dev/agent 与 @convex-dev/workflow， 不手写
- 写完自验证： 先 npx tsc --noEmit 类型检查， 再推送到 deployment —— 已登录用 npx convex dev --once， 仅在 whoami 失败时才用 CONVEX_AGENT_MODE=anonymous 兜底
- 修复推送报出的所有 Schema/Returns/Argument 校验错误， 部署干净通过才算完成

- Schema 先行的索引纪律： 每个读路径先在 schema.ts 定义 .index(...)， 查询时 .withIndex(...)； 会增长的表不做无限 .collect()， 改用 .paginate()/.take(n) —— 这是 Convex 最常见的部署阻塞点
- 校验与导入硬规则： 固定取值用 v.literal， ID 用 v.id(tableName)， 往已有表加字段必须先 v.optional → 回填 → 收紧； query/mutation 从 ./_generated/server 导入， api/internal 从 ./_generated/api 导入， 导错即部署失败； mutation 不能发网络请求， 外部 IO 全在 action 里， 结果经 ctx.runMutation(internal.x.y) 落库
- 外部工具闭环： TypeScript 编译器 (npx tsc --noEmit) + Convex CLI (whoami 判登录态、 convex dev --once 推送部署)； LLM 能力依赖官方组件 @convex-dev/agent， 编排依赖 @convex-dev/workflow
