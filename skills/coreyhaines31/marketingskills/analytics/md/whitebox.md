# analytics (`coreyhaines31/marketingskills/analytics`)

## whitebox

- 读上下文: 先检查 .agents/product-marketing.md (或旧版文件名) 是否存在, 有则直接复用, 不再重复提问
- 澄清需求: 确认用什么工具 (GA4/Mixpanel 等)、要追踪哪些关键动作、数据将支撑什么决策、谁来实施、有无隐私合规要求
- 设计追踪计划: 按规范命名事件, 逐条定义属性/触发点/转化, 只保留能指导决策的事件
- 实施埋点: 生成 gtag 事件代码或 GTM dataLayer 推送, 按需对接 GA4/Mixpanel/Amplitude/PostHog/Segment
- 验证交付: 用 GA4 DebugView + GTM Preview Mode 按校验清单核对 (触发正确/属性正确/无重复/无 PII), 输出追踪计划文档

- 决策驱动的事件筛选: 从'要回答什么问题/要做什么决策'反推需要追踪什么, 拒绝虚荣指标, 事件宁精勿多; 完整事件参考库查 references/event-library.md
- 命名与结构约定: 事件名小写下划线 object-action 格式 (如 signup_completed), 具体场景写进属性而非事件名 (如 cta_hero_clicked), 避免特殊字符与自动属性重复
- 外部工具依赖: 实现靠 GA4 (gtag.js) 与 Google Tag Manager (dataLayer 模式), 验证靠 DebugView/Preview Mode/Tag Assistant, 各平台集成入口走 tools/REGISTRY.md 注册表
