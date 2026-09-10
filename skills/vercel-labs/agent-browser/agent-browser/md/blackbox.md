# agent-browser (`vercel-labs/agent-browser/agent-browser`)

## blackbox

**function**: 我像一个替你操作浏览器的助理:你说要做什么,我就在真实浏览器里打开网页、点按钮、填表单、截图、取数据,把结果交给你。

- input: 一个网址,如「打开 example.com 并截图给我看」, output: 整页或指定区域的截图图片
- input: 一句话任务,如「登录 XX 网站,把订单表单填好提交」, output: 操作完成的结果:已填/已提交的确认截图,以及关键信息摘要
- input: 「把这个商品列表页的价格都抓下来」, output: 整理好的数据表(如 CSV/表格),含商品名、价格等字段
- input: 「帮我测一下这个新上线的网页,看看有没有问题」, output: 一份体验报告:列出能正常用的功能和发现的问题(按钮失灵、报错、排版错乱等),附截图证据
