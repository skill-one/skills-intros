# firecrawl-knowledge-ingest (`firecrawl/firecrawl-workflows/firecrawl-knowledge-ingest`)

## whitebox

- 从上下文推断门户 URL、输出格式、登录需求、页数上限; 仅受阻时追问 1~3 个简短问题
- 用 Firecrawl 浏览器打开门户, 检查导航, 识别分区、侧边栏链接与文章 URL
- 跟随分页/加载更多/搜索逐页抓取: 内容转 markdown, 抽取元数据 (标题、分区、更新日期、作者、标签)
- 公开 URL 用 Firecrawl map 补充发现; 登录门槛或重 JS 页面仍走浏览器导航
- 组装交付: 按固定 JSON 结构输出文章与元数据, 附摘要、分区统计、失败页、来源与重跑参数

- 抓取引擎: 依赖 Firecrawl 托管服务 (需 FIRECRAWL_API_KEY), 浏览器处理 JS 渲染与登录; Firecrawl map 仅作公开 URL 的补充发现手段
- 内容清洗: 抓取后统一转 markdown, 剥离导航/页眉/页脚, 保留代码示例、表格与格式
- 结构约定: JSON 固定为 source/url/extractedAt/totalArticles/sections[], 文章含 title/url/section/content/metadata; 逐页跟踪进度与失败, 失败页单独报告
