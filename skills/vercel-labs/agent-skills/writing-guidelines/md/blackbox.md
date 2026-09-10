# writing-guidelines (`vercel-labs/agent-skills/writing-guidelines`)

## blackbox

**function**: 给你的文档、文案做「写作规范体检」——找出不符合写作指南的地方, 并精确到文件和行号告诉你怎么改。

- input: 一个文档文件路径, 如 docs/getting-started.mdx, output: 一份问题清单, 每条形如 getting-started.mdx:12 ——「这里用了第一人称复数, 应改为第二人称」, 逐条指出违规点和位置
- input: 一组文件, 如 docs/**/*.md (批量模式), output: 所有匹配文件的问题清单, 按文件和行号排列, 一眼看到每个文档哪里要改
- input: 不指定文件, 直接说「审查 docs 目录」, output: 先问你要审查哪些文件, 然后给出对应的检查结果
- input: 一段粘贴过来的英文文案, output: 指出这段文字哪里不符合写作风格指南 (如语气、用词、句式), 并给出修改建议
