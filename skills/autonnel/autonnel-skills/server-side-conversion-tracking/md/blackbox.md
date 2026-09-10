# server-side-conversion-tracking (`autonnel/autonnel-skills/server-side-conversion-tracking`)

## blackbox

**function**: 帮你把店铺的真实成交准确上报给 Facebook、TikTok、Google、Bing 等广告平台, 修好"实际卖了很多单、平台却少报"导致投放跑偏的问题。

- input: 你的店铺/落地页网址 + 广告平台的接入凭证 (如 Facebook 的 Pixel ID 和访问令牌), output: 打通后的转化回传: 广告平台后台开始收到带点击编号的购买事件, 少报的部分补上了
- input: 一段描述, 如: "Facebook 报了 40 单, 我们订单系统只有 25 单", output: 一份核对报告: 指出漏掉的订单丢在哪一环 (点击编号丢失、跨域名跳转、事件被重复计数), 附修复清单
- input: 广告平台后台的数据 + 最近 7 天的真实订单表, output: 对比分析: 平台数 vs 真实订单数是否稳定一致, 以及"点击编号覆盖率"这个健康指标, 告诉你能不能放心加预算
