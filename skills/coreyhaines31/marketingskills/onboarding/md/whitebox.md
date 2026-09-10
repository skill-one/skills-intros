# onboarding (`coreyhaines31/marketingskills/onboarding`)

## whitebox

- 匹配触发词 (激活率 / aha moment / 注册后不用 / onboarding flow 等) 后加载本 skill.md
- 先查 .agents/product-marketing.md (或 .claude/ 同名文件、旧文件名) 是否存在, 有则先读, 只追问未覆盖的信息
- 初始评估: 收集 3 项 — 产品类型与核心价值、激活定义 (aha moment)、当前流失点; 缺什么就问 skill.md 内置的 5 个任务问题
- 设计或诊断: 用核心原则 (MPTV、单次会话单目标、Do Don't Show、进度激励) + 心理学机制 + 10 组件工具箱产出方案
- 按固定格式输出 (审计: Finding→Impact→Recommendation→Priority; 设计: 激活目标/流程/清单/空状态文案/邮件触发器/指标), 超出范围的议题路由给关联技能 (signup/emails/paywalls/ab-testing)

- 上下文优先注入: 输出任何建议前先探测 3 个固定路径的 product-marketing.md 读作背景, 再把用户输入 diff 到 Initial Assessment 的 3 个维度上, 只补缺口, 避免重复提问
- 知识转换全靠本地 markdown, 无外部 API/库/模型调用: references/minimum-path-to-value.md、activation-models.md、experiments.md 按需引用, 结论统一转成结构化模板 (漏斗公式 Signup→Step→Activation→Retention 带百分比、10 组件表、按产品类型的模式表)
- 校验走指标闭环: 每条建议绑定可度量指标 (激活率 / 到达时长 / D1/7/30 留存), 按漏斗最大跌幅定优先级, 改动包装成可 A/B 的实验
