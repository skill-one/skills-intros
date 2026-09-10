# referral-program (`coreyhaines31/marketingskills/referral-program`)

## whitebox

- 触发匹配: 用户请求命中 description 中的关键词 (referral / affiliate / word of mouth / refer a friend 等) 即激活; 若是「上线期的病毒传播」则显式转交相邻技能 launch-strategy, 不越界
- 读上下文: 先查本地文件 .agents/product-marketing-context.md (旧版为 .claude/ 路径), 有则直接采用, 只补问未覆盖的信息
- 收集缺口: 上下文不足时按固定清单提问, 仅 4 类 — 项目类型 (推荐制/联盟, B2B/B2C, LTV, CAC)、现状、产品可分享性、资源与预算
- 套框架产出: 按「推荐闭环 = 触发时刻→分享→被推荐者转化→奖励→循环」设计方案, 配激励结构选择、问题-修复对照表、健康度与业务指标
- 按需深挖: 遇到细节需求时指向拆分文件 — references/program-examples.md (激励案例)、references/affiliate-programs.md (联盟计划)、tools/integrations/*.md (Rewardful/Tolt/PartnerStack 等工具接入指南)

- 关键词路由: description 字段就是触发词表, 匹配即激活; 边界外任务 (launch 相关病毒性) 写明了移交对象, 保证只做推荐/联盟增长
- 文件式上下文注入: 用读本地 markdown 上下文文件代替重复提问, 降低交互成本; 无文件时才按 4 类清单发问
- 渐进式披露 + 纯本地依赖: 主文件只保留框架/清单/检查表, 深度内容拆到 references/ 与 tools/ 引用文件按需加载; 依赖全部是本地文件引用, 不调用任何外部 API 或模型
