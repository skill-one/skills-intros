# firecrawl-competitive-intel (`firecrawl/firecrawl-workflows/firecrawl-competitive-intel`)

## whitebox

- 推断输入: 从上下文推断竞品清单、关注点 (pricing/features/changelog)、采集频率与输出格式; 仅在被卡住时追问, 最多 1~3 个问题
- 制定采集计划: 对每个竞品列出目标页面 — 定价页 (含年/月切换、展开的功能表)、功能/产品页、changelog/博客/发布说明, 必要时带上权限的 dashboard
- 并行采集: 按竞品或关注点拆成多个子研究员并行跑, 每个研究员统一返回定价档位、功能、近期变更、来源 URL 和置信度
- 组装交付: 按固定 markdown 模板输出报告 (Alerts / 逐竞品拆解 / 横向对比 / 后续建议 / Sources / 复跑参数); 若要求结构化, 则输出约定字段的 JSON

- 外部依赖 Firecrawl (API key: FIRECRAWL_API_KEY): scrape 抓静态页, browser 处理需交互的动态页 — 切换年/月定价、展开功能表、访问登录后的 dashboard (仅限有合法访问权限时)
- 并行分解机制: 用 sub-agents (子代理) 做'每竞品一个研究员'或'每关注点一个研究员'的分片, 各研究员返回统一结构 (定价/功能/变更/URL/置信度) 便于汇总
- 质量与可复跑约束: 只提取真实的计划名、限额、日期; '联系销售'等门控信息标注为 gated 而非猜测; 保留来源 URL, 供下次运行做 diff 对比
