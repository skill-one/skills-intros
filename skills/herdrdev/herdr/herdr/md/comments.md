# herdr (`herdrdev/herdr/herdr`)

## comments

- user: 第一次用的新手, category: 坑, comment: 想看用法直接敲 herdr, 结果整屏 TUI 给我弹出来。要看命令得敲 herdr --help, 再像 herdr pane 这样单独敲子命令组逐个看。
- user: 后端老兵, category: 妙用, comment: agent 在备用屏上跑, 输出怎么加 --lines 都读不全。后来让它把完整回复写成 /tmp 下的 md 文件, 我直接读文件, 一次搞定。
- user: 运维老哥, category: 注意, comment: machine list 只是连接配置清单, 不是跨机器的面板列表。w1:p1 在两台机器上都存在, ID 不通用, 远程操作前要在那台机器上重新查一遍。
- user: 独立开发者, category: 妙用, comment: 用 split --no-focus 在旁边开个 pane, pane run 跑测试, wait-output 匹配 "test result" 等结果, 测试跑完前我的焦点一直没被抢走。
- user: AI 编程重度用户, category: 坑, comment: prompt 超时后我当没发出去, 又发了一遍, agent 把同一任务跑了两遍。超时不等于没送达, 先用 agent get 和 read 看状态再决定要不要重发。
- user: 带 Agent 小组的 Tech Lead, category: 注意, comment: blocked 不是报错, 是检测到审批或提问弹窗, 先 agent read 看清再决定; TUI 的 Done 徽章每个客户端独立记录, 拿不准就用 agent get 查真相。
