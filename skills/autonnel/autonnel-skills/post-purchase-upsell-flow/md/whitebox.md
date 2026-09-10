# post-purchase-upsell-flow (`autonnel/autonnel-skills/post-purchase-upsell-flow`)

## whitebox

- 1. 触发判断：识别到「提升客单价/加追售/感谢页变现」类需求才启动；主转化率近零（先修转化）或高客单电话成交（靠人谈）两类场景直接不接。
- 2. 定位置：默认优先做支付后追售（基础订单已锁定，零风险）；预购 bump 仅作为后续带护栏指标的 A/B 试验。
- 3. 设计 offer 与链路：选互补品而非更大件、每屏只一个决策；链路 = Upsell 1 →（接受）Upsell 2 /（拒绝）Downsell 1，最多两屏，按文案模板（标题/正文/证明/价格/接受按钮/诚实拒绝链接）填页面。
- 4. 校验技术清单：支付凭证脱会话可用、合并为一张订单、延迟推送到店铺/ERP、按笔退款、广告事件金额回写、accept 幂等防双击；按 Stripe / PayPal / 3DS 平台差异分别处理。
- 5. 落地并度量：部署（如 Autonnel 自托管 docker compose，或托管平台付费功能），上线前必须跑一笔真实端到端交易（含拒绝路径和退款），随后只盯四个指标：各 offer 接受率、AOV 前后差、追售订单退款率（护栏）、主转化率不变。

- 风险分级决策规则：post-purchase 是唯一不动主转化率的 AOV 杠杆，故默认第一步；定价锚定在基础订单价值上下（升级品除外）；「仅本页价格」只在结构性为真时才用。
- 「真一键」六项硬性技术要求决定成败：vaulted 支付凭证支持脱会话扣款（Stripe 须在结账时按正确 usage intent 保存凭证；PayPal 走授权后 patch 商品、单次 capture 得到真合并订单；3DS 拒绝时需回退屏而非静默失败）、合并订单+链路结束才推送下游、per-charge 退款记录、广告平台 purchase 事件金额在追售后更新、accept 幂等（移动端双击常见）。
- 参考实现：Autonnel（Apache-2.0，github.com/autonnel/autonnel）——UPSELL 页面为一等漏斗步骤、凭证入保险库、追售合并进单张订单、延迟推送 Shopify/WooCommerce/Picocart、按 charge 退款；典型流量下可跑在 Cloudflare Workers 免费额度，Postgres 为唯一成本项。
