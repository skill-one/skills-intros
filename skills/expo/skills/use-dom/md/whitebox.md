# use-dom (`expo/skills/use-dom`)

## whitebox

- 判定适用场景: 任务需用 web-only 库 (如图表库)、迁移既有 web 组件、复杂 CSS 或 canvas/iframe, 且非性能关键路径、非 _layout 路由
- 新建独立组件文件: 顶部写 'use dom' 指令, 单文件单默认导出, props 限定可序列化类型并声明 dom prop 类型
- 在原生父组件中像普通组件一样引入使用, 通过 dom prop 配置 webview 行为 (滚动开关、尺寸、安全区等)
- 需要原生能力时, 把 async 函数作为 props 传入, webview 内触发即回调原生; 路由参数在原生侧读取后以 props 下传
- 运行时分流: iOS/Android 装进 WebView 渲染, web 平台原样渲染且忽略 dom prop

- 平台分流机制: 'use dom' 指令标记组件, 原生端 (iOS 用 WKWebView, Android 用 WebView) 在独立 JS context 中渲染 web 代码, web 端无 webview 直接渲染 — 依赖 Expo (expo/dom)
- 原生↔web 桥接机制: 字符串/数字/布尔/数组/纯对象等可序列化 props 经序列化传入; async 函数 props 被桥接为可调用原生动作; expo-router 的 <Link>/router API 在组件内可用, 但 useLocalSearchParams 等需同步读取路由状态的 hooks 必须由原生侧读取后以 props 传入 — 依赖 expo-router
- web 库复用与样式隔离机制: 组件运行于浏览器环境, recharts、react-syntax-highlighter 等依赖 DOM API 的 React web 库免修改直接 import; CSS 须在组件文件内 import 或内联 (隔离上下文), 静态资源用 require 打包而非 public 目录
