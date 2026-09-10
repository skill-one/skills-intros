# expo-dev-client (`expo/skills/expo-dev-client`)

## whitebox

- 判断场景: 只有当用到自定义原生模块、Apple 扩展 (widget 等)、Expo Go 未内置的第三方原生库、config plugin 或推送/Universal Link 时, 才需要 dev client
- 配置 eas.json: 确保 development profile 开启 developmentClient: true + autoIncrement: true, 版本号以 EAS 为准 (appVersionSource: remote)
- 构建: 云端跑 eas build -p ios --profile development (可加 --submit 直送 TestFlight), 或本机 --local 构建 (iOS 需 Xcode)
- 安装产物: .ipa 装到真机/模拟器 (ideviceinstaller / xcrun simctl), .apk 用 adb install
- 连接运行: 启动 Metro (npx expo start --dev-client), 在手机上的 dev client 里扫码或输入 URL 加载 JS

- Profile 驱动构建: eas.json 的 development profile 是核心开关, developmentClient: true 让打出的原生包内置 expo-dev-client 运行时 (替代 Expo Go); autoIncrement + remote 版本源让 EAS 服务端管理 build number, 避免手动维护
- 双通道产物分发: 本地构建 (--local) 免费, 直接产出 .ipa/.apk/.aab, 依赖本机 Xcode 与 adb/ideviceinstaller/simctl 完成安装; 云端构建消耗 EAS build 分钟数, --submit 会自动把产物提交到 App Store Connect → TestFlight (需付费 Apple 开发者账号), 构建完成后邮件通知
- 原生壳 + JS 热连: dev client 本质是一个可连接 Metro bundler (JS 开发服务器) 的原生壳, 通过扫码/输入 URL 建立连接, launcher UI 可切换多个 dev server; 因此改 JS 免重装, 改原生代码才需要重新 build
