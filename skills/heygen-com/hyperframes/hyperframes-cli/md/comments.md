# hyperframes-cli (`heygen-com/hyperframes/hyperframes-cli`)

## comments

- user: 第一次做动画视频的新手, category: 坑, comment: 用中文搜 catalog 返回空,差点以为组件库是坏的。其实索引是英文的,把「标题逐行浮现」写成 "reveal headline line by line" 立刻就搜到了。
- user: 写 CI 的运维老哥, category: 坑, comment: 直接拿 doctor 的退出码当体检结果,流水线永远绿灯——它不管好坏都退出 0。CI 里要接 jq -e '.ok' 读返回体才算真把关。
- user: 笔记本没配环境的独立创作者, category: 妙用, comment: 本地没装 Chrome 和 FFmpeg 也能出片,直接 cloud render。素材大就先 --dry-run --json 查 200MB 上传上限,别盲目传一半失败。
- user: 接外包的前端工程师, category: 妙用, comment: 客户说「就改这个元素」时不用截图来回猜,preview --context --json 直接拿到他选中的元素;返回 no-selection 就请他点一下再跑。
- user: 写过自动化脚本的后端, category: 注意, comment: --on-device 要一次性下载约 33MB,必须先征得同意;脚本和 --json 模式下不会弹任何提示,得自己开口问,用户点头后记得加 -y。
- user: 从手写 CSS 动画转来的老前端, category: 启发, comment: 以前动效全手写,现在先 catalog --query 用效果描述找现成组件,多数一装就有;真没有就把结果里拼好的 report_gap 发出去,补上 --wanted 即可。
