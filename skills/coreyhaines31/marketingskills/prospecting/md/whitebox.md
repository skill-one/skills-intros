# prospecting (`coreyhaines31/marketingskills/prospecting`)

## whitebox

- Intake: 先查 .agents/product-marketing.md 复用已有上下文, 按销售对象分流到四条分支之一 (SaaS / B2B / Local SMB / Demand-signal); 缺失输入只问一次, 其余取合理默认值
- Phase 1 定 ICP: 产出一段式 ICP 陈述 + pass/fail 检查清单, 未完成不得进入发现阶段
- Phase 2 建候选池: 按 2~3 倍超量 sourcing, 用 2~3 个来源交叉验证 (B2B/SaaS: Apollo/ZoomInfo/LinkedIn; Local SMB: Google Maps + 浏览器辅助调研)
- Phase 3~4 审定与评分: 每条候选对照 ICP 清单打分, 附来源 URL 与置信级; 邮箱先过 Truelist 送达性验证; 按 Hot/Warm/Cold/Skip 分级 (Demand-signal 分支例外, 改用 0-100 需求契合度)
- Phase 5 交付: ≤25 行输出聊天表格, >25 行或用户要求则输出 CSV, 必附 Top outreach targets、搜索参数、未决问题

- 分支分流机制: 五阶段框架共享, 但分支决定数据源与'合格'的定义 — SaaS 看 technographic + 融资/招聘信号, Local SMB 看网站状态/距离/决策人可达性, Demand-signal 抛弃 firmographic、只认带引用的公开痛点证据且交付物变为证据报告
- 证据 + 送达性双重校验: 禁止无凭据断言 — 每条资格判定必须带来源 URL + 置信级, High 需两个独立来源确认; 邮箱未通过 Truelist 验证一律移入 invalid 桶不得进终表。外部依赖: Apollo/ZoomInfo/Clay/Clearbit (数据 enrichment)、Truelist (邮箱验证)、BuiltWith/Crunchbase (技术栈/融资信号)、Google Maps/浏览器 (Local SMB)
- 合规护栏前置: 每次执行先读 — 禁批量抓取 LinkedIn/Google Maps、禁绕过 CAPTCHA/登录墙、只用公开商务联系方式、每条联系人保留来源 URL + 日期作 lineage (GDPR/CAN-SPAM)、禁止按健康/财务/宗教等敏感属性定向
