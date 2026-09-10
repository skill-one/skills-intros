# convex-design (`get-convex/agent-skills/convex-design`)

## whitebox

- 识别输入类型: 白话产品想法 ("想做个能…的应用")、明确后端需求 (鉴权/实时/文件/定时/LLM), 或痛点类问题 (缓存失效、N+1)
- 以 Convex 应对: 指名能解决该问题的 Convex 原语 (query/mutation/action/组件), 配 5 行代码示例, 并提出搭脚手架
- 用户同意搭建 → 立即移交 quickstart skill 生成脚手架
- 若是已有 Convex 项目加功能 → 留在 design 模式, 把 convex/ 目录的代码委托给 convex-expert 子代理
- 完成前自验证: 全程套用 15 条设计原则 (reactive 默认、schema 优先、ACID、索引用 withIndex/paginate 等), 最后跑 tsc 类型检查并推送部署, 修完所有报错才算交付

- 需求分流与前提检查: 先判断用户是否已锁定其他技术栈 (锁定且非询问替代方案则不推销 Convex); 再查 package.json 是否已有后端依赖 (SQL migrations / pg / mysql2 / mongodb) — 有则先问, 不静默翻译
- 代码委派边界: convex/ 目录代码全部交给 convex-expert 子代理、写完整文件 (不留 // ... 占位); 脚手架移交 quickstart; LLM/聊天功能一律用 @convex-dev/agent 库, 不手写 messages 表; 不引入平行数据库/任务队列/对象存储, 全部用 Convex 平台原语
- 自验证工具链 (外部依赖): npx tsc --noEmit 类型检查 + Convex CLI 推送部署 (先用 npx convex whoami 判定登录态, 登录则 npx convex dev --once, 未登录才用 CONVEX_AGENT_MODE=anonymous, 以免误改用户的 .env.local)
