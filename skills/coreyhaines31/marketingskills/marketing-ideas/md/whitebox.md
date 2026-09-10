# marketing-ideas (`coreyhaines31/marketingskills/marketing-ideas`)

## whitebox

- 先检查项目里是否已有产品营销上下文文件 (.agents/product-marketing.md / .claude/product-marketing.md / 旧版 product-marketing-context.md), 有则读取, 避免重复提问
- 上下文缺关键信息时, 追问三件事: 产品、目标受众、当前阶段
- 按用户情况 (阶段/预算/时间线) 从 139 个点子库中筛出 3~5 个最相关的
- 对选定的点子, 按固定格式输出落地方案: 为什么适合 / 怎么起步 (前 2~3 步) / 预期效果 / 所需资源 (时间、预算、技能)
- 需要深挖某个点子时, 加载对应 reference 文件 (如游击营销 #121 的完整框架 + 品牌案例库)

- 分类索引 + 查找表匹配: 139 个点子按 16 个类别编号 (内容 SEO #1-10、付费广告 #23-34、产品驱动增长 #87-96 等), 再叠加阶段 (pre-launch→scale)、预算 (free→high)、时间线 (quick wins→long-term) 三张实施技巧表做筛选; 全量清单在 references/ideas-by-category.md, 单点子深度文档在 references/guerrilla-marketing.md
- 纯本地知识文件, 零外部依赖: 不调用任何外部 API、库或模型 —— 全部 '数据' 就是 skill 包内的 markdown 参考文件
- 结构化输出约束 + 转介机制: 每条推荐必须含 五字段 格式; 用户要的是具体渠道执行 (广告/邮件/SEO 等) 时, 转介给关联 skill (programmatic-seo、emails、free-tools、referrals 等) 而非自己硬做
