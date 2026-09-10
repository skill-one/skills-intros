# flutter-setup-declarative-routing (`flutter/agent-plugins/flutter-setup-declarative-routing`)

## whitebox

- 脚手架: flutter create 建 App, flutter pub add go_router 引入路由库。
- 定义路由: 建一个 GoRouter 实例, 用 GoRoute 描述路径→屏幕的映射, 绑定到 MaterialApp.router; Web 端先调 usePathUrlStrategy 去掉 URL 里的 #。
- 配置深链接: 按目标平台改原生文件 (Android 改 AndroidManifest 加 intent-filter, iOS 改 Info.plist + entitlements), 并在你的域名下托管校验文件 assetlinks.json / apple-app-site-association。
- 验证循环: 用 adb (Android) 或 xcrun simctl (iOS) 模拟打开链接, 报错就修, 直到通过。
- 需要底部导航栏时, 用 StatefulShellRoute.indexedStack + StatefulShellBranch 搭持久化外壳, 每个标签页独立保留状态。

- 声明式路由解析: go_router 按 URL 路径匹配 GoRoute, 路径参数 (如 :id) 经 state.pathParameters 注入屏幕; redirect 参数在进入路由前做登录态拦截; 页面跳转统一走 context.go/push。
- 系统级域名验证: 深链接不是 App 自己解析, 而是 OS 先核对托管在域名 /.well-known/ 下的 JSON (Android assetlinks.json 需 SHA256 证书指纹, iOS AASA 需 TEAM_ID.appID), 验证通过才把 https://链接 递给 App; iOS 若用第三方插件需把 FlutterDeepLinkingEnabled 设 NO 防冲突。
- 外部依赖: 库层面是 go_router + flutter_web_plugins (url_strategy); 校验工具是 adb 与 xcrun simctl; 本技能由 models/gemini-3.1-pro-preview 模型驱动。
