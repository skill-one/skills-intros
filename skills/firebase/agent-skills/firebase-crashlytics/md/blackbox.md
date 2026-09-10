# firebase-crashlytics (`firebase/agent-skills/firebase-crashlytics`)

## blackbox

**function**: 帮你给手机 App (Android / iOS) 接上「崩溃收集」: App 闪退时自动记下原因和现场, 让你知道哪里坏了、为什么坏。

- input: 「我有个 Android 应用, 想接入 Firebase 崩溃收集」, output: 一套从零到跑通的接入步骤 + 可直接粘贴的配置与初始化代码
- input: 「iOS 应用怎么装 Crashlytics?」, output: 对应 iOS 平台的安装步骤和 Swift 初始化代码
- input: 「App 崩了, 但我还想知道当时是哪个用户、做了什么操作」, output: 对应平台的示例代码: 挂自定义标签、记录日志、绑定用户标识, 以及主动上报『没闪退但也算出错』的异常
