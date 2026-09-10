# swiftui-expert-skill (`avdlee/swiftui-agent-skill/swiftui-expert-skill`)

## blackbox

**function**: 帮你搞定 iOS/macOS 的 SwiftUI 界面代码: 写新页面、改旧代码、查出卡顿掉帧的原因, 交给你能直接用的代码和报告。

- input: 一个 SwiftUI 代码文件的路径, 加一句 "帮我检查一下", output: 一份代码审查报告: 哪里是过时写法、哪里有状态不刷新之类的隐藏 bug, 每条附上改好的代码
- input: 一句需求, 例如 "做一个带搜索框和下拉刷新的商品列表页", output: 可直接运行的 SwiftUI 代码, 适配最新 iOS 版本, 老系统上自动用兼容写法
- input: 一个 Instruments 的 .trace 文件 (性能录制的文件), 或一句 "帮我录一段性能数据", output: 一份性能诊断报告: 哪个界面被反复无谓刷新、谁在拖慢主线程导致卡顿掉帧, 按优先级排好的修复清单
