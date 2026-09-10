# write-product-spec (`warpdotdev/common-skills/write-product-spec`)

## blackbox

**function**: 把一个功能想法变成一份说清楚「该做成什么样」的产品规格文档 (PRODUCT.md)，逐条列出可验证的行为规则和边界情况，让实现的人不用猜。

- input: 一段白话描述的功能想法，如「帮我写个规格：给标签页加悬停预览」, output: 一份 PRODUCT.md 文件，把功能行为写成编号、可逐条验证的规则，涵盖默认流程、加载/失败/空状态、悬停中途移开鼠标等边角情况
- input: 一个 Linear 工单号 (如 APP-1234) 或 GitHub issue 链接，附一句功能说明, output: specs/APP-1234/PRODUCT.md 规格文件，归档在该工单号对应的目录下，界面设计相关的会标注对应的 Figma 设计稿链接
- input: 一份已有的 PRODUCT.md 草稿，加上一条新决定，如「长表格改成横向滚动」, output: 更新后的规格：新行为写入对应条目，还没定论的点明确标成「Open question (待定问题)」而不是含糊带过
