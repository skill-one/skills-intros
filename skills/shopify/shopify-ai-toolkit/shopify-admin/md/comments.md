# shopify-admin (`shopify/shopify-ai-toolkit/shopify-admin`)

## comments

- user: 后端老兵, category: 妙用, comment: 接手老项目里一堆祖传查询, 我直接贴给它逐字段解释: 哪个参数能省、哪个字段早没人用了。改代码前心里就有底, 比翻文档快得多。
- user: 第一次用的新手, category: 坑, comment: 我以为它能直接连上店铺把查询跑出数据, 结果它只负责写和解释 GraphQL, 真正执行要走 Shopify CLI。先分清分工再开工, 别像我一样卡半天。
- user: 钉死旧版API的店铺开发者, category: 注意, comment: 我们的 app 锁在旧 API 版本上, 它默认按最新稳定版生成, 字段会对不上。开口先报版本号 (比如 2024-10), 生成的结果就准了。
- user: 做会员定期购的电商开发, category: 注意, comment: 「订阅」分两种别搞混: 给 app 本身收费不归它管; 顾客买货的定期购 (selling plans) 归它管。我第一句就问错了对象, 白绕一圈。
- user: 外包全栈, category: 坑, comment: 把 shopify.app.toml 贴过去想验配置, 它明确说这归 CLI 的 config validate 管。GraphQL 的活它接得很爽快, 但边界要先记牢。
- user: 独立开发者, category: 启发, comment: 以前我写 mutation 全靠先跑一次看报错再改, 它是先生成、先校验再给我。我才意识到自己一直拿线上当校验器, 这个习惯真得改。
