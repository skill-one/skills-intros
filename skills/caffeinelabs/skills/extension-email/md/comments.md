# extension-email (`caffeinelabs/skills/extension-email`)

## comments

- user: 第一次用的新手, category: 坑, comment: 我拿它发注册验证码，结果发现验证类邮件明确不支持，这是订单确认、通知这类事务邮件专用的。验证码得另找方案，别像我一样白搭半天。
- user: 免费版尝鲜用户, category: 注意, comment: 它要求 plus 或 pro 订阅，我免费套餐装好依赖一调用就失败。上手前先确认自己的套餐档位，免得白折腾。
- user: 前端转全栈, category: 坑, comment: 照示例传了带 \n 的纯文本，收件箱里全挤成一行。参数名叫 htmlBody，换行要用 <br> 或 <p>，别用 \n。
- user: 社群运营者, category: 妙用, comment: 给会员发到期提醒时发现：每个收件人是单独一封邮件，互相看不到对方地址。群发通知不怕泄露邮箱了，放心用。
- user: 后端老兵, category: 注意, comment: 示例里失败直接 trap 整个调用会崩。我改成把错误返回给前端，err 里有原文，打个日志就能定位失败原因。
- user: 电商小老板, category: 启发, comment: 我只会描述「客户下单后收确认邮件」，一次说清什么时间、发给谁、发什么内容三件事，一次就配好了。提需求前先想清这三点。
