# vercel-react-native-skills (`vercel-labs/agent-skills/vercel-react-native-skills`)

## comments

- user: 转做 App 的 Web 前端, category: 坑, comment: 网页习惯 `count && <组件/>` 直接搬进 RN, 购物车为 0 时屏幕上印出个 0, 改三元才对. 另外文字不包 Text 组件会直接报错. rendering 这两条规则专治 web 党.
- user: 赶工修卡顿的全栈, category: 妙用, comment: 列表卡先照优先级表过一遍 8 条 list-performance 规则. 我的元凶是内联样式对象: 每次渲染新建, 整列表跟着重绘. 提到组件外 StyleSheet.create 就顺了.
- user: 第一次写 RN 的新手, category: 坑, comment: 首页用 ScrollView+map 渲染 800 条商品, 滑动掉帧到没法用. 换 FlashList、列表项加 memo 才救回来. 几十条以上的列表别碰 ScrollView.
- user: 带五人 RN 小组的组长, category: 启发, comment: 现在评审直接引规则名: 「list-performance-callbacks, 这个 onPress 每次渲染都是新引用」. 比「感觉有点卡」具体十倍, 新人也能拿规则名自查.
- user: 十年安卓转跨端, category: 妙用, comment: 动画只动 transform 和 opacity 这条点醒我: 之前用 Reanimated 改 width, 一直掉帧. 换 scale 后稳 60fps, 一条规则省了我两天试错.
- user: 上架过两款 App 的独立开发, category: 注意, comment: 它是最佳实践手册, 不会自动改代码: 推荐的 FlashList、expo-image、Reanimated 都要自己装, 再照各 rule 文件里的正确示例改自己的写法.
