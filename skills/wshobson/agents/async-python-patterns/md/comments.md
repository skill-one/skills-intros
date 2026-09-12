# async-python-patterns (`wshobson/agents/async-python-patterns`)

## comments

- user: 第一次碰异步的后端新人, category: 坑, comment: 在 async 函数里写了 time.sleep,10 个任务直接排队串行,换回 await asyncio.sleep 才真正并发。
- user: 自学转行的爬虫开发, category: 坑, comment: 忘写 await 不报错,拿到的是个 coroutine 对象,打印才发现函数根本没跑。IDE 的灰色警告别无视。
- user: 十年后端老兵, category: 妙用, comment: 批量调下游接口时用 gather(..., return_exceptions=True),失败不炸全场,之后统一筛出 Exception 重试。
- user: 独立开发者, category: 注意, comment: 拿 asyncio 跑图片压缩这种 CPU 活,比同步还慢。它只救网络/磁盘等待,CPU 密集请用 multiprocessing。
- user: 运维老哥, category: 注意, comment: 调第三方接口务必套 asyncio.wait_for 设超时,否则对方一挂,连接池被拖死,整站接口跟着全超时。
- user: 测试工程师, category: 启发, comment: 配 pytest-asyncio 后,超时、取消、清理逻辑都能写成确定性单测,补偿代码终于敢直接上生产了。
