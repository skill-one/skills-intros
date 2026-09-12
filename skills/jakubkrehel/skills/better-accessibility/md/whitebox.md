# better-accessibility (`jakubkrehel/skills/better-accessibility`)

## whitebox

- 两轮走查: 先纯键盘走完所有流程 (不用鼠标), 再用屏幕阅读器走一遍 (每个控件播报名称、角色、状态)
- 按核心规则清单逐项核对: 原生元素优先、:focus-visible 焦点环、完整键盘支持、最小命中区、表单标签、动态内容播报、替代文本、标题结构与 200% 缩放
- 验证: 有浏览器 → 按 Tab 顺序走流程、从无障碍树读取实际名称/角色、逐站确认焦点指示器、跑自动审计; 无浏览器 → 做静态检查, 没跑过的检查一律标 Not verified
- 输出: 发现按违反的原则分组、按严重度排序, 每个根因一行表格 (Severity | Location | Before | After | Why)
- 判定: 存在 HIGH → Block; 否则 Approve; 无发现 → 报告 "No actionable accessibility findings" 并附验证方式

- 原生优先语义判定: 能用原生元素就不写 ARIA —— <button> 管操作、<a href> 管导航 (必须支持 Cmd/Ctrl/中键新开页), 禁止 <div onClick>; 宁可不用 ARIA 也不用错 ARIA, 不确定时做减法 (删 ARIA) 而非加
- 双通道验证: 浏览器通道依赖无障碍树 (读计算出的 accessible name/role) + 自动审计工具; 静态通道核对可访问名称、非原生控件的键盘处理、焦点样式、prefers-reduced-motion 守卫、label-input 绑定。外部依赖: 浏览器、WCAG 标准 (如 2.5.8 命中区) 与 ARIA APG 交互模式、包内参考文档 (semantics-and-aria.md、focus-and-keyboard.md 等); 不调用任何外部模型 API
- 严重度分级 + 范围转交: HIGH=阻断任务/屏蔽辅助技术/系统性失败, MEDIUM=交互明显变难, LOW=局部打磨, 任一 HIGH 未修即 Block; 越出本技能范围的发现不自行修改, 转交姊妹技能 —— 对比度与配色→better-colors, 字号与 iOS 输入缩放→better-typography, RTL 布局→better-layout
