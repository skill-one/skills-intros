# schema (`coreyhaines31/marketingskills/schema`)

## comments

- user: 独立博客站长, category: 妙用, comment: 一个页面用 @graph 同时挂 Article + FAQPage, 搜索结果里文章摘要和常见问题展开同时出现, 一次排版多占一块展示位, 博客流量白捡。
- user: 第一次加标记的新手, category: 坑, comment: 我把页面没展示的好评塞进 review 想凑星级, 直接被判内容不符。教训: schema 只能标页面上真实可见的内容, 别想着凭空加分。
- user: SaaS 独立开发者, category: 注意, comment: Product 页只写 name 和 image 拿不到带价格的富结果, offers 里的价格加库存是必填, 动手前先把这两个字段备齐。
- user: WordPress 老用户, category: 坑, comment: Rank Math 已经生成了 FAQ 标记, 我又手动加一份, 验证器报重复。先查插件生成了哪些, 只补它没覆盖的类型。
- user: React 前端, category: 注意, comment: schema 放在客户端组件里渲染, Rich Results Test 抓不到内容。挪到服务端输出到 head 后一次通过, 动态站先确认抓取端能看到。
- user: 做 AI 搜索优化的人, category: 启发, comment: 原以为 schema 只讨好 Google, 补全 Organization 和 FAQ 后发现 AI 搜索也能更准确引用我的页面, 一次投入两头受益。
