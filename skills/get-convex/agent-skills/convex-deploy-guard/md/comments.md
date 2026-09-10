# convex-deploy-guard (`get-convex/agent-skills/convex-deploy-guard`)

## comments

- user: 独立开发者, category: 坑, comment: 改完代码 deploy 三次线上都没变, 以为是网络问题瞎重试。其实命令打到了另一个 personal dev。先看目标再动手, 别学我硬重试。
- user: 第一次用的新手, category: 注意, comment: 说了一次'只读', 整个会话都改不了东西, 中途想补数据也不行, 这是故意的。动手前想清楚要不要只读, 模式中途解不了锁。
- user: 兼职运维, category: 妙用, comment: 帮客户查线上问题只开只读权限, prod 的日志数据随便看, 物理上就改不了。'看'和'改'分开授权, 终于睡得着觉。
- user: 技术负责人, category: 启发, comment: '我以为部署到哪'和'实际部署到哪'是两回事。现在团队每次部署前先播报目标, 出事能立刻对上号, 排查时间砍半。
- user: 后端老兵, category: 注意, comment: 上周批过 prod 操作, 这周直接让跑被拦下要求重新确认。起初嫌烦, 后来想通: 旧授权基于过期信息, 每次重问是对的。
- user: 接外包的自由职业者, category: 妙用, comment: 同时维护 4 个客户的 Convex 项目, 开工第一件事让它识别并播报当前目标, 按客户名核对再干活, 再没把数据推串过环境。
