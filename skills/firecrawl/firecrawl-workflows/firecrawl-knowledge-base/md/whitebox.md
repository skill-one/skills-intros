# firecrawl-knowledge-base (`firecrawl/firecrawl-workflows/firecrawl-knowledge-base`)

## whitebox

- 确认输入: 从上下文推断来源 (URL/主题)、目标、深度、输出位置, 信息齐全立即开工, 缺了才追问 (最多 1~3 个简短问题)
- 制定采集计划: 文档站用 Firecrawl map 摸清站点结构, 主题类语料用 Firecrawl search 搜来源, 逐页 scrape 成 markdown
- 并行执行: 用子代理 (或等效并行任务) 分工 — 按文档章节、按来源类型 (官方文档/教程/社区讨论/参考), 或按任务 (抓取 → 切块 → 生成清单)
- 按输出模式落盘: 四种模式 Reference / RAG / Training / Docs-mirror 各自产出对应文件 (index.md + sources.json / chunk 文件 + manifest.json / training-data.jsonl / 完整镜像 + 目录)
- 交付最终说明: 一份知识库文档, 含摘要、输出结构、覆盖范围、用法建议、来源 URL 和重跑参数

- 外部依赖只有 Firecrawl 托管服务 (需 FIRECRAWL_API_KEY), 三个核心能力: map (发现站点页面结构)、search (按主题找来源)、scrape (把页面抓成 markdown); 不调用任何模型 API
- 存储约定: 按 Firecrawl download 风格写入 .firecrawl/<hostname>/<path>/index.md; 质量标准是保留代码示例与表格格式、剔除模板化导航、来源 URL 写入 frontmatter 或元数据
- 模式驱动的产物切换: 同一份抓取结果按 goal 分叉 — RAG 模式追加 chunk 文件 + manifest.json, Training 模式追加 training-data.jsonl + training-metadata.json, Reference 模式只要 markdown + sources.json
