# accessibility (`addyosmani/web-quality-skills/accessibility`)

## whitebox

- 用 Chrome DevTools MCP 对已渲染页面跑 Lighthouse 无障碍审计 (公开页用移动端导航模式, 需保留登录/用户态时用快照模式)
- 拿审计返回的失败节点直接定位到具体组件/模板, 而不是全仓库搜通用写法
- 检查渲染后的无障碍树快照 take_snapshot (名称/角色/状态/地标/标题层级), 并用键盘实际走一遍受影响的流程
- 修改源码完成修复
- 重跑同一条审计 + 重做同样的手动交互, 验证修复

- 证据链驱动: 自动扫描优先用 Chrome DevTools MCP 的 lighthouse_audit (返回失败节点的渲染位置), 工具不可用时退回 Lighthouse CLI 或 axe-core (npx @axe-core/cli); 明确认知自动化只覆盖部分障碍, 100 分 ≠ WCAG 合规, 结论 = 审计失败节点 + 人工检查双证据
- 规则基座是 WCAG 2.2 的 POUR 四原则与 A/AA/AAA 合规级别, 修复套用固定模式: 原生元素 (button/input/a) 优先于 ARIA、图标按钮补可访问名称 (aria-label)、对比度阈值 4.5:1 (正文) / 3:1 (大字) 且焦点样式同样 ≥3:1、:focus-visible 焦点指示、aria-live/role=alert 播报动态错误
- 回归闭环: 修复后重跑同一审计与手动清单 (键盘 Tab + Enter/Space、读屏 VoiceOver/NVDA、200% 缩放、24×24px 最小触控目标), 不以分数下结论, 以同一标准复核
