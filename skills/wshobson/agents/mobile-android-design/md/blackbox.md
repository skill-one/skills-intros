# mobile-android-design (`wshobson/agents/mobile-android-design`)

## blackbox

**function**: 帮你设计原生 Android 应用的界面，直接产出能运行的界面代码（Kotlin + Jetpack Compose），并确保符合 Google 的 Material Design 3 规范。

- input: 一段界面描述，如「做一个音乐 App 的播放列表页，每行是封面、歌名、歌手名，点击跳转」, output: 一份完整的 Compose 界面代码文件（Kotlin），可直接放进 Android 项目编译运行，含卡片布局、点击事件
- input: 你现有的一段 Compose 界面代码, output: 按 Material 3 规范修订后的代码：颜色改用主题变量（自动适配深色模式）、按钮等可点区域不小于 48dp、可访问性标签补齐
- input: 一条适配需求，如「这个 App 要在手机、平板和折叠屏上都好看」, output: 自适应布局代码（用 WindowSizeClass 区分屏幕尺寸）+ 一份简洁的改动说明，列出各屏幕下的布局差异
