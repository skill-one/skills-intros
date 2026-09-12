# momentic-explore-prompt (`momentic-ai/skills/momentic-explore-prompt`)

## blackbox

**function**: 为使用 Momentic 自动测试的代码仓库生成一份「探索提示文件」(explore-prompt.md), 让自动测试机器人明确该测哪个网站、用什么网址、怎么登录、生成的测试存到哪里, 从而产出又准又不乱放的测试。

- input: 一个用 Momentic 做自动测试的代码仓库, output: 一份可直接使用的 explore-prompt.md, 写清每个前端应用要测试的网址、登录方式、生成的测试文件应存放的文件夹
- input: 仓库的 momentic.config.yaml 和 CI 配置文件路径 (以及一句「生成的测试总连错地址」), output: 修订后的 explore-prompt.md, 网址改为测试真正运行时的线上地址, 而不是开发时用的本地地址
- input: 一份已有的 explore-prompt.md + 「机器人总把测试存错位置 / 忘了登录」的反馈, output: 改写后的 explore-prompt.md, 带上明确的存放路径硬性规则 (HARD RULE)、登录模块名称, 以及这个仓库特有的注意事项
