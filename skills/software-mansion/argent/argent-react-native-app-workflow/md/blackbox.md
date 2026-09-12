# argent-react-native-app-workflow (`software-mansion/argent/argent-react-native-app-workflow`)

## blackbox

**function**: 把 React Native (一套用 JS 同时开发 iPhone / Android 应用的框架) 项目在手机模拟器上跑起来, 并修好启动、构建、运行中出现的各种问题。

- input: 一个 React Native 项目文件夹 + 「帮我在 iPhone 模拟器上启动」, output: 模拟器里装好并打开了 App, 你能直接看到能操作的运行界面
- input: 「App 打开就红屏报错 / 白屏卡住」, output: 问题被定位并修复, App 恢复正常界面, 附修复前后的截图对比
- input: 「我刚改了几个页面文件, 帮我确认效果」, output: 模拟器里的 App 直接刷新显示改动, 不用重新安装; 也可顺带跑一遍测试, 给出通过/失败的报告
