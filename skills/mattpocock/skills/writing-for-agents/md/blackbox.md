# writing-for-agents (`mattpocock/skills/writing-for-agents`)

## blackbox

**function**: 帮你写好、改好那些给 AI 助手看的「说明书」——比如技能文档 (skill)、AGENTS.md、CLAUDE.md——让 AI 每次照着做都稳定靠谱。

- input: 一份已写好的 skill.md 草稿, output: 改好的版本: 冗余内容被精简, 歧义步骤写得更明确, 并附上具体改了什么、为什么
- input: 一段话描述, 如「我想让 AI 每次提交代码前自动检查测试和格式」, output: 一份可直接使用的技能文档或 AGENTS.md 文件, 交给 AI 后它就知道何时触发、照什么规则做
- input: 一份越来越长、AI 总跑偏的 CLAUDE.md, output: 瘦身后的版本: 常驻内容只留关键规则, 次要细节挪到需要时才查的独立文件, 并说明拆分理由
