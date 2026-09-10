# expo-brownfield (`expo/skills/expo-brownfield`)

## whitebox

- 识别场景: 现有原生 iOS/Android 应用要嵌入 React Native (brownfield), 先按仓库结构/团队/工具链在 isolated 与 integrated 两种方案中选定其一
- 检查构建环境前置条件: 打包 RN 的一侧需 Node.js LTS + Yarn; 选 integrated 且目标为 iOS 时另需 CocoaPods
- 创建并固定 SDK 版本: 用 npx create-expo-app --template default@sdk-55 创建项目, Expo SDK 55 是 brownfield 集成的最低版本要求
- 按所选方案执行对应参考文档: isolated 走 AAR/XCFramework 预构建路线 (BrownfieldActivity / ReactNativeViewController / ReactNativeView), integrated 走 Gradle/CocoaPods 集成路线 (ReactActivity / RCTRootView / Podfile)
- 遇到 Metro 连接、构建、签名、模块解析等问题时, 按 troubleshooting.md 排查

- 双方案路由: 依据团队归属、仓库是否分离、原生团队是否愿意装 RN 工具链、是否需要热重载与 JS source map, 在 comparison.md 决策矩阵上落点为 isolated 或 integrated
- 产物差异是核心转换点: isolated 把 RN 侧构建成 AAR (Android) / XCFramework (iOS) 预编译包, 原生工程按普通依赖消费、无需 Node/Yarn/RN 构建链; integrated 则把 RN 源码直接挂进现有 Gradle/CocoaPods 构建, 换取热重载与 source map 无缝工作
- 外部依赖与版本约束: Node.js LTS、Yarn、npx 驱动的 Expo CLI 为共用前提; integrated iOS 额外依赖 CocoaPods (sudo gem install cocoapods); 依赖 Expo SDK 55+ 提供的 expo-brownfield、ExpoReactHostFactory/ExpoReactNativeFactory 入口与 autolinking, RN 工程与嵌入依赖需锁定同一 SDK 版本
