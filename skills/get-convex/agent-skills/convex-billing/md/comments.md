# convex-billing (`get-convex/agent-skills/convex-billing`)

## comments

- user: 第一次接支付的全栈新手, category: 坑, comment: 在 Stripe 后台忘了加 webhook 端点, 用户付款成功了 isSubscribed 却一直 false。第 7 步的 Dashboard 配置千万别跳过。
- user: 独立开发者, category: 坑, comment: 上线没设 SITE_URL, 用户付款后被跳回 localhost:3000, 差点以为被骗来投诉。部署前先把 SITE_URL 写进 Convex 环境变量。
- user: 照抄官方 demo 的前端, category: 坑, comment: convex.config.ts 里 import 顺手写了 .ts 后缀, push 直接报错。必须用 .js 结尾, 打包器的硬要求, 踩一次就记住了。
- user: 兼职运维的 SaaS 创始人, category: 注意, comment: 测试和正式是两套密钥: 换成 sk_live_ 时, STRIPE_WEBHOOK_SECRET 也要回 Dashboard 重新生成替换, 不然事件全部验签失败。
- user: 后端老兵, category: 妙用, comment: 以前手写 webhook 验签又长又容易错, 这边 registerRoutes 自动搞定, 我只管在事件列表里勾全 customer.subscription 和 invoice 相关项。
- user: 被白嫖怕了的产品经理, category: 启发, comment: 订阅判断只走服务端 isSubscribed 查询, 状态存在组件自己的表里, 前端根本碰不到。我再也不敢把订阅状态放 localStorage 了。
