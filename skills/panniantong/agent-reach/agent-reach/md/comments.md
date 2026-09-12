# agent-reach (`panniantong/agent-reach/agent-reach`)

## comments

- user: 做竞品调研的市场人, category: 启发, comment: 以前调研就搜索引擎一把梭，现在先拆问题：找吐槽去 Reddit/推特，看真人用法去小红书/B站。开工前让 agent 跑趟 doctor，确认哪些平台今天可用。
- user: 第一次用的新手, category: 坑, comment: 以为 cookie 配好、doctor 全绿就能搜推特，一跑就报错。后来才知道 doctor 只查配置齐不齐、不实测；真搜索还得显式带上 auth_token 和 ct0。
- user: 独立开发者, category: 坑, comment: 抓 B 站字幕我照搬 YouTube 那套 yt-dlp，反复失败才明白 B 站不吃这套；按 video.md 的重试链换 bili-cli，一次就出。
- user: 想自动化运营的博主, category: 边界, comment: 本想让它顺手发笔记、回评论，不行——只读不写，点赞发帖都不支持。拿来看风向、扒选题很顺手，发布环节还得回自己账号手动操作。
- user: 后端老兵, category: 妙用, comment: r.jina.ai 一条 curl 就把烂排版网页转成干净文本，我当通用转 Markdown 用；Exa 先拉 10 条再挑 2、3 条深读，比逐个点开省一半时间。
- user: Reddit 重度用户, category: 注意, comment: Reddit 没有免配置通道，必须登录态：桌面用 OpenCLI、服务器用 rdt-cli。我没登录直接让它搜，白跑一趟；动手前先 doctor 确认后端。
