# revops (`coreyhaines31/marketingskills/revops`)

## whitebox

- 预检上下文: 先找产品营销上下文文件 (.agents/product-marketing.md / .claude/product-marketing.md / 旧文件名 product-marketing-context.md), 命中则先读入
- 收集任务上下文: GTM 模式 (PLG/销售主导)、ACV、销售周期、现有工具栈、现状与目标; 信息不全不阻塞, 用已有输入先干, 缺口标注出来
- 按问题域匹配内置框架: 生命周期阶段/MQL 定义/评分/路由/管线阶段/Deal Desk/数据清洗/指标看板, 原则是先定义后自动化、每个交接环节有 SLA
- 交付 5 份可独立实施的文档: 生命周期定义、评分规格 (打分点+MQL 阈值)、路由决策树、管线配置、指标看板规格; 已知 CRM 时附平台特定实施指南

- 文件驱动的上下文预检: 三个候选路径按序探测上下文文件, 读入后只追问未覆盖的部分——避免重复收集用户已给信息
- 模板外置按需加载: 详细模板不在主文件里, 按需引用 references/ 下的四个子文件 (lifecycle-definitions / scoring-models / routing-rules / automation-playbooks), 实施细节再指向 tools/REGISTRY.md 下各平台指南
- 量化基准作为参照系: 所有建议附带内置 benchmark 表校准 (如 MQL→SQL 30-50%、speed-to-lead <5分钟、pipeline coverage 3-4x、LTV:CAC 3:1); 运行时不调用任何外部 API——HubSpot/Salesforce/Clearbit/Apollo 等仅以集成文档形式被引用, 本身无运行时依赖
