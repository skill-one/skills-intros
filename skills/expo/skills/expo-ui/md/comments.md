# expo-ui (`expo/skills/expo-ui`)

## comments

- user: 第一次用的新手, category: 坑, comment: BottomSheet 写了 isOpen 死活不弹，还不报错。正确属性是 isPresented/onDismiss，旧属性会静默失效，改完秒好。
- user: 创业公司前端, category: 坑, comment: 把 @expo/ui/swift-ui 组件写进普通页面，iOS 正常，Android 一进就崩 view config。得拆成 .ios/.android.tsx 两套，还别放 app/ 目录。
- user: 独立开发者, category: 注意, comment: List 不是滚动列表，是 iOS 设置页那种分组行，节点不回收。我拿它渲 500 条搜索结果直接卡爆，换 FlatList 秒好。短设置页才用它。
- user: 老项目维护者, category: 妙用, comment: 项目 30 多处用 @gorhom/bottom-sheet，走 @expo/ui/community 的替换包只改 import，调用处几乎没动，还顺手摘掉了 Reanimated 依赖。
- user: 自学中的转行者, category: 注意, comment: universal 组件要 SDK 56+，Expo Go 里直接能跑，不用自己出包。我 SDK 55 的老项目装不上，后来才知 55 只支持平台专用那两层。
- user: 移动端组长, category: 启发, comment: 定了条团队规范：开关、滑块、底抽屉先查 @expo/ui 有没有，没有才引第三方。一份代码两端都是原生渲染，评审清净多了。
