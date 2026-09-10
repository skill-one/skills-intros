# competitor-alternatives (`coreyhaines31/marketingskills/competitor-alternatives`)

## whitebox

- 先读产品营销上下文文件 (.agents/product-marketing-context.md, 旧版在 .claude/), 只向用户追问文件未覆盖的信息
- 初始评估: 摸清自家产品定位/差异化/定价/短板、竞争格局、本次目标 (SEO 流量 / 销售赋能 / 竞品用户转化)
- 深度调研竞品: 产品体验、各档定价与隐藏成本、评论挖掘 (G2 / Capterra / TrustRadius)、双向流失客户访谈、对方官网与 changelog
- 按搜索意图匹配 4 种页面格式之一 (竞品 alternative 单数 / alternatives 复数 / 我们 vs 竞品 / 竞品 A vs B), 按 SKILL.md 规定章节写页面: TL;DR → 对比表 → 分维度段落对比 → '谁适合谁' → 迁移路径 → CTA
- 输出三件套: 竞品 YAML 数据文件 + 完整页面内容 (URL / meta / 分节文案 / 表格 / CTA) + 按搜索量排优先级的页面集计划

- 上下文预读: 任务开始先查 product-marketing-context.md 文件, 用文件内容替代提问, 只问增量信息
- 集中式竞品数据 (单一事实源): 每个竞品一份 YAML 档案 (定位/定价/功能评分/优劣势/投诉主题/迁移注意事项), 数据结构见 references/content-architecture.md, 页面章节模板见 references/templates.md; 数据集中存放, 更新一次自动传播到所有对比页
- 诚实原则 + 评论挖掘 + SEO 映射: 从 G2/Capterra/TrustRadius 提炼好评与投诉主题, 页面必须承认竞品长处、明确写出双方'适合谁/不适合谁'; 每种格式绑定固定关键词表, 配内链 (竞品页互链 + hub 页) 与 FAQ schema
