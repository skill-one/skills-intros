# skill-development (`anthropics/claude-code/skill-development`)

## blackbox

**function**: 帮你把一个想法或一段经验做成 Claude Code 插件的"技能包"(skill)——一份能让 AI 按你的套路稳定干活的说明书;也能诊断和修好写得不灵的现有技能。

- input: 一句需求, 如「我想让 Claude 每次都按我们公司的模板写周报」, output: 一个可直接放进插件的技能文件夹(含 SKILL.md 说明书), 装好后 Claude 遇到「写周报」就会照你的规范执行
- input: 一个写好但不好用的 SKILL.md 文件路径, output: 改好的文件 + 改动说明: 比如触发词更准了(以前说「整理文档」不触发, 现在会), 正文从 8000 字精简到 2000 字
- input: 一句抱怨, 如「我的 skill 总是没被触发, 或者触发后干得乱七八糟」, output: 一份诊断报告: 指出问题在哪(如触发描述太模糊、内容太臃肿), 并直接给出修复后的版本
