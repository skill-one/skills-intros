# mobile-ios-design (`wshobson/agents/mobile-ios-design`)

## blackbox

**function**: 把你的 iOS 界面想法变成符合苹果设计规范、可直接使用的 SwiftUI 代码。

- input: 一句话描述，如「做一个记账 App 的首页，顶部是本月总支出卡片，下面是交易列表」, output: 完整的 SwiftUI 界面代码，含卡片样式、列表布局，贴进 Xcode 就能运行
- input: 一段自己写的、不太规整的 SwiftUI 代码, output: 改好的代码：适配深色模式、字体随系统缩放、无障碍支持等，并标注改了哪里
- input: 一个问题，如「底部标签栏怎么和页面跳转一起做？」, output: 能运行的示例代码 + 简短说明，按苹果推荐的方式（TabView + NavigationStack）实现
