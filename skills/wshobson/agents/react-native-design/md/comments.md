# react-native-design (`wshobson/agents/react-native-design`)

## comments

- user: Web 前端转 RN 的, category: 坑, comment: 照 Web 习惯用 ScrollView 套 map 渲染长列表, 一百多条数据滑两下就卡。换 FlatList 才顺, 新手别重蹈覆辙。
- user: 独立开发一个人撸 App, category: 妙用, comment: 直接把示例的 ItemCard 抄成项目卡片模板, 自带按压回弹和阴影, 列表瞬间有原生手感, 省了我一天调样式。
- user: 第一次用的新手, category: 注意, comment: 模拟器里动画丝滑, 装到真机就掉帧——两者表现差很多。上线前务必真机跑一遍, 卡了再往 UI 线程 worklet 挪。
- user: iOS/Android 双端上架的开发者, category: 坑, comment: 只写了 shadowColor 那套阴影, iOS 正常 Android 全平。要补 elevation, 或用 Platform.select 分端写样式。
- user: 被刘海屏坑过的, category: 注意, comment: 我把头部写死 padding 20, 刘海屏上内容直接钻进状态栏。改用 useSafeAreaInsets 按机型取边距才正常。
- user: 接手他人 RN 项目的, category: 启发, comment: 接手的老项目内联样式满天飞, 我照指南全换 StyleSheet.create 并给列表项加 memo, 滚动肉眼可见变顺, 这笔债值得先还。
