# expo-brownfield (`expo/skills/expo-brownfield`)

## blackbox

**function**: 帮你在现有的原生 iOS / Android 应用里, 加进 React Native (用 JavaScript 写界面) 的页面或功能, 并搞定选型、配置和报错。

- input: 一个已有的原生 Android 工程 (Kotlin + Gradle), 加一句需求: 「我想在里面开一个 React Native 页面」, output: 一套可直接照做的接入方案: 改好的构建配置、打开 RN 页面的示例代码, 以及每一步做完应该看到什么
- input: 一段团队情况描述, 如: 「原生团队 5 人, RN 团队 2 人, 两边代码在不同仓库, 各自发版」, output: 明确告诉你该选哪种集成方式 (预编译包 vs 源码集成), 以及对应的取舍和理由
- input: 现有 iOS 工程 (Swift) + 需求: 「把 RN 模块做成一个包, 原生团队像装普通库一样接入」, output: 具体做法: 生成可分发的 RN 组件包, 以及原生工程里怎么引用、怎么展示这个页面
- input: 一段报错信息或现象, 如: 「RN 页面白屏 / 连不上本地开发服务器」, output: 问题原因的判断 + 修复步骤, 修好前先给出能让页面跑起来的临时办法
