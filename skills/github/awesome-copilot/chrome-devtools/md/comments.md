# chrome-devtools (`github/awesome-copilot/chrome-devtools`)

## comments

- user: 第一次用的新手前端, category: 坑, comment: 上来就按截图点按钮, 点不动——点击要靠快照给的 uid。跳页后 uid 会失效, 复用旧的直接报错, 每步操作前重抓一次快照就稳了。
- user: 全栈老兵, category: 妙用, comment: 排查白屏的固定套路: 先看 console 报错, 再过滤网络请求里的 4xx/5xx, 一遍就能分清前端挂了还是接口挂了, 不用自己开 F12 翻面板。
- user: QA 测试工程师, category: 妙用, comment: 响应式和弱网验收不用真机: resize_page 调到 375 宽, 再 emulate 限速 Slow 3G, 骨架屏兜底逻辑一跑就现形, 还能留截图当证据。
- user: 运维老哥, category: 注意, comment: 页面弹 alert 时流程会卡住, 别以为挂了, 要先 handle_dialog 处理掉弹窗; 慢页面用 wait_for 记得留足超时, 我干等过好几分钟。
- user: 性能优化工程师, category: 妙用, comment: trace 加 reload=true、autoStop=true 一条龙录完首屏, analyze_insight 直接指出 LCP 卡在哪段, 我手动录 Performance 的活基本省了。
- user: 做数据整理的运营, category: 启发, comment: 以前导后台数据全靠复制粘贴, 现在让它用 evaluate_script 跑段 JS 直接吐结构化结果。我开始把重复网页操作都想能不能交给它。
