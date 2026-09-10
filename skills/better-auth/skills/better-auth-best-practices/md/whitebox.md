# better-auth-best-practices (`better-auth/skills/better-auth-best-practices`)

## whitebox

- 定位文档版本: 用户指定 → 查 lockfile/package.json 中的 better-auth 版本 → 有 MCP 则 get_doc /llms.txt 解析, 否则访问 better-auth.com/llms.txt 找匹配版本索引
- 安装 better-auth 并写入 BETTER_AUTH_SECRET (≥32字符) 与 BETTER_AUTH_URL 环境变量; 仅当环境变量缺失时才在配置里写 baseURL/secret
- 创建 auth.ts (数据库适配器 + emailAndPassword/socialProviders/plugins 等配置) 并为框架挂路由处理器, CLI 会在 ./、./lib、./utils、./src 下寻找它
- 按 ORM 选迁移路径: 内置适配器跑 npx auth@latest migrate; Drizzle 用 generate 生成 auth-schema.ts 后 drizzle-kit push/migrate; Prisma 生成进 schema.prisma 后 prisma migrate dev
- 校验: 请求 GET /api/auth/ok, 返回 { status: "ok" } 即主流程完成; 新增/修改插件后需重跑迁移命令

- 版本锁定机制: 文档与代码版本强绑定, 通过 lockfile → package manifest → Better Auth MCP (get_doc/search_docs) → 官方 llms.txt 的降级链确定要查的文档标识符, 避免跨版本 API 不匹配
- 数据库适配层: 直连方式接收 pg.Pool / mysql2 / better-sqlite3 / postgres.js / Neon serverless 连接实例; ORM 方式走 better-auth/adapters/{drizzle,prisma,mongodb}; 关键校验点是配置用 ORM 模型名 (如 modelName: "user") 而非底层表名 (users)
- 会话存储优先级链: 定义了 secondaryStorage (如 Redis/KV) 则会话进外部存储 → 否则进数据库 (可设 storeSessionInDatabase) → 无数据库时靠 cookieCache (compact/jwt/jwe 三种策略) 实现完全无状态; 外部依赖工具: better-auth CLI (migrate/generate/mcp)、drizzle-kit、prisma migrate
