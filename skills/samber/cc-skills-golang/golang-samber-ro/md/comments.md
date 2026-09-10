# golang-samber-ro (`samber/cc-skills-golang/golang-samber-ro`)

## comments

- user: Go 十年后端, category: 妙用, comment: 两个接口轮询用 CombineLatest 合流, 替掉了原来 80 行 select+channel 样板, 连重试都是一行 Retry 的事。
- user: 第一次用的新手, category: 坑, comment: 用 ro.OnNext() 订阅, 错误全被静默吞掉, 线上丢数据都没报警。换 NewObserver 写全三个回调才看到 onError。
- user: 运维老哥, category: 坑, comment: 定时轮询的无限流没加 TakeUntil 也没 Unsubscribe, pprof 里 goroutine 一路涨。上线前务必给流绑停止信号。
- user: RxJS 转来的前端, category: 注意, comment: 冷 Observable 每个订阅者都重跑一遍源逻辑, 我订阅两次请求就发两次。要多方共享就上 Share 或 Subject。
- user: 天天写单测的后端, category: 妙用, comment: 测管道别再手写 channel 加超时了, ro.Collect() 阻塞拿 []T 和 err, 一行断言收工, 测试代码少一半。
- user: 小团队技术负责人, category: 启发, comment: 最值的是「何时别用 ro」那张表: 有限切片老实用 lo, ro 只留给事件流。帮我省掉一轮过度设计。
