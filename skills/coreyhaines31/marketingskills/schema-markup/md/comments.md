# schema-markup (`coreyhaines31/marketingskills/schema-markup`)

## comments

- user: 独立站卖家, category: 坑, comment: 只填名称和图片就上线, 报缺 offers, 搜索里一直不显示价格; 补上 price 和库存状态才出. 要星级还得加 aggregateRating.
- user: React 前端, category: 坑, comment: JSON-LD 写在纯客户端组件里, 本地正常, 上线后测试工具读不到脚本; 改服务端渲染、让 script 进服务器返回的 HTML 才生效.
- user: 内容博客主, category: 坑, comment: 照模板抄了 FAQ schema, 页面却没放这些问答, Search Console 警告『内容与标记不符』. 规矩: 页面上看得见的问答才能标记.
- user: 企业官网管理员, category: 妙用, comment: 首页要放 Organization、WebSite、面包屑三套数据, 我用 @graph 合并成一个 script, 以后只维护一处, 测试工具一次全验证.
- user: 活动运营, category: 注意, comment: Event 日期我写「6月5日晚8点」一直报错; 换成 2025-06-05T20:00 这种格式秒过. 链接也必须带 https:// 的完整地址.
- user: SEO 外包老兵, category: 启发, comment: 结构化数据不提排名, 只是让结果带星级、价格、问答折叠, 醒目才换来点击. 心态从堆代码变成如实描述页面, Search Console 增强报告每周必看.
