# nextjs-app-router-patterns (`wshobson/agents/nextjs-app-router-patterns`)

## whitebox

- 判断任务是否命中技能范围: 构建 Next.js App Router 应用、Pages Router 迁移、SSR/SSG、Server Components、数据获取优化
- 按渲染模式决策表选策略: 默认写 Server Component, 仅在需要交互 (hooks、浏览器 API) 时才标 'use client'
- 按文件约定搭建 app/ 目录: layout.tsx、page.tsx、loading.tsx、error.tsx 等各司其职, 用 loading.tsx 或 Suspense 边界兜住加载态
- 按 Quick Start 模板实现数据获取: 在 Server Component 内直接 fetch, 用 next: { revalidate } 控制缓存刷新 (ISR)
- 若导航层信息不够用, 再读取 references/details.md 获取详细模式与完整示例

- 渲染模式决策表是核心转换逻辑: 按 "在哪渲染 (服务端/浏览器) + 何时渲染 (构建时/请求时/渐进式)" 把需求映射到 Server/Client/Static/Dynamic/Streaming 五种模式
- 文件约定即路由: app/ 目录下的文件名直接决定路由结构与 UI 职责 (含 API 端点 route.ts、OG 图 opengraph-image.tsx), 无需手工配置路由表
- 靠 Do's/Don'ts 清单校验: 数据获取放在数据使用处且尽量留在服务端、Server→Client 边界只传可序列化数据、Server Component 内禁用 hooks; 依赖 Next.js 14+ 与 React Server Components 本身, 无额外外部模型或工具 API
