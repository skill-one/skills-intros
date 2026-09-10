# clerk-nextjs-patterns (`clerk/skills/clerk-nextjs-patterns`)

## whitebox

- 接任务后先核对前提：环境变量 CLERK_SECRET_KEY / NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY 是否具备（手动验 JWT 时还需 CLERK_JWT_KEY 或 CLERK_PEM_PUBLIC_KEY）
- 按「What Do You Need?」路由表把任务归类（服务端/客户端鉴权、中间件策略、Server Actions、API 路由、缓存），定位到对应 references/*.md
- 查 package.json 里的 SDK 版本，判断是否要走「Core 2 ONLY」降级写法
- 套用加载到的模式改造代码：服务端用 await auth()，客户端用 useAuth()/useSession()，对外部 API 用 getToken({template}) 取自定义 JWT
- 对照 Common Pitfalls 症状表逐项自检：漏 await、中间件 matcher 缺失、缓存 key 少 userId、Server Action 未鉴权、401/403 混用

- 路由表分发：skill 本体是索引，按任务类型映射到 5 份参考文档（server-vs-client、middleware-strategies、server-actions、api-routes、caching-auth）按需取用，不全文展开
- 版本门控：「Core 2 ONLY (skip if current SDK)」标注块做新旧 SDK 差异切换——旧版用 !!userId / <SignedIn>+<Protect>，当前版用 isAuthenticated / sessionStatus / <Show>
- 外部依赖与校验：全部能力来自 Clerk SDK——@clerk/nextjs/server 的 auth()（必须 await）、@clerk/nextjs 的 hooks、@clerk/backend 的 verifyToken（无中间件的独立 API 服务手动验 JWT，自动校验 exp/nbf）；JWT 模板 (Hasura/Supabase) 需在 Clerk 后台预先定义；允许的工具只有 WebFetch（拉官方文档 clerk.com）
