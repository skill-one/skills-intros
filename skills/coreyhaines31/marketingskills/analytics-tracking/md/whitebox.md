# analytics-tracking (`coreyhaines31/marketingskills/analytics-tracking`)

## whitebox

- 先读 .agents/product-marketing-context.md 获取产品上下文, 只追问缺失信息
- 评估三方背景: 数据要支撑什么决策、现有埋点、技术栈与隐私合规要求
- 从问题倒推设计追踪计划: 事件名、属性、触发点、转化目标
- 落地实现: GA4 (gtag.js) 或 GTM (dataLayer.push) 埋点, 配 UTM 参数命名规范
- 用 GA4 DebugView / GTM Preview Mode 按验证清单逐项核对, 交付追踪计划文档

- 事件建模规范化: 统一 '对象-动作' 命名 (小写下划线, 如 signup_completed), 上下文放 properties 而非事件名; 标准属性按 page/user/campaign/product 分组, 禁止 PII
- 双实现通道: GA4 用 gtag('event', ...) 直接上报 (支持 MCP 集成); GTM 走 dataLayer.push → 触发器 → 标签 三段式; 另有 Mixpanel/Amplitude/PostHog/Segment 的实现指南可切换
- 校验闭环: GA4 DebugView / GTM Preview Mode / Tag Assistant 实时调试, 按清单验证事件触发正确、属性取值、无重复、无 PII; 细节查 references/ 文档库 (event-library, ga4-implementation, gtm-implementation)
