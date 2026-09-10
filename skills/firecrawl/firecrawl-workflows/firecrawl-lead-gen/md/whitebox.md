# firecrawl-lead-gen (`firecrawl/firecrawl-workflows/firecrawl-lead-gen`)

## whitebox

- 从上下文推断目标人群、数据源、数量与输出格式; 目标清晰就直接开工, 只有被卡住才追问最多 1~3 个简短问题
- 制定采集方案: 需要筛选、搜索表单、翻页或登录的数据库走 Firecrawl 浏览器, 公开源直接用 search/scrape
- 按可用条件施加过滤器: 角色、公司规模、行业、地域、融资阶段、技术栈
- 抓取可见字段: 姓名、职位、公司、网址、地点、行业/规模/融资等; 邮箱、电话、LinkedIn 仅在可见/允许时才采
- 去重、标注被遮蔽或付费墙的字段, 按 Markdown + JSON/CSV 输出最终交付

- Firecrawl 托管浏览器 (依赖 FIRECRAWL_API_KEY 调用托管服务): 负责操作带筛选器、搜索表单、翻页或登录的数据库; 公开源则退化为 search/scrape, 不需要浏览器
- 合规提取原则: 只抓公开可见或合法可访问的数据, 被遮蔽/不可用/付费墙字段明确记入 Data Gaps, 不绕过验证码或访问控制
- 固定交付结构: Summary (来源、过滤条件、数量、注意事项) + Leads 表格或 JSON/CSV + Data Gaps + Rerun Inputs (可复跑参数), 并对线索去重
