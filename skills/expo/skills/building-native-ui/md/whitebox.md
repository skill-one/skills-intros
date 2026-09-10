# building-native-ui (`expo/skills/building-native-ui`)

## whitebox

- 路由与导航交给 expo-router skill 处理, 本技能只负责单个屏幕内部的 UI 构建
- 按技能内置的库偏好表选型: expo-image (含 SF Symbols)、expo-audio/expo-video、safe-area-context 等, 排除已废弃模块 (Picker/WebView/AsyncStorage/expo-av 等)
- 按 Apple HIG 写界面: 语义色、内联样式、flex gap、continuous 圆角、进入/退出动画、按条件加触觉反馈
- 响应式保障: 路由首组件为 ScrollView/FlatList 并设 contentInsetAdjustmentBehavior="automatic", flexbox + useWindowDimensions 布局, 顶部标题用导航栈标题而非自定义文本
- 运行验证: 先 npx expo start 用 Expo Go 扫码实测, 功能跑不通才升级为自定义原生构建

- 参考文档按需加载: references/ 目录按主题拆成八份 (animations/controls/gradients/icons/media/storage/visual-effects/webgpu-three), 写到对应功能时才查阅对应文档
- 颜色解析机制: 用 expo-router 的 Color API 读取 iOS UIKit / Android Material 3 原生语义色, 经 Platform.select 包装 + 十六进制 web 兜底, 集中定义在 theme/colors.ts 全局引用, 深浅色模式自动适配
- 运行策略分流 + 代码规范强制: Expo Go 优先, 仅本地原生模块/Apple targets/第三方原生模块/特殊 app.json 四种情况才需自定义构建; 同时校验代码规则 — kebab-case 文件名、import 置顶、内联样式优先、阴影一律 CSS boxShadow (禁旧 shadow/elevation)、禁用 img/div 等原生 HTML 元素
