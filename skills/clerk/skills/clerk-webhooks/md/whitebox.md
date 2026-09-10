# clerk-webhooks (`clerk/skills/clerk-webhooks`)

## whitebox

- 生成 webhook handler 代码: 第一步永远是 verifyWebhook(req) 验签, 签名不合法直接返回 400
- 验签通过后按 evt.type 匹配事件 (user.created / organizationMembership.created / subscription.* 等), 从 evt.data 提取字段
- 执行业务动作: 数据库同步、Resend 欢迎邮件、Slack 通知等, 慢任务先排队再返回
- 返回 200 OK 确认接收 (返回 2xx 即成功, 4xx/5xx 会触发 Svix 重试)
- 配套要求: 路由在 clerkMiddleware 中设为 public (否则 401); 本地用 clerk webhooks listen 建隧道, 生产换 endpoint URL 并配好签名密钥

- 验签: verifyWebhook 取自框架专属子路径 (@clerk/nextjs/webhooks、@clerk/express/webhooks 等), 自动读取环境变量 CLERK_WEBHOOK_SIGNING_SECRET (即 Svix 签名密钥) 校验签名, 任何 handler (包括纯通知类) 都不得跳过
- 类型收窄: verifyWebhook 返回 WebhookEvent 判别联合, if 匹配 evt.type 后 evt.data 自动获得对应 JSON 类型 (UserJSON、OrganizationMembershipJSON 等), 字段访问有编译期保障
- 可靠性: 事件由 Svix 投递并按固定计划重试失败消息, 以 svix-id 请求头作幂等键去重; webhook 是最终一致, 同步流程 (如注册后立刻读数据) 应改读 session token 或 Backend API
