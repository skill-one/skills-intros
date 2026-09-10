# paywalls (`coreyhaines31/marketingskills/paywalls`)

## whitebox

- 先探测并读取项目内产品营销上下文文件 (.agents/product-marketing.md 等三种路径), 已覆盖的信息不再追问
- 用诊断问题确认三类背景: 升级场景类型 (freemium/试用到期/功能门/用量限制)、免费与付费的边界、用户旅程及 paywall 出现时机
- 按四条核心原则 (先给价值再开口、展示而非说教、无摩擦升级路径、尊重拒绝) 选定 paywall 类型与触发/频率策略
- 输出具体方案: 按内置模板填充文案 (7 组件: 标题/价值演示/功能对比/价格/社会证明/CTA/退出选项), 覆盖 3 种 paywall 类型
- 附 A/B 测试变量与追踪指标; 若需求超出范围 (定价页、取消挽留、新手引导), 转介对应的相关 skill

- 上下文注入: 启动时按优先级探测 `.agents/product-marketing.md` / `.claude/product-marketing.md` / 旧版 `product-marketing-context.md`, 读到则直接吸收, 只追问缺口
- 模板驱动生成: 内置 3 类 paywall 文案骨架 (功能锁/用量上限/试用到期) 和固定 7 组件屏幕结构, 输出是按模板+四原则填充, 不是自由发挥
- 零外部依赖: 无任何工具/库/模型 API 调用, 纯 prompt 逻辑; 仅引用一个本地扩展文件 references/experiments.md (实验点子库), 外溢需求靠 4 个相邻 skill (cro/onboarding/churn-prevention/ab-testing) 做路由
