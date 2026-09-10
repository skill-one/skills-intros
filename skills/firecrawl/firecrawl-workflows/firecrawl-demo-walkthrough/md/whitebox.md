# firecrawl-demo-walkthrough (`firecrawl/firecrawl-workflows/firecrawl-demo-walkthrough`)

## whitebox

- 从上下文推断产品 URL、流程重点、输出格式; 仅在被卡住时追问, 最多 1~3 个简短问题
- 用 Firecrawl 浏览器打开产品, 沿关键流程 (如注册、定价、仪表盘) 逐步导航, 每步做页面快照, 必要时抓取页面内容
- 按区域 (首页营销 / 注册引导 / 定价 / 文档 / 仪表盘 / 帮助支持) 并行派发子代理走查, 每条返回: 访问的屏幕、执行的动作、观察、摩擦点、来源 URL
- 汇总全部记录, 套用固定 Markdown 模板产出: 产品概览 → 分流程走查 → 关键发现 → 改进建议 → 访问页面列表 → 复跑参数

- 浏览器自动化: 依赖 Firecrawl 托管服务 (必须提供 FIRECRAWL_API_KEY), 核心操作是 navigate (导航流程) + snapshot (每步状态快照) + scrape (按需抓页面)
- 并行扇出: 最多 6 条区域路线由子代理并行执行, 返回统一字段结构 (screens / actions / observations / friction / source URLs), 保证可汇总比对
- 输出约束 + 安全闸: 结果强制套用固定模板并遵守质量标准 (屏幕/CTA/表单具体化、观察与观点分离、保留每个访问过的 URL); 未经用户明确指示和授权, 不提交真实凭据、不购买、不执行不可逆操作
