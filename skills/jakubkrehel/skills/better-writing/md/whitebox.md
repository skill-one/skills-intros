# better-writing (`jakubkrehel/skills/better-writing`)

## whitebox

- 勘察: 通读目标附近的既有文案, 记录产品术语、本地化惯例和已有文风/内容风格指南
- 对照原则清单逐项审查文案: 一个声音分档语气、朴素直白用词、动词开头的按钮、流程词汇一致、链接自述去向、统一大小写策略、开关标注 ON 状态、错误紧邻出错处并给出修法、空状态指明下一步、占位符仅作示例
- 按违反的原则分组输出报告, 按严重度排序, 每个根因一行表格: Severity | Location (path/to/file:line) | Before | After | Why
- 给出结论: 存在 HIGH 则 Block, 否则 Approve (剩余条目留表内作为待办); 若无发现, 声明 No actionable writing findings 并说明验证方式

- 纯静态源码审查, 零外部依赖: 不需要浏览器验证, 明确声明 Source alone is enough —— 逐条核对每个标签与其触发的动作、每条错误信息是否给出修法、术语与上下文文案是否一致; 不依赖任何外部工具/库/模型 API
- 规则引擎式的原则清单作评审基准: 内置分类规则表 (语气按风险分档、错误信息好坏对照表、空状态 HTML 范例等), 相邻能力划清边界 —— 标点/截断/大小写渲染归 better-typography, 错误标记与播报归 better-accessibility, 翻译空间归 better-layout, 均不属于本技能职责
- 严重度分级 + 放行门禁: HIGH (误导用户或掩盖错误恢复方式) / MEDIUM (破坏声音、术语、大小写一致性) / LOW (孤立措辞打磨); 规则: 有 HIGH 残留必须 Block, 且绝不 Approve 未实际检查的覆盖范围
