# argent-device-interact (`software-mansion/argent/argent-device-interact`)

## comments

- user: 第一次用的新手, category: 坑, comment: 没加载手势工具 schema 就直接调, 参数被强转成字符串, 连着报校验错。动手前先用 ToolSearch 把要用的手势工具全加载一遍。
- user: 自动化测试工程师, category: 坑, comment: 以前等加载自己循环截图轮询, 看图看到吐。改用 await-ui-element 挂文本条件阻塞等最省; 另 hidden 秒成功多半没匹配到, 看 note 再下结论。
- user: React Native 开发, category: 注意, comment: 点 RN 页面底部按钮前, 先看有没有 Open Debugger 警告横幅, 我点穿一次调试直接断连。有横幅先点 X 关掉再操作。
- user: 测登录流程的老手, category: 妙用, comment: 密码框用 {{secret:PASSWORD}} 占位符输入, 明文不进对话也不进日志; 输完也别对那个输入框截图, 双保险。
- user: 前端转 Electron 桌面端, category: 注意, comment: 驱动 Electron 前先读 chromium.md: swipe 只认触摸, 我滚了半天网页没反应, 换 gesture-scroll 立刻就动了。
- user: 后端老兵, category: 启发, comment: 以前靠截图猜坐标, 十次歪三次。现在每步操作后直接读返回的元素树定位, 少看一半图, 思路从「看图」变成了「读树」。
