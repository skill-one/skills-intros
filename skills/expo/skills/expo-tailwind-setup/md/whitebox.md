# expo-tailwind-setup (`expo/skills/expo-tailwind-setup`)

## whitebox

- 装依赖: npx expo install tailwindcss@^4 nativewind@5 react-native-css @tailwindcss/postcss tailwind-merge clsx, 并在 package.json 固定 lightningcss@1.30.1
- 写两份配置: metro.config.js 用 withNativewind 接管 Metro (inlineVariables: false), postcss.config.mjs 挂 @tailwindcss/postcss; 全程不需要 babel.config.js (旧 NativeWind babel 预设反而要删)
- 建 src/global.css: @import "tailwindcss/theme.css" layer(theme) / preflight.css / utilities.css 三件套, 附带 @media ios / @media android 的字体变量
- 生成 CSS 组件包装器 (src/tw/): 用 react-native-css 的 useCssElement 包一层 View/Text/ScrollView/Pressable/TextInput/Link/Image/Animated
- 业务代码改为 import { View, Text } from "@/tw" 直接写 className; 可选增强: @theme 自定义 token、Apple 语义色、useCSSVariable 在 JS 里读 CSS 变量

- CSS-first 转换链: 对比 v3/v4 的关键差异——配置全部内联进 CSS (@import 分层文件 + @theme 定义 token), 不再有 tailwind.config.js 和 babel 预设; 样式编译走 @tailwindcss/postcss, 兼容性由 lightningcss (锁定 1.30.1) 处理, 所以 Expo 下不需要 autoprefixer
- className→style 运行时桥接: 所有组件经 useCssElement (来自 react-native-css) 包装, 通过显式映射表生效, 如 { className: "style" }、ScrollView 的 contentContainerClassName→contentContainerStyle; 特殊改写: expo-image 的 objectFit→contentFit、TouchableHighlight 从 flat 后的 style 里抽出 underlayColor
- 跨平台样式解析: 用标准 CSS 特性做平台分支——@media ios 块内用 platformColor() 拿 iOS 原生色 (systemBlue/label 等), web/Android 回退到 light-dark(); 经 @theme 注册成 --color-* 变量供 text-sf-text 这类工具类消费; JS 侧 useCSSVariable 读值时按平台分派 (web 返回 var(--x) 字符串, 原生走 useNativeVariable); Metro 侧 inlineVariables: false 保证 PlatformColor 不被内联破坏
