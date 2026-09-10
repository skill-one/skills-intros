# firecrawl-company-directories (`firecrawl/firecrawl-workflows/firecrawl-company-directories`)

## whitebox

- 从上下文推断目录来源、筛选条件、目标数量、输出格式; 仅在被卡住时才问 1~3 个简短问题
- 制定采集计划: 需要筛选/翻页/无限滚动/点击详情页时用 Firecrawl browser; 公开静态列表直接用 scrape/map
- 逐页抓取并抽取可见字段 (name/description/industry/stage/funding/tags/profileUrl/websiteUrl), 不可见字段留空、不推断
- 质检: 去重、记录翻页进度、标注限流/登录墙/CAPTCHA
- 交付: Markdown 报告 (摘要/公司表/来源/复跑参数) 或按固定 JSON shape (source/filters/extractedAt/totalResults/companies[]) 输出

- 双模式采集: 通过 Firecrawl hosted API (需 FIRECRAWL_API_KEY) 执行 — 交互型目录走 browser (处理筛选、翻页、无限滚动、详情点击), 静态公开列表走 scrape/map
- 抽取守则: 只捕捉页面上可见字段, 不可得留空, 严禁推断 — 保证数据可溯源
- 结构化输出契约: Markdown 固定模板 + 统一 JSON shape (companies[] 内 12 个约定字段), 并附 rerun inputs 让任务可精确复跑
