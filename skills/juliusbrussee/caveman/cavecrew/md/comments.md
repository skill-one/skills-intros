# cavecrew (`juliusbrussee/caveman/cavecrew`)

## comments

- user: 后端老兵, category: 妙用, comment: 范围广就并行: 一条消息同时派 2-3 个 investigator, 分别查定义、调用方、测试, 三份结果加起来还没一次 Explore 的长文费 token。
- user: 第一次用的新手, category: 坑, comment: 我让 reviewer '给点整体建议', 它只回了一列 bug 加计数。它不评架构, 想听'该不该这么改'得换原版 Code Reviewer。
- user: 独立全栈开发者, category: 坑, comment: 五文件重构我串了 investigator→builder, 直接回 `too-big.`, 白跑一轮。超过两个文件别走这套链路, 回主线程自己动手。
- user: 运维老哥, category: 妙用, comment: 输出全是 path:行号 打头、符号带反引号, 拿 `path:\d+` 一把 grep 就能核对行号、二次过滤, 定位结果直接当索引用。
- user: 前端萌新, category: 注意, comment: 没定位就派 builder 是反效果: 得喂它一堆上下文, 反而更费。先 investigator 拿到 path:line 再派工, 已知位置可跳过定位直接改。
- user: 开源维护者, category: 启发, comment: 每次委派省几百 token, 一天几十次就是一整个会话的寿命。现在派活前我都自问: 要结论还是散文? 要结论一律 cavecrew。
