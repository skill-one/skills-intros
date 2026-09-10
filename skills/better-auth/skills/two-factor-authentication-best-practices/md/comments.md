# two-factor-authentication-best-practices (`better-auth/skills/two-factor-authentication-best-practices`)

## comments

- user: 独立全栈开发者, category: 妙用, comment: 我在验证码框下加了个「记住这台设备」勾选，勾上就传 trustDevice: true——信任 30 天且每次登录都会刷新，活跃用户几乎再也见不到验证码页。
- user: 第一次写登录页的新手, category: 坑, comment: 我漏查了 onSuccess 里的 twoFactorRedirect，开 2FA 的用户看似登录成功，请求却全 401。它为 true 就得跳 /2fa 验证页，验证过才会发会话。
- user: 后端老兵, category: 注意, comment: 只有邮箱+密码注册的账号能开 2FA，走 Google 登录的用户调 enable 直接报错。我把设置页入口对非密码账号隐藏了，免得用户点进去撞一脸报错。
- user: 安全合规审查员, category: 注意, comment: 审计时我特意显式配了 storeOTP: "hashed"，备份码默认已是加密存储。别让验证码明文躺在数据库里，这行配置一行代码的事，上线前一定检查。
- user: QA 自动化测试, category: 坑, comment: 自动化脚本并发打 2FA 接口，被内置限流（10 秒 3 次）掐了，报错长得像验证码错误，排查半天才发现。把验证类请求串行、拉开间隔就正常了。
- user: 自由职业接活侠, category: 注意, comment: 密码过了只是拿临时 cookie，默认 10 分钟。有用户去邮箱翻验证码磨蹭超时，一提交被踢回登录页。我把 twoFactorCookieMaxAge 调大并提示别关页面。
