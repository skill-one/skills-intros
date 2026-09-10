# remotion-studio (`remotion-dev/skills/remotion-studio`)

## comments

- user: 第一次用 Remotion 的前端实习生, category: 坑, comment: 命令几秒就退出, 我以为失败重跑了三遍。其实是项目已有 Studio 在跑, 打印 URL 后就退出, 复制链接打开即可, 别重跑。
- user: 接外包的独立开发者, category: 妙用, comment: 加 --port=3000 固定端口后, 给客户的预览链接永远不变, 换机重启都一样, 再也不用每次重发新地址。
- user: 运维老哥, category: 注意, comment: 它是常驻进程, 不是跑完就退, 终端一关预览就断。我扔进 tmux 挂后台, 断线重连预览还在。
- user: 转行做动效的设计师, category: 坑, comment: --no-open 表示不会自动弹浏览器, 我第一次盯着终端干等, 以为卡死了。URL 就在输出里, 自己复制到浏览器打开。
- user: 后端老兵, category: 妙用, comment: 旧实例卡住不用找进程去杀, 直接 --force-new --port=3010 再起一个干净的, 新旧对比着用, 互不干扰。
- user: 教 React 动效的讲师, category: 启发, comment: 「已在跑就打印 URL 秒退」这个行为被我写进课堂启动脚本: 秒退就提示学生直接开已有预览, 再没人重复起服务。
