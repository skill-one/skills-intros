# convex-domains (`get-convex/agent-skills/convex-domains`)

## comments

- user: 独立开发者, Cloudflare 老用户, category: 妙用, comment: 它发现我本机 flarectl 已登录, 列出命令让我确认后自动建了记录, 没碰后台。顺带知道 wrangler 根本不管 DNS, 以前一直找错工具。
- user: 第一次绑域名的新手, category: 坑, comment: 只加了 CNAME, 漏了 TXT 验证记录, 卡在验证那步半天, 还以为是平台坏了。补上 TXT 立刻通过, 两条记录缺一不可。
- user: 后端老兵, category: 坑, comment: 换完域名直接上线, OAuth 登录全挂——回调还指向旧域名。SITE_URL、ORIGIN 这些 auth 环境变量要同步改成新域名并重新发布。
- user: 运维老哥, category: 注意, comment: 解析生效要几分钟到几小时, 我两分钟没通过就反复改记录, 越改越乱。先用 dig +short 确认记录落地, 再等验证, 别手痒。
- user: 接外包活的全栈, category: 坑, comment: 裸域也照 www 填了 CNAME, 一直解析不生效, 后来才知道裸域得用 A/ALIAS 记录。它给的是每条记录的具体 host 和 value, 照抄就行。
- user: 带 passkey 登录的小团队技术负责人, category: 注意, comment: 换域名前没人提醒我: 老用户的 passkey 绑在旧域名上, 换完全登不进, 只能重设。RP_ID 和 SITE_URL 得一起改, 最好提前发公告。
