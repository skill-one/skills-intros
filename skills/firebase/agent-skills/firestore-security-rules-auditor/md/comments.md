# firestore-security-rules-auditor (`firebase/agent-skills/firestore-security-rules-auditor`)

## comments

- user: 第一次上线 App 的新手, category: 注意, comment: 要贴的是 rules 规则文本, 不是 Firebase 初始化配置。报告输出 JSON, score 共 5 档, 拿到 3 分以下先别急着上线。
- user: 独立开发者, category: 坑, comment: 只贴了一个集合的规则去审, 覆盖不了全库。把完整 rules 文件整个贴进去, 它才能发现跨集合打洞的路径。
- user: 后端老兵, category: 妙用, comment: 我用 diff() 限了可改字段, 以为很稳。它指出没配 ownership 校验, 任何登录用户都能改别人文档, 这点网上很少有人讲透。
- user: 接外包的全栈, category: 妙用, comment: 按报告把 update 补上和 create 一致的校验, 再贴回去复审, 两轮 score 从 2 到 5, 相当于白嫖一轮红队测试。
- user: 两人小团队的 CTO, category: 启发, comment: 以前规则能跑就行。现在写完按它六项过一遍: create/update 对齐、字段限类型限长度, 评审时心里有底多了。
- user: 安全爱好者, category: 注意, comment: 报告对硬编码管理员邮箱不扣分, 前提是同时校验了 email_verified。看到 5 分别慌, 先确认这条真的满足。
