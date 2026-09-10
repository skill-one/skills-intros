# observability-and-instrumentation (`addyosmani/agent-skills/observability-and-instrumentation`)

## comments

- user: 刚给服务配监控的新手, category: 坑, comment: 把 user_id 当指标 label, 一周后查询慢到超时——每个用户都是独立时间线. 改成只留 route 和 status_class, 查具体用户去日志里搜.
- user: 十年后端老兵, category: 妙用, comment: 动手埋点前先写下值班会问的3个问题, 照着挑信号. 砍掉一半原计划的日志, 出事时每条信号都答得上问题, 没有一条凑数.
- user: 运维老哥, category: 注意, comment: 新告警必须手动触发一次再上线. 我有条队列告警配错了通知通道, 三周后复盘才发现从没响过. 临时调低阈值打一发, 两分钟的事.
- user: 接手老系统的维护者, category: 坑, comment: 定时任务和手动重跑写同一个日志, 只有 runId 没标来源, 排查全靠排除法猜, 一下午没了. 各入口起点统一打 entryPoint 字段后一眼定位.
- user: 创业公司唯一工程师, category: 启发, comment: 以前日志全凭"以后可能用得上"乱记. 先写值班要答的问题再埋点, 让我明白遥测是答题工具不是日记本: 三条可查事件胜过三百行流水.
- user: 测试工程师, category: 妙用, comment: 验收新功能我要求开发在 staging 强制造一次错, 只拿 requestId 去日志里捞, 不看代码. 上次真捞出一行 [object Object], 字段没结构化.
