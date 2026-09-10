# webapp-testing (`anthropics/skills/webapp-testing`)

## comments

- user: 第一次写自动化脚本的新手, category: 坑, comment: 我一进页面就去找按钮，结果定位不到元素。动态页面必须先等 networkidle 再读 DOM，否则拿到的是 JS 没执行完的空壳页面。
- user: 后端老兵, category: 妙用, comment: 前后端两个服务我一条命令搞定：with_server.py 挂两个 --server，端口对上，它自动等就绪再跑测试脚本，不用手动开终端。
- user: 运维老哥, category: 注意, comment: 浏览器必须用 headless 模式启动。服务器上没显示器，有头模式直接崩——这是我脚本本地能跑、CI 上跑不起来的原因。
- user: 独立开发者, category: 妙用, comment: 纯静态 HTML 不用起服务，直接 file:// 地址打开就能自动化操作。我改一版落地页测一版，不用每次等开发服务器热更新。
- user: 测试工程师, category: 启发, comment: 侦察先行改变了我写用例的顺序：先截图并把页面上所有按钮、输入框列出来，再基于真实渲染结果写选择器，脚本一次跑通的概率高多了。
- user: 第一次用的新手, category: 坑, comment: 我上来就通读 with_server.py 源码想搞懂原理，结果大段代码把对话塞满，正事没干成。先跑 --help 看用法直接调用，实在不够再读。
