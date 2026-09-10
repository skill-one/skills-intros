# claude-api (`anthropics/skills/claude-api`)

## comments

- user: 后端老兵, category: 坑, comment: 凭记忆写 budget_tokens 开思考，新模型直接报 400。让它先查技能里的 API 漂移对照表，才知该改成 adaptive thinking。
- user: 半路接手项目的全栈, category: 妙用, comment: 接手两年前的老代码，先跑 prompt-audit：不改一行，先给带 file:line 的过时写法报告和建议 diff，看完再决定动不动。
- user: 第一次接 Claude API 的新手, category: 注意, comment: 我项目里全是 openai 的包，它没硬写，先停下来问我要不要切 Claude。需求提前说清，能省一轮来回。
- user: 内网开发的运维老哥, category: 妙用, comment: 内网连不上官方文档仓库，它不死磕重试：按技能内写法直接生成代码，本地编译报错修到跑通，反而更快。
- user: 精打细算的独立开发者, category: 注意, comment: cost-optimize 真调模型前会先找我批准，不会偷偷烧钱。提前备好 Admin key 或 usage 日志，建议能直接按美元报价。
- user: 刚搭 agent 的产品工程师, category: 启发, comment: 它逼我先想清楚谁跑循环、谁管部署：Tool Runner 和 Agent SDK 都要自己部署，想连部署一起省就上 Managed Agents。
