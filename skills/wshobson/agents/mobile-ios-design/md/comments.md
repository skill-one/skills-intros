# mobile-ios-design (`wshobson/agents/mobile-ios-design`)

## comments

- user: 前端转 iOS 的新手, category: 坑, comment: 我把行高和字号都写死,用户开大字体后文字被裁掉一截。改用 .headline 这类语义字体后高度自动撑开,千万别写死。
- user: 全栈老哥, category: 坑, comment: 信息流列表用 VStack 一把梭,几百条数据滚动就掉帧。换 LazyVStack 立刻顺滑,长列表从第一天就该用懒加载。
- user: 第一次带 iOS 项目的后端, category: 注意, comment: NavigationLink 传的数据模型必须是 Hashable,没实现就点不动,跳转毫无反应还不报错,我查了半天才发现。
- user: 做过无障碍验收的测试工程师, category: 注意, comment: 模拟器看着没问题不代表过得了验收:开 VoiceOver 听一遍,没加 accessibilityLabel 的图标按钮会被读成空白。
- user: 独立开发者, category: 妙用, comment: 一份 LazyVGrid 自适应网格,iPhone 自动两列、iPad 自动四列,不用维护两套布局,横竖屏切换也稳。
- user: UI 设计师, category: 启发, comment: 以前恨不得每个卡片都加阴影描边,读完「克制、让内容当主角」这条后做减法,结果反而更像原生应用了。
