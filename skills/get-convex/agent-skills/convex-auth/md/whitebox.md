# convex-auth (`get-convex/agent-skills/convex-auth`)

## whitebox

- 安装 @convex-dev/auth 并在 convex.config.ts 挂载 (pnpm 需额外装 jose), 在 convex/auth.ts 定义 provider, 默认 Passkey, 除非明确要求 Password/OAuth
- 用 jose 的 node 脚本无头生成 JWT_PRIVATE_KEY + JWKS, 连同 SITE_URL 通过 Convex MCP envSet (或 NAME=VALUE 形式的 CLI) 设到部署上, 然后删除临时的 .auth-keys.json
- 手写 convex/auth.config.ts, 这个文件错了或缺失会让应用'静默始终未登录', 是头号坑
- 接客户端: 包 ConvexAuthProvider, 加登录组件和路由守卫; 若引用 shadcn/ui 原语, 先用 npx shadcn@latest add 装齐, 缺 @/components/ui/* 是硬性构建错误
- 跑一次真实登录往返验证通过, 才算完成

- 密钥生成不走交互式向导 (npx @convex-dev/auth 在无 TTY/CI 环境会挂起), 而是用 jose 以 extractable RS256 确定性生成: PKCS8 私钥换行替换为空格, JWKS 结构为 {keys:[{use:"sig", ...公钥JWK}]}
- 环境变量写入有两个防坑机制: 优先 Convex MCP envSet 每次一个变量避免 shell 转义; CLI 回退必须用 NAME=VALUE 前缀形式, 因为密钥值以 -----BEGIN 开头会被 CLI 误解析为未知 flag
- 依赖外部工具链: @convex-dev/auth (认证库), jose (密钥生成), Convex MCP/CLI (设置部署环境变量), shadcn CLI (按需安装 UI 原语); 正确性靠 auth.config.ts + 实际登录往返双重把关
