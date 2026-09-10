# google-agents-cli-adk-code (`google/agents-cli/google-agents-cli-adk-code`)

## comments

- user: 第一次写 Agent 的新手, category: 坑, comment: 跳过 `agents-cli scaffold create` 直接抄示例写代码, 项目缺配置跑不起来, 白折腾一晚。先 scaffold 再动手, 老项目用 `scaffold enhance .`。
- user: 后端老兵, category: 妙用, comment: 本想手写 Docker 沙箱让 agent 跑用户代码, 翻 samples.md 发现有现成 recipe, 克隆下来读它的 AGENTS.md 再改造, 半天搞定。先查目录再造轮子。
- user: 前端转 AI 的开发者, category: 注意, comment: 这份参考只覆盖 Python SDK, 我以为照着就能写 TypeScript 版, 写到一半才发现其他语言还是 coming soon。团队用 Node 的先确认这点。
- user: 独立开发者, category: 坑, comment: samples.md 只给菜名不给菜。我停在名字上就开写, 审批门禁写得漏洞百出; 后来克隆对应 recipe 读代码才看到差距, 目录只是索引。
- user: 运维老哥, category: 注意, comment: 机器上没装 agents-cli 什么都跑不了。先 `uv tool install google-agents-cli`, 再用 `agents-cli info` 确认项目, 然后才轮到写代码。
- user: 带两个 AI 项目的组长, category: 启发, comment: 用完我定了条组规: 写沙箱、审批、记忆这类模块前, 必须先翻 samples.md 查有没有现成 recipe。我们重复造的轮子实在太多了。
