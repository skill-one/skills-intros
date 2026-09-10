# clerk-setup (`clerk/skills/clerk-setup`)

## whitebox

- 读 package.json, 按依赖映射表识别框架 (如 next → Next.js, expo → Expo)
- 执行 `clerk init --framework <框架>`: 安装 SDK、接线项目, 无 Clerk 账号时自动生成临时开发密钥并写入框架对应的 env 文件 (如 Next.js 的 .env.local)
- (项目已有 Clerk 应用时) `clerk auth login` → `clerk link --app` → `clerk env pull` 拉取真实密钥
- 运行 `clerk doctor --json` 做集成健康检查
- 若根目录存在 components.json (shadcn/ui), 安装 @clerk/ui 并应用 shadcn 主题

- 框架解析: 静态读取 package.json 的 dependencies, 按映射表推出框架名、SDK 包名 (@clerk/nextjs 等)、env 变量名 (Vite 用 VITE_CLERK_PUBLISHABLE_KEY, Next.js 用 NEXT_PUBLIC_*) 及 env 文件优先级 (.env.development.local > .env.local > .env)
- 依赖外部工具 clerk CLI: init/link/env pull 负责应用供给与密钥写入 (未登录走 accountless 临时应用, 登录后自动认领); 密钥轮换用 `clerk api` 直调 PLAPI (Clerk 平台 REST API), 可设旧密钥 24h 宽限避免停机
- 校验与兜底: `clerk doctor --json` 检查框架集成/env 变量/middleware/SDK 安装状态; CLI 不可用 (如沙箱环境) 时退回 WebFetch 抓取 clerk.com/docs/{framework}/getting-started/quickstart 照做, 密钥从 dashboard.clerk.com 手动获取
