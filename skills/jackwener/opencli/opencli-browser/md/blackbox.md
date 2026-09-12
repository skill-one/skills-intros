# opencli-browser (`jackwener/opencli/opencli-browser`)

## blackbox

**function**: 你给我一个网址或一句「在网页上要做什么」, 我在真实浏览器里替你看页面、点按钮、填表单、取数据, 像一个替你动手上网的助手。

- input: 一个网址, 比如 https://example.com/news/123, output: 这个页面讲了什么的摘要, 或提取出来的正文/表格数据
- input: 一句任务: "帮我看看我邮箱里有哪些未读邮件" (浏览器已登录), output: 未读邮件的列表和要点, 不需要你亲手点开邮箱
- input: 一个待填写的网页表单页面 + 要填的信息 (姓名、日期、选项等), output: 已填好并提交的表单, 外加一份「实际填了什么」的确认
