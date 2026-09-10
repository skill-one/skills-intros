# performance (`addyosmani/web-quality-skills/performance`)

## whitebox

- 先测后改：读取测量流程 (references/MEASUREMENT.md)，建立真实用户数据 + 实验室基线（改动前快照）
- 用真实用户的 Core Web Vitals (p75) 定优先级，录一次 DevTools 性能 trace (性能轨迹)，用聚焦 insight 定位瓶颈成因
- 只改动与测量出的瓶颈相关联的代码/资源（图片、字体、JS、第三方脚本等对应模式）
- 在同等条件下重跑实验室测量，报告 before/after 数值、测试条件与不确定性（真实用户验证需等新数据积累）
- 若无可运行的页面：只做静态检查，结论一律标注为『假设』并附验证命令/浏览器操作步骤

- 测量路由：Chrome DevTools MCP 的 performance_start_trace 录轨迹 + performance_analyze_insight 分析聚焦洞察；明确不走 lighthouse_audit（那是非性能类目）。字段数据 (Field) 来自 CrUX 等真实用户来源，实验室指标 (Lab) 从 trace 中取 LCP/CLS/TBT/FCP/Speed Index
- 证据分级：真实用户 Core Web Vitals 用于 pass/fail 定优先级；本地 PerformanceObserver 片段不算真实用户数据；预算表（如 JS<300KB、总重<1.5MB）只是典型内容/电商页的初始护栏，已有项目预算优先保留
- 修复手段来自内置模式库，按瓶颈套用：关键渲染路径 (preconnect/preload/关键 CSS 内联)、图片格式选择与响应式 (AVIF/WebP)、字体加载 (font-display/变体字体)、缓存策略、避免布局抖动 (layout thrashing)、第三方脚本 facade 模式、View Transitions/Speculation Rules——只动测量关联处，不凭感觉优化
