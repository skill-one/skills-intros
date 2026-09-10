# claude-api (`anthropics/skills/claude-api`)

## blackbox

**function**: 把 Claude(Anthropic 家的 AI 大模型)接进你的项目:写好能直接跑的调用代码,也负责把旧代码迁到新模型、升级软件包、降低 API 账单。

- input: 一个还没用上 Claude 的 Python/TypeScript 文件 + 一句话需求(如"给这个客服脚本加上 AI 自动回复"), output: 改好的代码文件,拿来就能调 Claude 做对话、总结、分类
- input: 一条命令 `/claude-api migrate` + 旧代码所在的文件路径, output: 迁移到新模型后的代码,附一份改动清单:哪些参数已淘汰、各自替换成了什么
- input: 一段现有的 Claude 调用代码,或一条命令 `/claude-api cost-optimize`, output: 一份按省钱效果排序的优化清单:每条建议标明预计省多少、附可直接套用的代码修改
