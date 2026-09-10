# prisma-upgrade-v7 (`prisma/skills/prisma-upgrade-v7`)

## whitebox

- 触发: 用户提出 Prisma v6→v7 升级或遇到 v7 报错, 加载本 skill 全文作为唯一执行依据
- 前置拦截: 检查 datasource provider, 若为 mongodb 立即终止本指南, 转交 prisma-mongodb-upgrade skill (v7 无 MongoDB 连接器)
- 基础改造: 按 skill 内置命令升级 npm 包 (@prisma/client@7 / prisma@7), 定模块格式 (默认 ESM, 保 CommonJS 则 generator 设 moduleFormat="cjs"), 校验 Node 20.19+ / TS 5.4+
- 核心改写: schema generator 换成 prisma-client + 显式 output 路径, 新建 prisma.config.ts 并用 dotenv 手动加载 env, 按数据库安装 driver adapter 并注入 PrismaClient 构造函数
- 验证收尾: import 改指向生成目录, Prisma.validator 换成 satisfies, 跑 npx prisma generate (+ migrate dev), 按 Troubleshooting 处理模块找不到 / SSL / 连接超时

- 解析 = 触发词 + 场景匹配: 命中 "upgrade to prisma 7" / "prisma 7 migration" / "prisma-client generator" / "driver adapter required" 等即应用本指南; schema 含 mongodb 是唯一硬性否决分支
- 转换 = 优先级规则清单 + before/after 代码模板: 6 类规则按 CRITICAL→HIGH 排序 (schema-changes, driver-adapters, esm-support → prisma-config, env-variables → removed-features, accelerate-users), 由当前 LLM 按 "How to Use" 顺序套用 references/*.md 里的 v6→v7 代码块改写用户项目
- 校验 = 破坏性变更对照表 + 外部 CLI 实测: 用 skill 内置 v6/v7 差异表逐项核对用户现状, 最终靠 npx prisma generate / migrate dev 与 npm 包 (@prisma/client@7, @prisma/adapter-pg, dotenv 等) 跑通为准; 不调用任何外部模型 API, 全部逻辑为文本规则由 LLM 直接执行
