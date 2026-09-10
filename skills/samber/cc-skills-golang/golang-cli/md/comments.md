# golang-cli (`samber/cc-skills-golang/golang-cli`)

## comments

- user: 运维老哥, category: 坑, comment: 之前生成的工具没设环境变量前缀, 线上机器本来就有个 PORT 变量, 工具悄悄读错端口, 排查一下午。现在第一句就要求所有环境变量带 MYAPP_ 前缀。
- user: 后端老兵, category: 妙用, comment: 日志走 stderr、结果走 stdout 的纪律最值钱: `myapp list | jq` 管道不脏, 再加 --output json, 一个内部小工具直接变成脚本里的积木。
- user: 第一次用的新手, category: 坑, comment: 没设 SilenceUsage 时, 敲错一个 flag 就刷一整屏帮助文档, 还以为程序崩了。让 AI 补上后, 报错只剩一行原因, 瞬间清爽。
- user: CI 流水线维护者, category: 注意, comment: 拿到生成的 CLI 先验证退出码: 成功 0、参数错 2。我接手过一个工具永远返回 0, 流水线挂了照样绿灯, 按约定改完才敢进 CI。
- user: 开源小工具作者, category: 妙用, comment: version 用 ldflags 从 git tag 注入后, 用户报 issue 附的版本号就是精确提交, 再没出现"你用的哪个版本"的扯皮。
- user: 从 Python 转来的 Gopher, category: 启发, comment: 以前配置全靠 if-else 手工合并, 优先级经常写反。看到 flag > 环境变量 > 配置文件 > 默认值 这套分层后, 我把老项目也照着重构了一遍。
