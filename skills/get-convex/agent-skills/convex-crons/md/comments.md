# convex-crons (`get-convex/agent-skills/convex-crons`)

## comments

- user: 后端老兵, category: 妙用, comment: 给任务表加了已处理标记,handler 先查再写,重复触发也不会重复扣款,定时对账终于能放心跑了。
- user: 第一次用的新手, category: 坑, comment: 我在 crons.ts 里写了 api.xxx,部署不报错但到点直接被拒,改成 internal.* 并把函数声明成 internalMutation 才正常。
- user: 运维老哥, category: 注意, comment: 上线后务必去 dashboard 的 Crons 页看调度列表,我拼错时间表达式,任务安静地一次都没跑过,没有任何报错提示。
- user: 独立开发者, category: 启发, comment: 之前每分钟轮询查新数据是错误姿势,改成订阅推送后,定时任务只留夜间清理,数据库负载肉眼可见地降了。
- user: 全栈自由职业者, category: 坑, comment: 一个 handler 里处理上万条,跑到一半和下一轮重叠了。改成每轮只处理一页、游标分批,再没出过乱子。
- user: 小团队技术负责人, category: 妙用, comment: 把日报邮件挂到清晨低峰时段,handler 只做一次聚合查询就完事,不占资源、不卡用户请求,白嫖了闲时算力。
