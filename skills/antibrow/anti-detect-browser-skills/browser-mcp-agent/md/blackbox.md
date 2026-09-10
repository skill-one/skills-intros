# browser-mcp-agent (`antibrow/anti-detect-browser-skills/browser-mcp-agent`)

## blackbox

**function**: 我能给 AI 助手配一个真实浏览器, 让它自己打开网页、点击、填表、登录, 替你完成需要"动手操作网页"的任务。

- input: 一条网址 + 「告诉我这个页面写了什么」, output: 页面正文的文字摘要, 或一张页面截图
- input: 「登录我的后台, 看看今天的订单数」, output: 直接的答案 (如「今天 37 单」); 且下次再问时仍是登录状态, 不用重复登录
- input: 「在这个页面的表单里填上这些信息并提交」, output: 提交完成的确认, 以及提交后页面的返回结果
