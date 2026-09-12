# rust-async-patterns (`wshobson/agents/rust-async-patterns`)

## comments

- user: 后端老兵, category: 妙用, comment: 给任何请求套超时的土办法: 把请求和 tokio 的 sleep 一起塞进 select! 赛跑, sleep 先完成就返回超时, 不用自己起定时器。
- user: 第一次用的新手, category: 坑, comment: 在 async 函数里顺手写了 std::thread::sleep, 整个服务像死机。换成 tokio 的 sleep 才明白: 普通睡眠会堵死整个运行时。
- user: 运维老哥, category: 注意, comment: 上线前记得先初始化 tracing-subscriber, 不然任务挂起时日志里看不出卡在哪个 await, 排障基本靠猜。
- user: Java 转 Rust 的, category: 坑, comment: 把 std::sync::Mutex 的锁跨过 await 还没放, 直接卡死。要么在 await 前 drop 锁, 要么换 tokio::sync::Mutex。
- user: 并发服务开发者, category: 坑, comment: tokio::spawn 报 future cannot be sent, 查了半天是跨 await 用了 Rc, 换成 Arc 就编译通过。看到这个报错先查 Send。
- user: 重构爱好者, category: 启发, comment: 原来用 Arc<Mutex> 共享计数器到处加锁, 照着「传消息代替共享状态」改成 mpsc channel, 代码短了一截, 也没锁竞争了。
