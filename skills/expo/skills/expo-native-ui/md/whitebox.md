# expo-native-ui (`expo/skills/expo-native-ui`)

## whitebox

- 收到「构建原生质感 Expo 界面」类任务后, 先划界: 路由/导航转交 expo-router skill, 动画转交 expo-animation skill, 本 skill 只管结构、样式与视觉。
- 选组件前先查 expo-ui skill: 优先用 @expo/ui 的原生组件 (BottomSheet/Button/Picker/Switch 等, iOS 渲染 SwiftUI、Android 渲染 Compose), 不适用再回退到 RN 内置或社区库。
- 按需查阅 references/ (controls/gradients/icons/media/storage/visual-effects/webgpu-three) 并按样式规则写代码: 语义色、SF Symbols + Android Material 图标、禁用已废弃模块。
- 跑起来: 先试 Expo Go (npx expo start 扫码), 只有涉及本地原生模块/Apple targets/第三方原生模块时才走自定义构建 (npx expo run:ios/android)。
- 完成前自检: 走一遍主任务含一次失败与恢复, 检查键盘、返回/关闭行为、长标题/无图/大字号, 最后报告验证了什么、哪些没法跑。

- 组件分派机制: 一张「库偏好清单」决定技术选型 — @expo/ui 优先于 RN 内置; 明确禁用已废弃模块 (Picker/WebView/SafeAreaView/AsyncStorage、legacy expo-permissions、expo-av), 用 expo-audio/expo-video/expo-image/expo-symbols 替代; iOS 用 SF Symbols (SymbolView), Android 必须配 Material 图标, 不允许 SF-only。长列表 (FlatList/FlashList) 与设置短列表 (@expo/ui List) 按长度分流。
- 颜色与样式解析: 用 expo-router 的 Color API (iOS UIKit 色 + Android Material 3/动态取色) 统一收口到 theme/colors.ts, 经 Platform.select 包装并带 hex 兜底, 自动适配深浅色; 不支持 CSS/Tailwind, 只用内联样式; 阴影用 boxShadow 而非 legacy shadow/elevation。依赖: expo-router、@expo/ui、react-native-safe-area-context、SDK 56+ 经 expo-router/react-navigation 间接引 @react-navigation。
- 运行环境降级策略 + 验收校验: 默认 Expo Go 即可跑大多数 expo-* 包与 Expo Router, 仅在本地原生模块/Apple targets/未被 Expo Go 捆绑的第三方原生模块时才编译自定义构建; 交付前强制走查主任务 (含一次加载/保存失败与恢复), 遇 skill 本身的错误可经 npx submit-expo-feedback 上报。
