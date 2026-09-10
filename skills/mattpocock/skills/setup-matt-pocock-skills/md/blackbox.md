# setup-matt-pocock-skills (`mattpocock/skills/setup-matt-pocock-skills`)

## blackbox

**function**: 给你的代码仓库做一次性初始化配置：问清几个选项后写好配置，让这套工程技能家族（拆工单、分诊、写规格等）从此知道在哪跟踪问题、用什么标签、去哪读项目文档。

- input: 在一个远程仓库指向 GitHub 的项目里说「帮我初始化工程技能配置」, output: 一串带推荐答案的选择题（逐题点头即可），确认后仓库里多出几份配置文件，项目说明书（CLAUDE.md 或 AGENTS.md）里多出一节「Agent skills」速查清单
- input: 回答「不用 GitHub，问题就用仓库里的 markdown 文件来记」, output: 配置里写明问题以 .scratch/ 目录下的文件形式管理，之后「把方案转成工单」的技能会直接往那里生成工单
- input: 告知「我的 issue 标签有自己的一套叫法」（例如 bug:triage），并报出现有标签, output: 配置按你现有的叫法做映射，之后自动打标签的技能直接沿用，不会另建一套重复标签
