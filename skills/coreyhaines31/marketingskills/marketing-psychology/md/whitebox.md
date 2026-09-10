# marketing-psychology (`coreyhaines31/marketingskills/marketing-psychology`)

## whitebox

- 触发词匹配: 用户请求含 psychology / mental models / cognitive bias / anchoring / scarcity / nudge 等关键词时激活本 skill
- 读产品上下文: 若存在 .agents/product-marketing.md (或 .claude/ 同名文件、旧版 product-marketing-context.md), 先读入再作答, 用于定制到具体产品和受众
- 选模型: 按情境从内置心智模型库 (基础思维/买家心理/说服/定价/设计交付/增长 6 大类, 50+ 条) 中筛选适配条目
- 套模板输出: 每个模型依次给出 心理学原理 → 具体营销应用 → 伦理实施建议

- 关键词路由 + 边界转交: description 中的触发词表决定是否激活; 超出范围的请求按 description 尾注分别转交兄弟 skill (页面心理应用→cro, 定价策略→pricing, 文案框架→copywriting)
- 双段式知识模板: 内置模型每条固定为 '模型原理 + 营销应用' 结构, 回答即按情境套用, 并强制附加伦理约束 (如 scarcity 仅在真实稀缺时使用, defaults 仅在合乎伦理时使用)
- 外部依赖: 无外部工具、库或模型 API; 唯一外部输入是可选的本地上下文文件 product-marketing.md, 缺失则按通用情境作答
