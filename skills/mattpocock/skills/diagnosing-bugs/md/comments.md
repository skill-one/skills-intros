# diagnosing-bugs (`mattpocock/skills/diagnosing-bugs`)

## comments

- user: 后端老兵, category: 妙用, comment: 只在两个版本间出现的 bug, 我给了两个 commit 号, 它做差分循环对比输出, 十分钟锁定一处依赖升级, 省我一下午。
- user: 第一次独立修 bug 的实习生, category: 坑, comment: 我只转述了现象没给报错原文, 它复现出旁边另一个错, 修完主 bug 仍在。把报错和步骤一字不改贴给它才有效。
- user: 前端工程师, category: 妙用, comment: 连点三层弹窗才出现的 UI 崩溃, 它写成 Playwright 脚本断言 console 报错, 两秒跑一次; 我肉眼点了三小时都没复现。
- user: SRE 老哥, category: 注意, comment: 它不肯看堆栈就猜, 先要能跑的环境或 HAR、日志。提前备好复现环境和脱敏日志, 能少一轮来回。生产日志它会自动打码。
- user: 被 1% 概率 bug 折磨的后端, category: 启发, comment: 我的 bug 百次才现一次, 它不追干净复现, 而是把触发场景跑一百遍放大复现率再查。难的不是复现, 是复现率——想通了。
- user: 远程接活的自由职业者, category: 注意, comment: 它动手前会发来 3~5 条按概率排序的猜测让你确认。我回一句「昨天刚发过版」直接命中, 这步别晾着, 回复能省大半天。
