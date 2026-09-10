# core-web-vitals (`addyosmani/web-quality-skills/core-web-vitals`)

## whitebox

- 确认输入形态: 可访问的 URL 则先读取性能测量工作流; 仅源码则只做成因推测、不下结论
- 查询 CrUX p75 真实用户数据定位不达标指标 (页面级数据缺失时明确标注回退到 origin 级)
- 在声明条件下用 Chrome DevTools MCP 录制一次加载/交互的性能 trace 作实验室证据
- 只分析与失败指标相关的 trace insights, 追溯到具体代码与资源, 按需读取 LCP/INP/CLS 参考文档实施修复
- 修复后重跑同等条件实验室测量验证; 不宣称字段数据立即改善 (CrUX/RUM 需新用户访问才有新数据)

- 字段优先判定: 以 CrUX p75 对照阈值 (LCP≤2.5s / INP≤200ms / CLS≤0.1) 确定优化目标; 依赖 Google CrUX / Search Console 作真实用户数据源, 单次实验室值不与 p75 直接对比
- trace 归因: Chrome DevTools MCP 的 performance_start_trace 采集实验室证据, 指标分开归因——LCP 查 TTFB/资源发现/渲染延迟, INP 拆输入延迟/处理/呈现延迟, CLS 定位位移节点与触发源; 性能诊断明确绕过 lighthouse_audit (仅限非性能类目), 无 DevTools 时回退 Lighthouse CLI / PageSpeed Insights
- 修复模式库 + 验证闭环: 按指标套用 preload+fetchpriority、内联关键 CSS、预留尺寸、Speculation Rules 预渲染、Next/React/Vue 框架速修等模式; 生产端采集推荐 web-vitals 库 (raw PerformanceObserver 未完整实现各指标的声明周期规则)
