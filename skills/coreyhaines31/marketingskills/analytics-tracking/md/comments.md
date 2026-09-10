# analytics-tracking (`coreyhaines31/marketingskills/analytics-tracking`)

## comments

- user: 电商运营, category: 妙用, comment: 让它按命名规范生成全渠道 UTM 链接表，同事直接复制。以前 wechat/WeChat/微信 在报表里裂成三条，现在能合并统计了。
- user: 第一次埋点的独立开发者, category: 坑, comment: 一上来只说"帮我装 GA4"，装完才发现关键转化没埋。错在不先说目的：它问"这数据帮你做什么决策"时认真答，埋的事件才会真被用到。
- user: 市场部负责人, category: 坑, comment: 想回头分析去年哪个渠道拉新最有效，才发现来源属性根本没埋——没埋的数据永远补不回来。别等要做归因了才想起埋点。
- user: 投放优化师, category: 坑, comment: 网站同时装了 gtag 和 GTM，购买事件重复上报、转化翻倍。告诉它两套都装了，它定位出重复触发，删掉 gtag 基础代码才恢复。
- user: 出海律所运营, category: 注意, comment: 面向欧盟用户的话，务必先说清要合规，否则默认方案直接采集数据。提了 GDPR 后它才改成 consent mode：用户同意前先不收集。
- user: B 端产品经理, category: 启发, comment: "先列决策再埋点"改变了我的流程：先写下三个想回答的问题，再倒推事件，从 40 个砍到 12 个，报表反而更多人看了。
