# tavily-best-practices (`tavily-ai/skills/tavily-best-practices`)

## comments

- user: 后端老兵, category: 妙用, comment: 搜技术问题我用 include_domains 锁官方文档域名, 再 exclude_domains 排掉 SEO 内容农场, 一次配置结果质量立升, 比翻十页谷歌快多了。
- user: 第一次用的新手, category: 坑, comment: 抄示例直接 TavilyClient() 报错缺 key, 折腾半天才发现要先设置 TAVILY_API_KEY 环境变量, 设好再初始化就通了。
- user: 数据工程师, category: 注意, comment: extract() 一次最多传 20 个 URL, 我一把塞 50 个直接被拒, 改成每批 20 个循环调用才跑完, 新手别学我。
- user: AI 应用开发者, category: 注意, comment: research() 是异步的, 调完不会马上出结果, 要拿返回的 request_id 每隔约 10 秒轮询 get_research(), 我第一回还以为程序卡死了。
- user: 独立开发者, category: 妙用, comment: 先 map() 拿整站 URL 列表, 挑出真正要的几页再 extract(), 比直接 crawl 全站省不少额度, 站点越大越明显。
- user: 产品经理转做AI, category: 启发, comment: model 拿不准就用 auto, 但我后来固定: 日常聚焦问题用 mini, 竞品分析这种大活才上 pro, 一个月账单降了不少。
