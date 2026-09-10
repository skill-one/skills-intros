# page-cro (`coreyhaines31/marketingskills/page-cro`)

## whitebox

- 先读上下文: 探测 .agents/product-marketing-context.md (旧版在 .claude/ 下), 已覆盖的信息不再向用户追问
- 识别三要素: 页面类型 (homepage/landing/pricing/feature/blog/other)、主要转化目标、流量来源
- 按影响权重依次分析 7 个维度: 价值主张清晰度 → 标题 → CTA → 视觉层级/可扫读性 → 信任背书 → 异议处理 → 摩擦点
- 命中对应页面类型的专属子框架 (如落地页要求单一 CTA、定价页要求方案对比)
- 按固定结构输出: Quick Wins → 高影响改动 → A/B 测试假设 → 备选文案 (标题/CTA 各 2~3 条带理由)

- 上下文前置加载: 优先从文件系统读产品上下文文件, 缺失时才向用户提 5 个任务特定问题 (现有转化率、流量来源、后续流程、用户研究数据、已尝试方案)
- 分类分发: 先判定页面类型再套子框架; 超范围问题按规则路由给关联技能 (signup-flow-cro / form-cro / popup-cro / copywriting / ab-test-setup)
- 无外部依赖: 不调用任何外部工具、库或模型 API — 纯提示词层方法论, 实验清单等扩展内容来自本地引用文件 references/experiments.md
