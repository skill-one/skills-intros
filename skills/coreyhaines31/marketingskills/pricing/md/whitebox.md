# pricing (`coreyhaines31/marketingskills/pricing`)

## whitebox

- 读上下文: 先找产品营销上下文文件 (.agents/product-marketing.md / .claude/ 下同名文件 / 旧版文件名), 已覆盖的信息不再重复问
- 补缺口: 就业务类型、核心价值与竞品定价、现有指标 (转化率/ARPU/流失率)、优化目标 (增长/收入/利润) 向用户提问
- 匹配路径: 按需求套用对应框架 — 新定价 ($10/$100/$1000 经验值起步)、价值指标选择、分层打包、Van Westendorp 调研、涨价流程、定价页 teardown
- 查参考文档: 深层细节读取 references/ 下的文档 (pricing-models, tier-structure, research-methods, teardown 十维评分细则)
- 输出结果: 给出建议/评分/按优先级排序的修复项; 涉及落地实现时标注转交技能 (schema, ai-seo, cro, copywriting 等)

- 上下文前置: 靠文件存在性决定是否提问, 减少往返; 纯文件读取, 无外部依赖
- 框架+文档驱动: 所有判断与输出来自内置框架 (定价三轴、涨价的四类信号、价值指标选择法) 与 references/ 文档, 不调用任何外部模型 API
- 唯一外部依赖: teardown 的 "paste test" 需把定价页交给可联网的 AI (Perplexity / 开搜索的 ChatGPT / Claude) 问"套餐和价格是什么", 属启发式验证而非证明; Product/Offer 结构化数据的实现转交 schema 技能
