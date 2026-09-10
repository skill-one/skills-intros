# caveman-manage (`juliusbrussee/caveman/caveman-manage`)

## comments

- user: 第一次用的新手, category: 坑, comment: 我直接说"帮我批准这个实验", 它只给了三行建议就停了。后来明白: 它只读不执行, 连"你看着办"也不算授权。建议里的动作要自己去控制台做。
- user: 算法组评审人, category: 妙用, comment: 它说 evidence incomplete 时, 我就对照它列的字段逐个补: 样本量、guardrail、回滚原因。补齐了才肯给 approve 建议, 比人肉查漏稳多了。
- user: 值班运维老哥, category: 妙用, comment: 最好用的闭环: 它出建议→我执行→再叫它复查。它会重读服务器真实状态, 不信我口头"跑完了", 值班留痕全靠这一步。
- user: 管三个项目的中层, category: 注意, comment: 想让它跨组织查实验, 它拒绝代填组织 id——范围只认登录账号的权限。先切到有权限的账号, 再让它 list, 这步省不掉。
- user: 做汇报的数据分析师, category: 启发, comment: 以前我把实验提升数字直接写成"已验证节省"汇报, 它死活不认, 只认真实流量加供应商侧账本证据。团队汇报口径被它掰正了。
- user: 踩过回滚坑的SRE, category: 注意, comment: 它建议 rollback 后你执行, 服务器可能老实返回 cave_not_implemented。它不会把拒绝说成回滚成功——这时别干等, 走人工路径。
