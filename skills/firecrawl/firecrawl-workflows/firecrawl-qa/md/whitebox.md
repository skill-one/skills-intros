# firecrawl-qa (`firecrawl/firecrawl-workflows/firecrawl-qa`)

## whitebox

- 确定参数: 从上下文推断目标 URL、测试焦点 (full/forms/navigation/responsive/performance) 和输出格式, URL 明确则直接执行
- 发现页面: 用 Firecrawl map 摸清站点页面结构, 用 Firecrawl scrape 抓取页面内容与链接
- 交互测试: 用 Firecrawl browser 执行表单交互、导航跳转、响应式和人工检查
- 并行测试: 按焦点拆分子代理 (tester) 并行跑各模块, 每个 tester 返回 severity、URL、描述、证据、复现步骤
- 汇总交付: 合并去重后输出统一 QA 报告 (健康分、C/M/m 三级问题、正面观察、已测页面清单)

- 外部依赖: 全程依赖 hosted Firecrawl 服务 (需 FIRECRAWL_API_KEY), 三个能力各司其职——map (页面发现) / scrape (内容与链接抓取) / browser (真实交互)
- 并行子代理架构: 按 5 种焦点各有一组固定 tester (如 Full = 导航链接 + 表单交互 + 内容视觉 + 错误状态), 每个 tester 按统一结构 (severity/URL/描述/证据/复现步骤) 回传, 便于机器化汇总
- 质量门控: 报告走固定 markdown 模板 (health score x/10, [C]/[M]/[m] 严重度分级); 功能性问题必须附复现步骤, 无证据的推测性 bug 不上报, 跨 tester 结果去重
