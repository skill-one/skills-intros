# firecrawl-workflows (`firecrawl/firecrawl-workflows/firecrawl-workflows`)

## whitebox

- 从用户请求推断工作流、输入、受众和产出格式；只有缺失输入会阻塞时才追问，最多 1~3 个问题，够用就立即开工。
- 按交付物类型匹配子工作流（研究报告、文献综述、SEO 审计、QA 报告、线索清单、知识库等 15 个），都不契合则走通用流程。
- 通过 Firecrawl（CLI 或等效工具面，需 FIRECRAWL_API_KEY）采集网页证据，保存并引用来源，保证结论可追溯。
- 相互独立的调研单元（如一个竞品 / 一个页面 / 一类来源各一个研究员）交给子代理并行执行。
- 综合成最终交付物：执行摘要 + 证据基础 + 用户要的分析产物 + 建议 + 可复跑输入（rerun inputs）。

- 意图路由：以『要什么交付物』为键把请求映射到 15 个子工作流之一（website-design-clone、research-papers、deep-research、seo-audit、lead-research、qa、competitive-intel 等）；无匹配时回退到通用流程，并产出可沉淀为新 skill 的复用模式。
- 双证据管线：普通研究走网页证据（Firecrawl 托管 API 抓取）；文献综述走 Firecrawl 论文索引（PubMed、bioRxiv、medRxiv、arXiv 摘要、可直达全文），专门避开普通网站搜索。
- 并行分发与溯源：给每个并行单元统一的交接信息（工作单元、URL/检索词、期望提取字段、输出格式）；所有来源保存或引用，最终交付物中附带证据基础以供核查。
