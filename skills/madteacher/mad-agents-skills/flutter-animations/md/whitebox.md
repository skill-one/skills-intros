# flutter-animations (`madteacher/mad-agents-skills/flutter-animations`)

## whitebox

- 判断请求类型: 新增/修复/重构/调试卡顿与生命周期/讲解/独立示例
- 读取本地 Flutter 上下文: widget 树、状态管理、路由、主题、无障碍配置、既有动画抽象
- 按决策表选最小动画模型: 隐式 (状态驱动) → 显式 controller (需要生命周期/手势控制) → Hero (跨路由共享元素) → staggered (错峰时序) → physics (速度/弹簧/滚动)
- 按项目既有风格实现: 保持公共 API 不变、controller 由所属 state 持有并 dispose、不在 build 里创建动画状态、用 AnimatedBuilder 控制重建范围、检查 disableAnimations 做降级
- 验证: dart format → flutter analyze → 相关导航/手势/生命周期变更跑 widget/integration 测试, 无法可视化验证的部分明确指出

- 按需资源路由: 只读当前任务对应的参考文档 (implicit/explicit/hero/staggered/physics/curves.md) 和配套模板文件; 模板是完整 demo 而非可直接投产模块, 套用时需改类名、删 main()、适配路由/状态后重新跑 analyze
- 决策表驱动选型: 用固定的『需求→默认方案』映射表替代自由发挥, 且有硬约束兜底——隐式动画能达到效果时不新增 AnimationController, 不盲抄参考代码 (需适配 Flutter 版本/lint/null-safety)
- 工具链验证闭环: 依赖 Flutter SDK 工具 dart format、flutter analyze、flutter analyze lib/main.dart (模板校验) 及 widget/golden/integration 测试; 无法实机运行时必须静态报告哪些视觉行为未验证
