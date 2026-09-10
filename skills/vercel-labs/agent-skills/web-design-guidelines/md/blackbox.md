# web-design-guidelines (`vercel-labs/agent-skills/web-design-guidelines`)

## blackbox

**function**: 给你的网页/前端代码做一次"体检", 找出用起来不舒服、不合规的地方 (如看不清、点不了、无障碍缺陷), 并精确告诉你问题在哪。

- input: 一个前端页面代码文件的路径, 如 src/checkout/page.tsx, output: 一份问题清单, 每条精确到「文件:行号」, 如 「page.tsx:42 — 按钮没写 type, 可能误触发表单提交」
- input: 一整个前端项目目录 (如 src/**/*.tsx) + 一句「帮我 review 一下 UI」, output: 逐文件列出的审查报告: 哪里交互不对、哪里对键盘/读屏用户不友好、哪里违反常见网页设计最佳实践
- input: 「帮我检查无障碍 (accessibility)」+ 相关组件代码, output: 只针对无障碍问题的一份发现列表, 每条含具体位置和改法建议, 不报没问题的部分
