# firecrawl-build-search (`firecrawl/skills/firecrawl-build-search`)

## comments

- user: 独立开发新手, category: 坑, comment: 传 categories:['research'] 给 /search, 拿到的只是过滤到学术站的普通网页, 没有 arXiv 摘要。真要查论文请走 research-index。
- user: AI 问答产品开发者, category: 妙用, comment: 只对 /search 返回的前两三条抓全文, 其余留标题加 snippet 做引用来源, 成本和响应时间都砍了一大截, 别全量抓正文。
- user: 后端老兵, category: 注意, comment: 先想清楚搜索结果要 snippet、URL 还是全文再写接口, 我们默认全抓正文, 又慢又贵。查询入参也要保持稳定, 下游抓取逻辑才不用天天改。
- user: 全栈工程师, category: 妙用, comment: 我把 /search 当管道第一环: 先搜出候选网址, 再用 scrape 抓内容, 碰到要点按钮、填表单的页面就切 interact, 基本没再抓空过。
- user: 客服机器人维护者, category: 坑, comment: 让机器人答 "怎么配置 XX" 这类开发问题, 加 categories:['developer'] 拿到的仍是普通网页, 不是 issue 原文。搜 issue 和 README 要走 developer-index。
- user: 做竞品调研的产品经理, category: 启发, comment: 以前竞品调研先开十几个标签页, 现在固化成流程: 一句话查询 → 网页短名单 → 挑重点深挖。多数调研缺的不是内容, 是来源发现。
