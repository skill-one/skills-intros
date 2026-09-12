# argent-android-emulator-setup (`software-mansion/argent/argent-android-emulator-setup`)

## comments

- user: 第一次用的新手, category: 注意, comment: 先在 Android Studio 建好 AVD, 用 emulator -list-avds 确认能列出名字, boot-device 才有 avdName 可填。我没建设备就开机, 白报错半天。
- user: React Native 开发, category: 坑, comment: 模拟器重启后 App 红屏连不上 8081, 原因是忘了重跑 adb reverse。记住每次重启设备都要重新 reverse 一次, 红屏先查这里。
- user: 后端老兵, category: 坑, comment: kill -9 强杀卡住的模拟器后镜像写脏, 冷启动连着几次挂十几分钟。要用 adb -s 序号 emu kill; 已脏就带 -wipe-data 开一次机重置。
- user: TV 端开发, category: 坑, comment: 电视 AVD 的序号长得和手机一样, 我拿 gesture-tap 点半天没反应。runtimeKind 显示 tv 时要换 tv-remote 加键盘, 电视靠焦点不吃点击。
- user: UI 自动化测试工程师, category: 妙用, comment: 安卓上 reinstall-app 重装自带权限预授予, 首启不再弹授权框, 我的用例再也不随机死在权限弹窗上了。
- user: 从 iOS 转来的前端, category: 注意, comment: 安卓这里传的是 serial, 不是 iOS 那种 UDID, 平台不用自己指定。另外 describe 的树比 iOS 浅, 找不到可点元素就先 screenshot 肉眼确认。
