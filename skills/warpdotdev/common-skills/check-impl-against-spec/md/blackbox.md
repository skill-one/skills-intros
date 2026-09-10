# check-impl-against-spec (`warpdotdev/common-skills/check-impl-against-spec`)

## blackbox

**function**: 在代码合并请求 (PR) 审查时, 对照事先写好的需求规格 (spec_context.md), 找出实际代码改动与规格的重大出入, 并把结论写进审查结果 review.json。

- input: 处于审查中的 PR + spec_context.md (需求规格) + pr_diff.txt (改动清单), output: review.json 审查结果: 只列出规格要求但没做到、或做法与规格矛盾的重大出入, 至少标记为 important 级别
- input: 规格里明确要求某项行为/校验步骤, 但改动里没有实现, output: review.json 中指出这条缺失, 并能对应到具体的改动代码行
- input: 实现和规格一致, 只有变量命名、代码结构等无害的小差异, output: review.json 不额外添加评论——完全对齐时不吹毛求疵
