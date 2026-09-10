# writing-skills (`obra/superpowers/writing-skills`)

## blackbox

**function**: 把你的经验、规矩、工作方法写成 AI 能一看就懂、照做不出错的"技能说明书", 并在交付前先验证 AI 真的会照着做。

- input: 一段口头描述的做法, 比如 "我要求 AI 改完代码必须先跑测试再说完成", output: 一份可直接安装的技能文档 (SKILL.md), AI 装上后就会遵守这条规矩
- input: 一个已有技能的文件路径 + 一句吐槽, 比如 "AI 总是跳过核对需求这一步", output: 改好的技能文档, AI 不再钻这个空子
- input: 一份写好但还没启用的技能文档, output: 一份验证结果: 没装时 AI 会怎么犯错、装上后是否照做、还有哪些漏洞要堵
