# golang-concurrency (`samber/cc-skills-golang/golang-concurrency`)

## comments

- user: 十年Go后端, category: 启发, comment: 以前随手 go func 一把梭, 现在开 goroutine 前先过它的清单: 怎么退出、能不能被等、channel 谁来关, 写代码的顺序整个变了。
- user: 第一次用的新手, category: 坑, comment: 我在消费端用完就 close 了 channel, 生产方还在往里写, 直接 panic。只有发送方才能关, 让它生成代码时都标 chan<- 方向, 编译期就能防。
- user: 技术负责人, category: 妙用, comment: 同事 PR 加了个后台 goroutine, 我切 Review 模式只盯 diff, 它指出没传 context 根本停不下来, 我照着意见留评论, 十分钟审完。
- user: 高并发业务开发, category: 妙用, comment: 热点 key 过期瞬间几百请求同时回源, 它给改成 singleflight 去重, 同一 key 只打一次下游, 回源 QPS 直接掉了一个量级。
- user: CI工程, category: 注意, comment: 本地测试全绿, 线上偶发数据错乱。它提醒我 CI 里必须加 go test -race, 加上当场抓出一个计数器竞态, 裸跑真的测不出来。
- user: 运维老哥, category: 注意, comment: 两个前提: 先确认机器上 go 命令能跑; 它是写和审代码的, 程序已经卡死要查现场, 得换 golang-troubleshooting 那个技能。
