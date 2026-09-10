# ai-seo (`coreyhaines31/marketingskills/ai-seo`)

## whitebox

- 先读产品营销上下文文件 .agents/product-marketing.md (兼容 .claude/ 路径与旧版文件名); 不存在则只追问四类上下文: 当前 AI 可见度、内容与域名、目标、竞对格局
- AI 可见度审计: 对 10~20 个关键查询在 Google AI Overviews / ChatGPT / Perplexity 实测, 记录'自己是否被引用、被引用的是谁'
- 逐页做可提取性检查 (定义块、40-60 词答案块、对比表、FAQ、schema、更新时间), 并解析 robots.txt 确认各家 AI 爬虫未被 Disallow
- 按三大支柱出优化方案: Structure 可提取结构 / Authority 引用+统计+专家署名 / Presence 第三方阵地 (Wikipedia、Reddit、评测站等)
- 落地机器可读层 (llms.txt、pricing.md、OKF 目录); schema 结构化数据的具体实现转交 schema skill

- 上下文前置与缺口追问: 触发后先找并读取产品营销上下文文件, 只补问文件未覆盖或任务特有的信息 — 纯本地文件读取, 无外部依赖
- 清单驱动审计: 查询×平台矩阵表 + 逐页 pass/fail 可提取性检查表 + robots.txt 爬虫规则解析 (GPTBot/ChatGPT-User、PerplexityBot、ClaudeBot/anthropic-ai、Google-Extended、Bingbot); agent-readiness 评分依赖外部工具 `npx is-agentic` 或 Frase checker; 可用 DevTools 抓取 ChatGPT 的真实后台 fan-out 查询
- 参考文件路由 + 技能委托: 深度细节按需加载 references/*.md (platform-ranking-factors、content-patterns、agent-readiness、okf、format-volatility、youtube-ai-citations); 本体不直接调用模型 API — 平台测试靠真实查询, 平台源选择逻辑与 GEO 研究数据 (+40%/+37%/+30%) 内置于文档
