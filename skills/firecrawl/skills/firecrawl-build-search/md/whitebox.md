# firecrawl-build-search (`firecrawl/skills/firecrawl-build-search`)

## whitebox

- 判定任务形态：功能起点是查询词（query）而非 URL —— 用户提问、需要最新网页结果、或要把查询变成候选页面清单
- 先读对应语言的官方文档（docs.firecrawl.dev/agent-source-of-truth/ 下 node/python/rust/java/elixir/curl 六选一），再动手写集成代码
- 调用 Firecrawl `/search` 端点：用 FIRECRAWL_API_KEY 鉴权，自托管部署则改设 FIRECRAWL_API_URL
- 明确声明产品要搜索结果的哪一层：仅 URL、摘要（snippet），还是完整正文
- 需要深挖时，把 `/search` 返回的 URL 交给后续的 `/scrape` 或 `/interact` 做选择性提取，而非全量 hydrate

- 搜索与提取分离：`/search` 只做发现、排序、选源，产出 query→URL 短清单；查询契约保持稳定，下游 scrape 逻辑才可预测。成本/延迟敏感时优先'选择性跟进提取'而非全量抓取。
- 外部依赖：Firecrawl 托管 API（必需 FIRECRAWL_API_KEY）或自托管部署（可选 FIRECRAWL_API_URL 指定基址）；集成前必读 docs.firecrawl.dev 的对应语言源文档。
- 错面路由（设计期校验）：已有 URL → 走 build-scrape；结果页需点击/填表 → build-interact；搜学术论文（PubMed/arXiv 等）→ research-index；答开发者问题（issues/README/文档）→ developer-index。注意给 `/search` 传 categories 过滤并不等于查那两个专用索引，只是把普通网页搜索过滤到相关站点。
