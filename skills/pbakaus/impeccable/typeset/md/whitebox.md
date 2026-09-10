# typeset (`pbakaus/impeccable/typeset`)

## whitebox

- 强制前置: 调用 /impeccable 技能获取设计原则、反模式与上下文收集协议; 若尚无设计上下文, 先执行 /impeccable teach
- 评估现状: 从字体选择、层级、字号比例、可读性、一致性五个维度诊断现有排版的薄弱点
- 制定计划: 确定字体替换方案、模块化字阶 (固定比例如 1.25)、字重角色分配、行高/字距/间距
- 系统实施: 更换字体、建立 5 档层级、修复可读性 (65ch 行宽、分场景行高)、打磨细节 (tabular-nums、letter-spacing、语义化 token)
- 验证结果: 按清单核对层级可辨性、正文 ≥16px、同角色样式一致、品牌个性、字体加载性能、WCAG 对比度与 200% 缩放

- 依赖链: /impeccable 是强制前置技能 (提供设计原则、反模式清单、上下文收集协议), 字阶/字体配对/加载策略查阅其 reference/typography.md; 无外部模型 API 依赖
- 转换机制: 全部落地为 CSS 规则 — 字号用 rem 不用 px (尊重用户设置), 营销页标题用 clamp() 流式缩放, 文本容器 max-width: 65ch, font-display: swap 防布局抖动, token 用语义命名 (--text-body 而非 --font-16)
- 校验机制: 验证清单 + NEVER 禁区双重约束 — 清单覆盖层级/可读性/一致性/性能/无障碍; 禁区限制字体族 ≤3、字重 ≤4、正文不得低于 16px、装饰字体不得做正文、禁止 user-scalable=no
