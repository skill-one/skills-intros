# public-relations (`coreyhaines31/marketingskills/public-relations`)

## whitebox

- 先查产品上下文文件 (如 .agents/product-marketing.md), 已有的信息不再追问用户
- 根据请求意图 (newsjack / 找记者 / 回 HARO / 播客备战…) 路由到 references/ 下对应的工作流模块
- 按该模块的框架执行: 如 story angle 三选一、记者名单按 checklist 打分、套回应模板起草
- 产出 pitch 前过 7 项质量门禁, 任一项不过即不发、返工

- 文件级上下文注入: 触发后优先读 .agents/product-marketing.md (回退 .claude/ 同名路径与旧文件名), 用已有产品信息替代重复提问
- 关键词意图路由: 主文档本质是路由表, 真正流程分散在 6 个 references/*.md (newsjacking / journalist-pitching / story-angles / press-platforms / media-outlets / podcast-guest-prep), 按触发词加载对应模块
- 硬校验门禁 + 外部依赖: pitch 必过 7 项 checklist (≤150 词、主题行能预测标题、禁用 revolutionary/game-changing 等词、ask 明确…); 研究记者依赖 dev-browser 抓其近 5 篇文章, 入站提问来自 HARO/Qwoted/Featured 平台
