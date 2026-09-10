# email-and-password-best-practices (`better-auth/skills/email-and-password-best-practices`)

## comments

- user: 第一次用的新手, category: 坑, comment: 开了 requireEmailVerification 却没先配 sendVerificationEmail, 结果全站用户登录被拒。先配好发信函数再开这开关, 顺序别反。
- user: 前端小哥, category: 坑, comment: callbackURL 图省事写相对路径, 本地一切正常, 前后端分域名上线后验证链接全跳错页。必须写带 https:// 的完整地址。
- user: Vercel 部署党, category: 注意, comment: serverless 部署忘配 advanced.backgroundTasks, 重置邮件时有时无——函数一返回发送任务就被掐, 记得接平台自己的 waitUntil。
- user: 维护老系统的后端, category: 注意, comment: 想从默认 scrypt 换 Argon2id 先停手: 老用户密码是旧算法哈希的, 直接换全站登不上。要么渐进迁移, 要么引导重置。
- user: 后端老兵, category: 妙用, comment: 忘记密码接口对不存在的邮箱也返回同样响应还做假操作, 前端直接统一话术"若存在将收到邮件", 撞库探测不出账号。
- user: 接外包的全栈, category: 妙用, comment: 用户反馈密码疑似泄露, 我开 revokeSessionsOnPasswordReset, 重置后所有设备强制下线, 省了手写清 session 的代码。
