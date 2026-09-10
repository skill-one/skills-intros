# enhance-prompt (`google-labs-code/stitch-skills/enhance-prompt`)

## whitebox

- 评估输入: 按六项清单 (平台/页面类型/结构/视觉风格/颜色/组件) 找出 prompt 里缺失的信息
- 检查项目里的 DESIGN.md: 存在则用 Read 读取并提取设计系统; 不存在则记住, 输出末尾附加提示
- 应用四类增强: 模糊措辞替换为具体 UI 组件名、补氛围形容词、内容重组为编号页面区块、颜色格式化为「名称 (#hex) + 用途」
- 按固定模板格式化: 一句话定位 → DESIGN SYSTEM (REQUIRED) 设计系统区块 → 编号 Page Structure
- 默认以文本返回供复制; 用户要求时才用 Write 写入 next-prompt.md 或自定义文件名

- 规则表驱动的确定性转换, 无模型自由发挥: 内置「模糊→精确」关键词映射 (如 menu at the top → navigation bar with logo and menu items) 和氛围形容词升级表 (如 modern → clean, minimal, with generous whitespace)
- 设计系统注入保证多页一致性: 有 DESIGN.md 就把其色板/字体/组件样式格式化为 DESIGN SYSTEM (REQUIRED) 区块; 没有则在末尾追加引导用户用 design-md skill 创建的提示
- 外部依赖仅三处: 工具层只声明 Read/Write; 前置要求查阅官方 Stitch Effective Prompting Guide (https://stitch.withgoogle.com/docs/learn/prompting/) 同步最新最佳实践; 产出物最终供 Stitch (Google 的 UI 生成工具) 消费
