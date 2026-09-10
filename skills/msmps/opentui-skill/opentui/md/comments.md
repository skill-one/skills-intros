# opentui (`msmps/opentui-skill/opentui`)

## comments

- user: 前端 React 老手, category: 坑, comment: 我照网页习惯写 <text bold>,样式死活不生效。这里文本样式要用嵌套标签,别传 props。对照 text-display 文档改完就好了。
- user: 第一次用的新手, category: 坑, comment: bunx create-tui my-app -t react 直接报错。参数必须放项目名前面:bunx create-tui -t react my-app,顺序反了不认。
- user: 独立开发者, category: 妙用, comment: 没想到终端能直接摆 PNG/GIF 和二维码。我把部署面板做成 TUI,告警时同事扫码直达日志页,不用再甩链接。
- user: 运维老哥, category: 妙用, comment: @opentui/ssh 把整个面板挂在 SSH 上,服务器端零安装。手机连进去也能看监控界面,现场救火太好用了。
- user: Node 后端, category: 注意, comment: 先装 Bun 再跑,底层还有 Zig 原生构建,纯 Node 环境起不来。只是想要键位绑定的话,@opentui/keymap 无 FFI,Node 可用。
- user: CLI 工具作者, category: 启发, comment: 以前全靠手拼 ANSI 转义码,现在按写网页的思路组织布局和组件,老 CLI 一下午改成带滚动和快捷键的交互面板。
