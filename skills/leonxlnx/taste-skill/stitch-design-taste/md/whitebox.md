# stitch-design-taste (`leonxlnx/taste-skill/stitch-design-taste`)

## whitebox

- 接收目标项目的意图 / vibe 描述, 评估项目定位与氛围
- 把模糊的 vibe 量化为三个 1~10 维度: 密度 / 变化度 / 动效强度, 默认基线 Variance 8 / Motion 6 / Density 4, 按用户描述动态调整
- 由维度分数推导全套规则: 配色 (≤1 强调色, 禁 AI 紫霓虹)、字体 (禁 Inter 与通用衬线)、组件行为、布局原则、动效参数、反模式清单, 全部带精确 hex / rem / px 值
- 将正向规则 + NEVER DO 禁令填入固定的 8 段 markdown 结构, 生成 DESIGN.md
- DESIGN.md 作为单一事实源, 供 Google Stitch 按语义描述生成界面屏幕

- Vibe 量化映射: 模糊感受 → 三维评分, 分值直接触发条件规则 (如 Variance>4 禁居中 Hero, Density>7 数字强制等宽字体)
- 语义化 token 编码 + 内建校验: 每个设计 token = 描述性命名 + 精确值 + 功能角色, 禁止技术黑话直译 ("rounded-xl" → "generously rounded corners"); 硬约束校验: ≤1 强调色、饱和度<80%、禁纯黑 #000、禁 Inter/通用衬线; AI 味套路 (霓虹发光、三等分卡片、emoji、"Elevate" 类文案、假数据) 显式编码为 NEVER DO 禁令, 生成时逐一规避
- 外部依赖: 产物唯一消费方是 Google Stitch (labs.google/stitch); 可选 Stitch MCP Server 与 Cursor / Antigravity / Gemini CLI 程序化集成; 本体不依赖代码库或模型 API, 输出为纯文本规范
