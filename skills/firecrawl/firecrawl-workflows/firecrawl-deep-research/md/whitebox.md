# firecrawl-deep-research (`firecrawl/firecrawl-workflows/firecrawl-deep-research`)

## whitebox

- 入口把关: 判断请求是否为「报告级研究任务」(需要正式书面报告、简短搜索答不了的复杂议题); 不匹配则拒绝触发 (文献综述类转交 firecrawl-research-papers, 快查类走常规方式)
- Onboarding 访谈: 问一个短问题确定运行时长, 映射到深度档位 — 几分钟→Quick / 10-15分钟→Thorough / 不限→Exhaustive; 题目不明时可再追问 1-2 个
- 按档位收集证据: 用 Firecrawl (CLI/MCP, 需 FIRECRAWL_API_KEY) 逐档执行 search + scrape — Quick 搜 3-5 个 query 抓 5-10 个源, Thorough 5-10 个 query 抓 15-25 个源, Exhaustive 10+ query 抓 25+ 个源 (含一手来源与反方观点); search 已返回全文的 URL 不重复抓取
- 并行研究: 按研究角度 (综述定义/技术细节/市场产业/反方风险/官方文档) 分派子代理, 每个返回「论断 + 源 URL + 来源质量 + 不确定性」
- 综合成稿: 按固定结构输出 markdown 报告 — Executive Summary / Key Findings / Detailed Analysis / Contrarian Views And Risks / Open Questions / Sources / Rerun Inputs

- 外部依赖: Firecrawl API (search 返回网页结果, scrape 抓取页面全文; 经 CLI 或等价 MCP 工具面调用, 凭 FIRECRAWL_API_KEY)。注意它只搜网页 — 不查论文索引, search 传 categories:["research"] 也只是把普通网页搜索过滤到研究机构网站
- 深度档位机制: 用户给出的运行时长被确定性映射为三档采集计划, 档位同时决定 query 数和抓取源数; 不同角度多 query 覆盖, 保证跨视角
- 去重与校验: search-with-scrape 已返回全文的 URL 不再重抓; 质量线要求事实性论断必须带来源引用、优先一手来源、显式标记不确定与冲突证据, 且做综合分析而非罗列抓取摘要
