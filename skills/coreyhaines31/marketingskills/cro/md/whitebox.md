# cro (`coreyhaines31/marketingskills/cro`)

## whitebox

- 读上下文: 先探测并读取产品营销上下文文件 (`.agents/product-marketing.md` 及 `.claude/` 变体、legacy 文件名), 已覆盖的信息不再问用户
- 定三要素: 确认页面类型、主要转化目标、流量来源 — 仅对上下文未覆盖的部分向用户提问
- 跑分析: 按 7 维框架逐项检查 (价值主张 → 标题 → CTA → 视觉层级 → 信任信号 → 异议处理 → 摩擦点), 并叠加页面类型专属框架 (首页/落地页/定价/功能/博客)
- 出报告: 按固定四段结构输出 — Quick Wins / 高影响改动 / A/B 测试假设 / 文案备选 (每处 2~3 个带理由)
- 做路由: 按问题归属转介姊妹技能 — signup / popups / copywriting / ab-testing

- 上下文注入优先: 命中 `product-marketing.md` 就先读, 用存量上下文替代盘问 — 只问增量缺口信息
- 规则驱动而非自由发挥: 7 维检查清单每维都有明确检查项与好坏判据 (如 CTA 弱文案 'Submit' vs 强文案 'Start Free Trial'), 分析面再由页面类型子框架收窄, 输出可复现
- 固定输出契约 + 按需加载引用: 结果强制四段结构; 表单与实验细节下沉到 `references/form.md`、`references/experiments.md`; 除本地文件读取外, 无外部库 / 模型 API 依赖
