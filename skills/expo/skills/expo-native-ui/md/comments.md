# expo-native-ui (`expo/skills/expo-native-ui`)

## comments

- user: 业余独立开发者, category: 妙用, comment: 把颜色全换成 expo-router 的 Color API 后, colors.web.ts 那套明暗两份十六进制直接删了, 深色模式开箱即用, 再没维护过色值表。
- user: iOS 原生转来的新手, category: 坑, comment: 图标全用了 SF Symbols, iPhone 模拟器很美, 安卓真机全空白。每个图标必须给安卓另配 Material 源, 上线前一晚才发现。
- user: 后端出身第一次摸 App, category: 注意, comment: 别上来就 expo run:ios, 我光配 Xcode 就耗了一晚。先 npx expo start 用 Expo Go 扫码, 大部分功能直接能跑, 真不行再自建。
- user: 写过 RN 动画的前端, category: 坑, comment: 把 Color.ios.label 塞进 Reanimated 样式, 颜色压根不生效——它是不透明原生对象, 动画里老老实实用静态色值。
- user: 常写列表页的前端, category: 坑, comment: FlatList 外面又包了层 ScrollView, 滚动打架、布局全乱。列表页就让 FlatList 自己当滚动容器, 别套外壳。
- user: App 开发老兵, category: 妙用, comment: ScrollView 加 contentInsetAdjustmentBehavior='automatic' 后, SafeAreaView 全删了, 安全区和大标题收起都自动算好。
