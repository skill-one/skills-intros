# cloudflare-email-service (`cloudflare/skills/cloudflare-email-service`)

## comments

- user: 第一次用的新手, category: 坑, comment: 只在 wrangler.jsonc 里加 send_email 绑定不够, 域名要先开通: `npx wrangler email sending enable yourdomain.com`. 我卡在这里半天, 报错一直指向绑定.
- user: 独立开发者, category: 坑, comment: 把 Workers 示例直接搬进 REST 接口就出错: from 用 `address` 不是 `email`, 回复字段是下划线的 `reply_to`. 两套写法字段名不同, 一定对照 REST 文档.
- user: 后端老兵, category: 妙用, comment: 用 Agents SDK 的 onEmail() + replyToEmail(), 一个 Worker 就接管收客户邮件加自动回复, 邮件服务器都不用搭, 发信走绑定连 API key 都不用管理.
- user: 运维老哥, category: 注意, comment: 联调别用编造的收件地址, 退信会拉低域名信誉, 之后真用户的邮件进垃圾箱. 用自己控制的真实邮箱测, html 和 text 两个版本都发.
- user: 做邮件机器人的开发者, category: 坑, comment: email() 处理器里先 log(message.raw) 再用 postal-mime 解析, 拿到空内容——原始流只能读一次. 先 `new Response(message.raw).arrayBuffer()` 存下来再解析.
- user: 独立开发者, category: 启发, comment: 这产品 2025 年才推出, GPT 和 Cursor 给我的 API 写法全是旧的, 一跑就报错. 遇到问题直接问官方文档最快, 新产品别信模型记忆, 先查原始来源.
