# google-agents-cli-eval (`google/agents-cli/google-agents-cli-eval`)

## comments

- user: 第一次给 agent 做评测的新手, category: 坑, comment: 多轮 case 配了 final_response_quality 直接 400。只有 multi_turn_ 开头的三个指标吃多轮轨迹, 其余内置指标只认单轮, 跑前先对齐。
- user: ADK 项目开发者, category: 坑, comment: App(name=...) 和 agent 目录名不一致, eval generate 起服务就报 Session not found。name 必须和目录名一致, 我折腾了半小时才查到。
- user: 做 RAG 客服 agent 的, category: 妙用, comment: 别只盯分数, 打开 results.html 读 judge 的评分理由, 每个 fail 都写着差在哪条标准。照着理由改 prompt, 三轮就过线, 比瞎试快得多。
- user: 测试工程师转做 agent, category: 启发, comment: 留一批 case 不进迭代这点戳中我: 以前对着同一批改到全绿就上线, 新 case 一来全崩, 纯属过拟合。现在固定留 20% 当盲测集再收工。
- user: 管公司 GCP 项目的运维, category: 注意, comment: eval run / grade 默认走 global 区域, 不继承 manifest 里配的 region, 直接 400 FAILED_PRECONDITION。加 --region 指定支持的区域就通了。
- user: 赶 deadline 的独立开发者, category: 注意, comment: eval optimize 又慢又贵, 我上来就跑, 烧了半小时模型调用。其实先手动改 prompt、工具描述迭代, 实在改不动了最后跑一次收尾就够。
