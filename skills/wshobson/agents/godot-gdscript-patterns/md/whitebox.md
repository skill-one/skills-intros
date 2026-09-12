# godot-gdscript-patterns (`wshobson/agents/godot-gdscript-patterns`)

## whitebox

- 接收任务, 检查触发条件: 是否与 Godot 4 / GDScript 相关 (写游戏系统、设计场景架构、状态管理、性能优化、学最佳实践)
- 命中后直接使用 SKILL.md 内置的导航层知识: Godot 架构模型 (Node→Scene/Resource/Signal/Group) + GDScript 代码骨架模板
- 模板不够用时, 按文档指引读取本地文件 references/details.md 获取详细模式
- 按 skill 固定约定产出面向 Godot 4.x 的类型化 GDScript 代码或架构方案

- 分层文档 + 渐进式加载: SKILL.md 只存核心概念与一份可跑的代码模板作导航层; 详细模式全部外置到 references/details.md, 仅在导航层不够时才读取 —— 这是声明的唯一文件依赖
- 统一代码规范保证输出一致性: class_name + extends 声明、signal 事件通信、@export 暴露到 Inspector、@onready 延迟取节点、下划线前缀标私有变量、全程类型注解
- 无外部工具/库/模型 API: SKILL.md 未声明任何外部依赖, 产出物即纯 GDScript, 目标运行环境只有 Godot 4.x
