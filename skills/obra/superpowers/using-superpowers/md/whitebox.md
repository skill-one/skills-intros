# using-superpowers (`obra/superpowers/using-superpowers`)

## whitebox

- 对话一开始即触发: 在任何回应 (包括反问澄清、探索代码库) 之前, 先检查任务是否有适用的技能 —— 哪怕只有 1% 可能适用也必须调用
- 命中后宣布 "Using [skill] to [purpose]" 并调用该技能; 发现不合适可以不用, 但必须先查
- 严格按技能内容执行; 若技能带 checklist, 逐项转为待办事项
- 多技能并存时按优先级排序: 流程技能先行定调 (如 brainstorming、systematic-debugging), 实现类技能随后执行 (如 frontend-design)
- 用户显式指令 (CLAUDE.md、直接要求) 优先级最高, 可覆盖技能规则

- 强制调用闸门: 内置「红旗对照表」拦截一切合理化跳过的念头 (如"这只是个简单问题"、"我先快速看下文件"), 任何跳过技能检查的行动都被视为 rationalizing, 必须停下回到技能检查
- 纯调度器架构: 本技能自身不做任何具体任务, 只负责路由 —— 实际工作委托给外部 Superpowers 技能库 (brainstorming、systematic-debugging、frontend-design 等) 按名字调用; 外部依赖即该技能库及各平台适配参考文件 (references/codex-tools.md、pi-tools.md 等), 不依赖其他库或模型 API
- 平台适配机制: 检测运行环境类型 (Codex / Pi / Antigravity / Hermes Agent), 命中则读取对应参考文件获取该平台的特殊工具指令后再继续
