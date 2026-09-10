# launch (`coreyhaines31/marketingskills/launch`)

## whitebox

- 触发: 用户提到 launch / Product Hunt / beta / early access / waitlist / GTM 等发布类意图
- 读上下文: 优先读取 .agents/product-marketing.md (或 .claude/ 下同名文件、旧版 product-marketing-context.md), 只追问上下文未覆盖的信息
- 过 Readiness Gate: 用 SLC 清单 (简单/可爱/完整) 校验产品是否值得发布, 先判定属于『隐身模式』还是『再加一个功能』哪种失败模式
- 出方案: 按 ORB 渠道框架 (自有/租用/借用) + 五阶段发布流程 (内测 → Alpha → Beta → Early Access → 全量) 生成阶段化计划
- 收尾: 视需要补充 Product Hunt 打法、发布日 checklist、上线后运营动作 (onboarding 邮件、对比页、维持热度)

- 上下文注入: 开工前先读产品营销上下文文件作为已知输入, 避免重复提问——这是唯一的输入解析步骤; 本 skill 是纯方法论, 不执行代码、不调用外部模型 API
- 校验先行 (Readiness Gate): SLC 三项检查作为发布前置校验, 不通过就不跑五阶段机制, 而是给出『砍范围到 SLC』或『直接发布』的分流判断
- 框架转换: 把用户处境映射到两套结构化框架输出计划——ORB (Owned/Rented/Borrowed 三类渠道) + 五阶段发布; skill 中提到的外部工具 (SparkToro/Listen Notes 查受众重叠、Navattic 做交互式 demo、Introw 管渠道伙伴分成、Product Hunt/BetaList/HN 作为发布平台) 是给用户的操作建议, 不是我的运行依赖
