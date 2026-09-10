# golang-observability (`samber/cc-skills-golang/golang-observability`)

## comments

- user: 后端老兵, category: 妙用, comment: 我把 PromQL 查询按惯例写在指标声明上方的注释里, 半夜出警时直接 grep 指标名就能抄查询和告警规则, 不用翻 Grafana 仓库。
- user: 第一次接手线上服务的新手, category: 坑, comment: 我在每层都 slog.Error 又把 err 往上返回, 同一条报错在日志里叠了四遍, 告警全炸。正确做法: 只 return 带上下文, 顶层记一次。
- user: 带三个服务的 SRE, category: 坑, comment: 我把 userID 塞进 Prometheus label, 指标量随用户数暴涨直接打爆内存。改成路由模板等有界值后立刻恢复, 无界值千万别当标签。
- user: 正在迁日志库的团队后端, category: 注意, comment: 从 zap 迁移别一把梭改写。先用 slog-zap 桥接让新旧共存, 逐步替换调用, 全迁完再拆桥。我硬改半周被迫回滚重来。
- user: 兼职排查线上问题的全栈, category: 注意, comment: 它是给服务常驻装观测信号的, 不做临时深挖。我拿来查一个慢函数没找到入口, 后来看说明才知道该用 golang-performance 技能。
- user: Tech Lead, category: 启发, comment: 「功能可观测才算完成」这句话让我把 PR 模板加了检查项: 指标、日志、span、告警、面板。上线后两眼一抹黑的情况基本没了。
