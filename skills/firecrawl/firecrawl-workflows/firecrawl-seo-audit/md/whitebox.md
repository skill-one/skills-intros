# firecrawl-seo-audit (`firecrawl/firecrawl-workflows/firecrawl-seo-audit`)

## whitebox

- 从上下文推断站点 URL、目标关键词、输出格式; 只有被阻塞时才问 1~3 个简短问题 (skill 规定最多 3 个)
- 用 Firecrawl map 爬全站, 摸清 URL 结构
- 用 Firecrawl scrape 抓关键页面 (首页/产品/定价/文档/博客/高价值落地页), 提取 title、meta description、标题层级、内链、canonical、图片 alt 文本
- 若给了目标关键词, 搜索该关键词并抓取排名靠前的页面做竞品对比
- 并行跑完 4 条检查线后, 套固定模板输出含高/中/低优先级建议的 markdown 审计报告

- 外部依赖唯一: Firecrawl (托管 API, 需 FIRECRAWL_API_KEY), 提供 map (站点 URL 结构) 和 scrape (页面抓取) 两个动作; 所有结论基于抓取到的真实页面数据, 不凭空推断
- 并行分解: 用 sub-agents (或等价的并行任务运行器) 同时跑 4 条线 — Site Structure (URL 模式/死链/孤儿页)、On-Page SEO (title/meta/H1-H2/内容)、Keyword & SERP (关键词与竞品页面模式)、Technical Issues (死链/重复内容/缺 metadata)
- 输出与质量约束: 结果套固定 markdown 模板 (Executive Summary → Site Structure → On-Page SEO → Keyword Opportunities → 竞品对比 → Prioritized Recommendations → Sources → Rerun Inputs); 质量标准要求建议具体到精确改动、每个问题标注来源 URL、并区分技术发现与内容策略猜测
