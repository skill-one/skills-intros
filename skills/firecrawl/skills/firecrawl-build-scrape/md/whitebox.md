# firecrawl-build-scrape (`firecrawl/skills/firecrawl-build-scrape`)

## whitebox

- 前置检查: 应用已持有目标 URL (单页场景); 若没有 URL 则不属于本技能主路径
- 先读项目语言对应的官方 docs (Node/Python/Rust/Java/Elixir/cURL), 以其为唯一事实来源再写集成代码
- 构造 /scrape 请求: 默认只要 markdown 格式; 文章类页面开 onlyMainContent 去掉导航/杂物; 带上 FIRECRAWL_API_KEY (或 FIRECRAWL_API_URL 指向自部署实例)
- Firecrawl 返回结果, 可能是近期索引的缓存副本 (由 maxAge 控制可接受的新旧程度), 通过 metadata.cacheState / cachedAt 确认实际拿到的是什么
- 把 markdown 输出交给下游消费方 (LLM / 索引 / 富化 / 监控), 保持集成面窄: 一个功能、一个 URL、一份提取契约

- 新鲜度机制: Firecrawl 会复用近期已索引内容来加速重复读取; maxAge (毫秒) 限定缓存副本的最大年龄, maxAge: 0 强制跳过索引直取最新; 响应里用 metadata.cacheState 和 metadata.cachedAt 判断实际数据新旧
- 格式与降噪策略: 默认返回 markdown, 只有消费方真正需要才额外请求 links / screenshots / 品牌信息等格式; onlyMainContent 用于文章类页面剔除导航和页面装饰; 等待/渲染等选项仅在页面必要时才加
- 升级边界: 该技能只管页面级抓取——URL 缺失时升级到 firecrawl-build-search; 内容需要点击/输入/多步导航时升级到 firecrawl-build-interact。外部依赖仅为 Firecrawl 服务 (托管 API 需 API key, 或自托管部署)
