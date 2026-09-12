# resend (`resend/resend-skills/resend`)

## comments

- user: 第一次接邮件服务的新手, category: 坑, comment: 我直接用默认 onboarding@resend.dev 给同事发测试,全部 403。沙箱只能发给自己账号的邮箱,先验证自己的域名才能发给别人。
- user: 后端老兵, category: 坑, comment: Node SDK 报错不抛异常,我照旧套 try/catch,发送失败也静默通过,用户压根没收到。必须显式判断返回的 error。
- user: 独立开发者, category: 妙用, comment: 别用真邮箱测试。delivered/bounced/complained@resend.dev 三个地址分别模拟送达、退信、投诉,不伤发件信誉就能跑通全流程。
- user: 管告警邮件的运维老哥, category: 注意, comment: 服务超时自动重试,用户收到两封密码重置邮件。后来每次发信都带 idempotencyKey 如 reset-pw/用户ID,重试就只发一次。
- user: 做自动回复的全栈, category: 坑, comment: 以为 webhook 推送里带邮件正文,解析半天全是元数据。要拿 email_id 再调一次 receiving.get() 才有内容,别白折腾。
- user: 前端转全栈, category: 注意, comment: 我曾在浏览器端直接调 API,全被 CORS 拦截,密钥还暴露在页面里。必须由自己服务端转发,密钥只放环境变量。
