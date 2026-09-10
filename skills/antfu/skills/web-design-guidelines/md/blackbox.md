# web-design-guidelines (`antfu/skills/web-design-guidelines`)

## blackbox

**function**: 审查网页前端代码, 找出影响用户体验和可访问性的问题, 逐条给出带文件行号和修改建议的报告。

- input: 一个前端代码文件路径, 如 src/pages/Login.tsx, output: 问题清单, 每条标注文件和行号, 如「Login.tsx:23 按钮缺少文字, 屏幕阅读器读不出内容」, 并附具体修改建议
- input: 一个文件匹配模式, 如 "src/components/**/*.jsx", output: 该模式覆盖的所有文件逐个审查后汇总成的一份问题报告, 按文件分组列出不符合最佳实践的地方
- input: 直接把一段组件代码贴进对话, output: 逐条指出不合规之处, 如「点击区域太小」「文字对比度不足, 看不清」「键盘 Tab 无法操作到该控件」, 并说明怎么改
