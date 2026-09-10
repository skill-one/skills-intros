# firecrawl-build-scrape (`firecrawl/skills/firecrawl-build-scrape`)

## blackbox

**function**: 你给我一个网址和想要的页面信息, 我给你的应用程序写好「抓取该页面内容」的代码——拿到干净的正文、链接列表、截图或页面标题等信息, 直接可调用。

- input: 「我的应用要能把任意商品页网址变成干净的正文文本」, output: 一段能直接放进你项目里的代码——调用它并传入网址, 就拿到该页面的正文, 导航栏、广告等杂讯已被去掉
- input: 「从这个文档页 https://docs.example.com 把所有子页面链接都抓出来」, output: 调用后返回一个链接清单 (JSON 格式) 的代码, 你的程序可以接着逐个处理这些链接
- input: 「把 https://example.com/pricing 存成整页截图, 同时给我页面标题和描述」, output: 一张完整页面截图 + 页面标题与描述信息的代码, 保存图片并返回这两项数据
- input: 「我要定时检查某个页面内容有没有更新, 必须是最新版本」, output: 返回页面内容并附带「本次内容的抓取时间」的代码, 你的程序据此判断数据新旧
