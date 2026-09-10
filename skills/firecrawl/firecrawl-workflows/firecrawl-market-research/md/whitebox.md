# firecrawl-market-research (`firecrawl/firecrawl-workflows/firecrawl-market-research`)

## whitebox

- 从用户上下文推断研究目标 (市场/公司、数据焦点、时间范围、输出格式); 目标不清晰时最多追问 1~3 个简短问题, 清晰则直接开工。
- 制定 Firecrawl 采集计划: 静态内容 (市场报告、新闻、投资者关系页、SEC 文件、财报) 用 search + scrape; 有图表/标签页/时间选择器等交互的页面切换到 browser。
- 用 sub-agents (子任务并行器) 并行执行五条工作线: 公司财务、市场指标、行业趋势、新闻与分析师评论、来源校验。
- 把各路结果装配进固定 markdown 模板: Market Overview → Company Profiles → Comparison Tables → Trends And Outlook → Sources → Rerun Inputs。
- 按质量标准收尾: 交叉核对关键数字、标注来源间冲突数据、每个指标带周期和单位, 不提供投资建议。

- 采集层完全依赖 Firecrawl (托管版, 需 FIRECRAWL_API_KEY): search 做检索, scrape 抓静态页, browser 处理需要交互的金融门户/图表页。
- 并行化: 将研究拆为独立子任务 (financials / metrics / trends / news+analyst / source validation) 分发给并行任务运行器, 各自产出后汇总。
- 输出与质量控制: 强制 markdown 模板保证结构一致; Sources 段落保留 URL + 提取数据 + Rerun Inputs 保证可复跑; 交叉验证数字, 冲突数据显式标注, 指标强制带周期与单位。
