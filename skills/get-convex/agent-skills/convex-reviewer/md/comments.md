# convex-reviewer (`get-convex/agent-skills/convex-reviewer`)

## comments

- user: 从 SQL 转来的后端老兵, category: 妙用, comment: 我把 .filter() 当 SQL 的 WHERE 用, 它点破这在 Convex 里是全表扫描, 该换 withIndex, 还讲清了为什么——省掉上线后的性能雷.
- user: 第一次写 Convex 的新手, category: 坑, comment: 我在 query 里用 Date.now() 做倒计时, 页面死活不自动刷新. 审查标出这会破坏响应式, 把时间计算挪出 query 就好了.
- user: 接手遗留项目的工程师, category: 启发, comment: 跑了一遍接手的旧代码, 它抓到定时任务调的是 api.* 而不是 internal.*, 即用户端能触发管理任务. 这种藏得深的隐患人工真看不全.
- user: 赶上线的独立开发者, category: 注意, comment: 它只审 convex/ 目录里的代码, 目录外和前端逻辑不看; 而且只给结论和改法, 代码要自己动手改, 别等一键修复.
- user: 带五人小队的 CTO, category: 妙用, comment: 提 PR 前先让它过一遍, 按 Critical/Important 分级出结果, 团队评审只聊业务逻辑. 现在 Critical 清零才准合并.
- user: 做公开活动页的后端, category: 注意, comment: 点赞接口我故意不校验登录, 它照样标 Critical. 别慌, 这是「未鉴权即 Critical」的硬标准, 真要公开的接口自己判断后放行.
