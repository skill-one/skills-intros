# product-marketing (`coreyhaines31/marketingskills/product-marketing`)

## blackbox

**function**: 帮你把产品的定位、目标客户、竞争优势、品牌语气等营销基础信息, 整理成一份固定的说明文档 (保存在 .agents/product-marketing.md), 以后做任何营销内容都能直接引用, 不用每次从头介绍你的产品。

- input: 给我一个代码仓库的访问权限 (或一句「帮我看看我的项目, 整理产品定位」), output: 一份自动起草的产品营销背景文档 (.agents/product-marketing.md), 涵盖产品简介、目标客户、痛点、竞品、差异化等, 等你逐项确认和纠正
- input: 一段对话式描述, 如「我的产品是给中小餐厅用的预约系统, 客户主要是老板」, output: 一份完整的 .agents/product-marketing.md 文档, 我会一段一段提问补全, 直到信息足够准确
- input: 已存在的 .agents/product-marketing.md + 一句修改指令, 如「定位从『邮件工具』改成『送达率平台』, 目标客户加上销售运营」, output: 更新后的文档: 版本号自动 +1, 底部追加一行变更记录 (改了什么、为什么), 历史记录原样保留
- input: 现有文档路径 + 「帮我看看现在写了啥」, output: 当前文档的内容摘要, 包括现在处于哪个版本、最近几次改了什么, 再问你想更新哪些部分
