# amazon-product-research (`nexscope-ai/amazon-skills/amazon-product-research`)

## whitebox

- 触发: 用户提出产品调研/验证请求 (如 "Research wireless earbuds") → 进入固定五步工作流
- Step 1-2 市场与竞争: 用 web_search 按查询模板采集搜索量、品类趋势、季节性、竞争密度、头部品牌、价格带、评论分布
- Step 3-4 需求验证与利润: web_fetch 拉取 Google Trends 页面确认趋势, web_search 查 Alibaba 供货价, 套用利润框架算净利率
- Step 5 准入评估: 评估启动资金、MOQ、合规认证 (如 FDA)、上架时间与差异化空间
- 评分输出: 8 因子加权求和得 1-10 综合分, 按固定模板输出结构化报告或对比表, 并给出 Go/No-Go 建议

- 数据采集仅靠两个外部工具: web_search (执行带关键词模板的检索, 如 "[product] site:amazon.com") 与 web_fetch (直接拉取 Google Trends URL); 不接任何专有/付费数据 API, 因此销量与价格均为公开数据估算值
- 评分引擎: 8 因子加权合成总分 — 需求 25%、竞争 20%、利润 20%、准入 15%、增长 10%、差异化 5%、季节性 3%、风险 2%; 每个因子及总分均有预设 1-10 打分锚点 (rubric), 总分映射三档策略: ≥7 ✅ 建议跟进 / 4-6 有条件推进 / ≤3 不建议
- 利润模型: 固定成本占比模板 (商品成本 ~40%、亚马逊佣金 15%、FBA 按规格浮动、头程 5-10%、营销 10-20%、退货杂项 5%) 计算净利, 目标净利率 ≥20%; 输出端为固定报告模板 (完整报告 / 多产品对比表二选一)
