# compress (`juliusbrussee/caveman/compress`)

## comments

- user: Claude Code 重度用户, category: 妙用, comment: CLAUDE.md 每轮对话都会读进上下文, 压一次全程省 token。把 400 行压掉一半, 命令和路径原样保留, 没坏过。
- user: 第一次用的新手, category: 坑, comment: 我直接改了压缩后的文件, 半个月后自己都看不懂。正确做法: 改 FILE.original.md, 改完再压一次。
- user: 全栈自由职业者, category: 注意, comment: 我的笔记一半是代码块, 压缩只动文字部分, 省得很少。动手前先看代码占比, 纯代码文件别指望省。
- user: 独立开发者, category: 妙用, comment: 拿 FILE.original.md 和压缩版 diff, 一眼看清自己爱写的废话词。现在我一开始就写短句, 连压缩这步都省了。
- user: 运维老哥, category: 注意, comment: 不放心, 压完逐条 diff 核对: 反引号和代码块里的 shell 命令一个字符没动, 可以放心对运维文档下手。
- user: 技术文档作者, category: 启发, comment: "建议您考虑先运行测试"被砍成"先跑测试", 反而更清楚。现在我写文档直接用祈使句, 省得回头再压。
