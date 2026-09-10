# web-quality-audit (`addyosmani/web-quality-skills/web-quality-audit`)

## whitebox

- 确定审计目标: 代表性 URL、关键状态与流程、公开/登录态、移动/桌面范围
- 页面可运行时, 先采集最小实测基线 (性能 trace / Lighthouse), 再大范围查源码
- 用运行时失败缩小源码检查范围; 实测发现与仅代码推断的假设分开记录
- 按用户影响和置信度分级 (Critical~Low), 给出具体修复建议
- 重跑等价的自动化检查和受影响的手动流程, 报告已验证项与待验证项

- 证据先行: 优先真实浏览器测量 — Chrome DevTools MCP (performance_start_trace 采 Core Web Vitals 与 LCP/INP/CLS 见解, lighthouse_audit 覆盖无障碍/SEO/最佳实践/Agentic Browsing, take_snapshot/evaluate_script 查渲染后可访问性树); 降级用 Lighthouse CLI 或 PageSpeed Insights; 真实用户数据用 CrUX; 聚合分数不当作质量证明
- 实测与代码分离: 运行时失败用于定位源码检查点, scripts/analyze.sh 仅作快速源码冒烟测试而非渲染页审计的替代; 代码假设标注为假设
- 分级复核闭环: 按 Critical/High/Medium/Low (用户影响+置信度) 输出结构化报告, 修复后重跑同条件自动化检查, 区分实验室实测、手动检查与仍待真实场景 (field) 验证的项
