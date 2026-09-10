# writing-great-skills (`mattpocock/skills/writing-great-skills`)

## blackbox

**function**: 帮你编写和修改 AI「技能说明书」(skill, 即告诉 AI 助手该怎么干活的规范文档), 让 AI 每次执行都稳定、不跑偏、不偷工减料。

- input: 一份已写好的技能说明书 (SKILL.md 文件或文本), output: 改好的精简版本 + 问题清单: 指出哪里重复啰嗦、哪里是 AI 本来就会做的废话、哪里会让 AI 提前收工
- input: 一句话需求, 如「我想做一个自动生成周报的技能」, output: 一份结构完整的技能说明书草稿, 包含何时触发、按什么顺序做、做到什么程度算完成
- input: 描述症状, 如「我的技能 AI 有时执行有时忽略, 结果还不稳定」, output: 诊断结论: 属于哪种典型毛病 (如说明书太长太散、规则互相重复), 以及对应的修改方案
