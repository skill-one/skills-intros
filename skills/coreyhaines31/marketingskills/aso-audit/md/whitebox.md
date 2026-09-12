# aso-audit (`coreyhaines31/marketingskills/aso-audit`)

## whitebox

- 从 URL 识别商店类型 (apps.apple.com / play.google.com, 只有 app 名则 site: 搜索定位), 用 WebFetch 抓取 listing 页, 按平台字段清单逐项提取元数据
- 对 listing 页整页截图评估视觉资产 (图标/截图数量与文案/视频) — WebFetch 拿不到图片
- 判定品牌成熟度 tier (Dominant / Established / Challenger), 决定后续评分松紧
- 按 6 个加权维度各打 0-10 分 (Visual 25%, Title 20%, Ratings 20%, Description 15%, Metadata 10%, Conversion 10%), 加权求和得百分制总分
- 套用 report-template.md 输出报告: 分数卡 + Top 3 快速改进项 + 逐维度问题与具体修法 + 关键词建议 + 按影响/成本排序的行动计划

- 双平台 schema 分叉: Apple 与 Google Play 字段清单、字符限制 (标题/副标题 30 字符, Google 短描述 80、全描述 4000) 和索引规则不同 — Apple 长描述不进搜索索引、Google 全描述是强索引信号, 直接决定两侧优化策略不同
- Tier 评分修正: 扣分前先问「这是错误, 还是头部团队的数据知情选择」— Dominant 级 app 的品牌名标题/无视频/通用更新日志不扣分, Challenger 则严格按教科书 ASO 标准
- 外部依赖: WebFetch 抓 listing (客户端渲染拿不全时标记缺口、请用户补贴关键字段), 浏览器截图工具取视觉资产, 评分标准与平台规格来自 references/ 下 4 个规格文件 (scoring-criteria / apple-specs / google-play-specs / benchmarks)
