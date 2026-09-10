# swiftui-pro (`twostraws/swiftui-agent-skill/swiftui-pro`)

## whitebox

- 接收 Swift/SwiftUI 代码, 判断是全面审查还是部分审查 (部分审查则只加载对应主题的参考文件)
- 按顺序过 9 项检查: 废弃 API → 视图/动画写法 → 数据流 → 导航 → 设计规范(HIG) → 无障碍 → 性能 → Swift 语法 → 代码卫生
- 只保留真实问题, 不吹毛求疵、不编造问题; 无问题的文件直接跳过
- 按文件组织输出: 文件名 + 行号 + 违反的规则 + 修改前/修改后代码对照
- 结尾给出按影响程度排序的优先修改清单

- 规则库驱动: 9 份内置参考文档 (references/api.md、views.md、data.md、navigation.md、design.md、accessibility.md、performance.md、swift.md、hygiene.md) 是唯一审查依据, 无外部工具、库或模型 API 依赖
- 内置环境假设: 默认目标 iOS 26 + Swift 6.2+ (现代 Swift 并发), 坚持纯 SwiftUI 避开 UIKit, 未经询问不引入第三方框架, 一个类型一个文件、按功能组织目录
- 固定输出协议: 每个问题必须落在 '文件 → 行号 → 规则 → before/after 代码' 格式里, 保证结果可定位、可执行
