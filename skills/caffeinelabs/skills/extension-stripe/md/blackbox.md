# extension-stripe (`caffeinelabs/skills/extension-stripe`)

## blackbox

**function**: 给你的应用加上 Stripe 信用卡/借记卡收款功能: 从配置收款账户、管理商品, 到跳转付款和显示支付结果, 一整套线上支付能力。

- input: 管理员填入 Stripe 密钥和支持付款的国家列表 (如 ["US", "CA", "GB"]), output: 应用接入支付完成, 后续用户可直接用信用卡/借记卡付款
- input: 管理员添加/修改/删除一件商品 (名称、描述、价格、数量), output: 商品列表实时更新, 新商品立刻可以上架销售
- input: 顾客在商店里点击「购买」, output: 自动跳转到 Stripe 官方安全付款页, 付完后回到应用内的「支付成功」或「支付失败」页面
