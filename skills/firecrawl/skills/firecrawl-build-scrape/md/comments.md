# firecrawl-build-scrape (`firecrawl/skills/firecrawl-build-scrape`)

## comments

- user: 第一次用的新手, category: 坑, comment: 我以为每次都抓到最新页面, 结果监控到的是缓存的旧价目表。要实时就把 maxAge 设 0, 再看 metadata.cacheState 确认数据来路。
- user: 前端转全栈的新人, category: 注意, comment: 它只管『给网址抓这一页』, 我一开始想让它自己找页面, 白忙一场。先有 URL 再用, 没网址请换配套的搜索功能。
- user: AI 应用开发者, category: 妙用, comment: 抓文档页喂 LLM 时开 onlyMainContent, 导航和页脚噪音全没了, token 立省一截, 摘要质量也更稳。
- user: 运维老哥, category: 妙用, comment: 内网数据不能出门, 把 FIRECRAWL_API_URL 指到自部署实例就行, 业务代码一行没改, 只动了环境变量。
- user: 做监控服务的后端老兵, category: 坑, comment: 抓 JS 渲染的仪表盘, 默认配置拿到空壳 markdown, 点开啥都没有, 加上等页面渲染完再取, 内容才齐。
- user: 做数据清洗的分析师, category: 启发, comment: 抓取成功不等于信息仍有效。我抓到过还在线的已关闭招聘页——『页面能返回』和『事情还成立』是两码事, 业务侧得自己判断。
