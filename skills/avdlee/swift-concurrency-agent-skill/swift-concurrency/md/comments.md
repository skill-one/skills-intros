# swift-concurrency (`avdlee/swift-concurrency-agent-skill/swift-concurrency`)

## comments

- user: iOS老兵, 维护五年老项目, category: 妙用, comment: Swift 6 迁移, 我本想一把全修, 它让我先修完所有 Sendable 报错、编译测试干净再碰下一类. diff 变小, review 不再是灾难.
- user: 刚学 Swift 的新手, category: 坑, comment: 我为了消报错到处加 @MainActor, 结果请求也排队在主线程, 列表滑动卡顿. 它提醒我只有真正 UI 相关的代码才配用它.
- user: 后端转 iOS 开发, category: 坑, comment: 带着 GCD 习惯往 async 函数里塞信号量等锁, 任务直接挂死. 现在共享状态全放 actor 里, 编译器帮我查线程安全.
- user: 刚用上 Xcode 26 的独立开发, category: 注意, comment: 它诊断前必先确认项目设置(语言模式、默认隔离). Xcode 26 新项目默认 MainActor, 随口答会开错药方, 这步别嫌烦.
- user: 团队技术负责人, category: 妙用, comment: 碰到 Sendable 报错我想 @unchecked 一把过, 它先让我写安全前提和移除计划. 每个逃生口都留痕, code review 终于有抓手.
- user: 爱打断点调试的开发, category: 启发, comment: 以前爱抓 Thread.current 打印找线程跳来跳去, 它教我按隔离域思考, 用 Instruments 验证实际执行, 不再玄学猜.
