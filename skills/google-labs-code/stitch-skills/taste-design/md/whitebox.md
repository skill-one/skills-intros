# taste-design (`google-labs-code/stitch-skills/taste-design`)

## whitebox

- 接收用户的项目意图/氛围描述, 沿 Density/Variance/Motion 等轴量化基调 (默认 Creativity 9 / Variance 8 / Motion 6 / Density 5, 按用户描述动态调整)
- 据基调校准色板 (Zinc/Slate 中性基座 + 最多 1 个饱和度<80% 的强调色) 与字体架构 (禁 Inter/通用衬线, 强制 Geist/Satoshi 等特色字体)
- 逐项定义组件行为 (按钮/卡片/输入/加载态)、布局原则、响应式折叠规则与动效规格 (弹簧物理 + 永续微交互)
- 将 AI 设计俗套封禁清单编码为 DESIGN.md 的 Anti-Patterns (NEVER DO) 章节
- 用 Write 工具落盘 DESIGN.md, 作为后续向 Google Stitch 生成屏幕的唯一事实来源

- 语义翻译机制: 把工程级硬约束转写为 Stitch AI 代理可解读的自然语言规则, 且每条规则必须"描述性命名 + 精确值"成对出现 (如 Charcoal Ink #18181B、弹簧参数 stiffness:100/damping:20、触控目标≥44px), 拒绝含糊表述
- 约束驱动校验: 输出过负向闸门 — Anti-Patterns 清单显式封禁 Inter、纯黑 #000000、紫色霓虹辉光、三列等宽卡片、居中 Hero (variance>4 时)、编造数据/指标、"LABEL // YEAR"式排版等 AI 味俗套
- 外部依赖: 唯一消费目标是 Google Stitch (labs.google.com/stitch), DESIGN.md 即其生成屏幕的提示词事实来源; 可选经 Stitch MCP Server 程序化接入 Cursor/Antigravity/Gemini CLI; 文件读写由 Read/Write 工具完成
