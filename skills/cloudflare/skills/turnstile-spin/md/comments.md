# turnstile-spin (`cloudflare/skills/turnstile-spin`)

## comments

- user: 第一次接人机验证的新手, category: 注意, comment: 上手前先确认项目有能改的后端接口。我拿 mailto 联系表单去试，它直接说纯静态站没法放服务端校验，婉拒了。这不是 bug，是能力边界，先想清楚再雇它。
- user: 从 reCAPTCHA 迁移的后端老兵, category: 妙用, comment: 它扫代码时发现我已有的 reCAPTCHA v3，没新建 widget，直接切成迁移计划给确认。Turnstile 只返回 success 布尔值，v3 那套分数阈值调参彻底省了。
- user: 独立开发者, category: 坑, comment: widget 默认注册 localhost 方便本地调试，我图省事把生产后端的 TURNSTILE_HOSTNAMES 白名单也带上了 localhost → 线上伪造 hostname 也能过校验。生产环境必须剔除本机地址。
- user: 运维老哥, category: 注意, comment: 权限是第一道坎：wrangler login 的 OAuth 不一定含 Turnstile:Edit，别绕弯，直接去 dashboard 建自定义 token。token 走 export 进终端环境变量，它不会让你贴到聊天里。
- user: 博客个人站长, category: 启发, comment: 验证环节强制跑两遍：真 token 提交成功一次，再重放同一个确认被拒。我以前自己接验证码只测成功路径，从没想过测 token 重放。以后写安全逻辑都补上失败路径的测试。
- user: Next.js 全栈开发者, category: 注意, comment: siteverify 网络抖动时后端直接 403 拒绝，属于 fail closed，上线前想清楚业务能否接受偶尔误拒。另外所有改动都先给 diff 确认才落盘，不用怕 handler 被偷偷改。
