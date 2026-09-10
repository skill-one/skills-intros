# expo-brownfield (`expo/skills/expo-brownfield`)

## comments

- user: iOS 原生老哥, category: 坑, comment: 建 RN 项目时没加 --template default@sdk-55, 生成的工程缺 ExpoReactNativeFactory 入口, 原生侧死活找不到。删掉重建才通。
- user: 安卓团队组长, category: 妙用, comment: 隔离方案用着像普通依赖:RN 团队丢给我们一个 AAR, 原生侧不用装 Node, 两仓独立发版互不拖累。
- user: 第一次接 RN 的新手, category: 注意, comment: iOS 走集成方案前先装 CocoaPods (sudo gem install cocoapods), 我没装直接跑 Podfile, 报错卡了半小时。
- user: 跨端架构师, category: 启发, comment: 选型先读 comparison.md:分仓独立发版选隔离, 单队想热更新选集成。我先错选集成, 后迁到隔离省心多了。
- user: 前端转 RN 的开发者, category: 坑, comment: 主工程和内嵌依赖的 Expo SDK 必须锁同一版本, 我只升了主工程, 模块解析直接报错。升级时两边一起动。
- user: 后端老兵, category: 注意, comment: 集成方案改 JS 没反应, 以为构建坏了, 其实是忘了起 Metro。跑原生壳前先起 Metro, 热更新立即生效。
