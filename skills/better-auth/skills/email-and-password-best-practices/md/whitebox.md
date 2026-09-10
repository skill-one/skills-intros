# email-and-password-best-practices (`better-auth/skills/email-and-password-best-practices`)

## whitebox

- 在 betterAuth({...}) 配置中开启 emailAndPassword.enabled, 注入 sendVerificationEmail / sendResetPassword 两个回调 (内接你自己的发信函数)
- 运行 npx auth@latest migrate 建好认证相关数据表
- 注册: 前端调 authClient.signUp.email (带绝对 callbackURL), 框架生成验证链接并回调 sendVerificationEmail 发信
- 用户点链接完成验证; 若开启 requireEmailVerification, 未验证用户每次登录尝试会再收到验证邮件
- 忘记密码: 调 requestPasswordReset → 触发 sendResetPassword 发出重置链接 → 用户经一次性 token 链接完成重置

- 纯配置驱动: 框架只负责生成 url/token 并回调开发者注入的发信函数, 邮件内容完全由使用方控制
- 密码哈希可插拔: 默认 Node.js 原生 scrypt (零依赖), 可注入自定义 hash/verify 换用 @node-rs/argon2 的 Argon2id; 换算法后旧哈希用户无法登录, 需规划迁移
- 安全内建: 重置 token 默认 1 小时过期、单次使用即删; 响应消息恒定 + 无效请求执行空操作防时序攻击; 邮件后台发送 (serverless 平台需配 advanced.backgroundTasks.handler 如 waitUntil); 可选 revokeSessionsOnPasswordReset 重置后吊销全部会话, 密码长度上下限可配
