# tavily-best-practices (`tavily-ai/skills/tavily-best-practices`)

## whitebox

- 定位需求: 按方法选择表, 把需求映射到五个方法之一 — search(搜网页) / extract(抓指定 URL) / crawl(爬全站) / map(发现站内链接) / research(端到端 AI 研究)
- 给出安装与初始化: pip install tavily-python 或 npm install @tavily/core, 客户端从 TAVILY_API_KEY 环境变量读密钥
- 按 Quick Reference 输出对应代码片段和关键参数 (如 max_results、search_depth、extract_depth)
- 需要完整参数、异步模式、框架集成时, 跳转到对应的 references/*.md 详细指南

- 需求→方法映射: 不选方法不写代码, 先用选择表分流 — 自定义 agent 用四基础方法, 开箱即用研究用 research()
- 参数硬约束校验: query ≤400 字符、extract 的 urls ≤20、chunks_per_source 1-5、search_depth 分档、research 的 model 三选 (mini/pro/auto)
- research() 为异步任务模式: 提交拿 request_id → 轮询 get_research() 直至 completed/failed 才取结果; 外部依赖为 Tavily REST API, 经官方 SDK (tavily-python / @tavily/core) 调用
