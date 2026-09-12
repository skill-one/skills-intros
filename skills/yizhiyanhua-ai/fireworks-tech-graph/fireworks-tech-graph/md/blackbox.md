# fireworks-tech-graph (`yizhiyanhua-ai/fireworks-tech-graph/fireworks-tech-graph`)

## blackbox

**function**: 你用大白话描述想要的技术图 (架构图、流程图、时序图、云部署图), 我交给你画好的图片文件: 可选高清 PNG、可缩放浏览的离线网页、或会动的 GIF。

- input: 一段文字: 「画一张微服务架构图, 用户请求先到网关, 再分发给订单服务和支付服务, 都连同一个数据库」, output: 一张画好的 SVG 矢量图, 以及可直接插入文档/PPT 的高清 PNG 图片
- input: 一段文字: 「画个下单流程图: 用户下单 → 扣库存 → 支付 → 发货, 其中支付失败会退回库存」, output: 带箭头、分支和标注的流程图 PNG, 每个步骤和判断分支都清晰可读
- input: 一张已经画好的架构图, 加一句「让它动起来」, output: 一个 GIF 动图, 数据沿箭头流动, 直观展示请求怎么在系统里跑
