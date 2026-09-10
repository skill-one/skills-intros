# marketing-plan (`coreyhaines31/marketingskills/marketing-plan`)

## whitebox

- 触发 `/marketing-plan {client}` 后, 读取 `~/marketing-plans/{client-slug}/progress.md`, 按状态机 (fresh → INIT → REVIEW → FINALIZE) 决定从哪一步继续
- INIT 阶段: 读客户现有材料 + 从已接线的工具 (Ahrefs, GA4 MCP, Stripe MCP) 拉数据, 做结构化访谈, 用内嵌 17 节现状评分表打分, 结果存入 research.md
- REVIEW 阶段: 按 AARRR 结构逐节 (共 13 节) 在对话中展示草稿, 用户逐节批准/修改, 每节确认后写入进度文件 (可断点续跑)
- FINALIZE 阶段: 汇编 13 节为 final_plan.md, 做校验 (idea 编号等交叉引用是否准确、无机器本地路径、品牌语气一致), 可选发布到 GitHub 仓库供团队共享

- 状态机 + 落盘文件驱动: 中间产物全部存文件 (research.md / 进度文件 / final_plan.md), 中断后重跑同一命令可从下一未完成节续起; 已定稿 (finalized) 的计划不会被静默覆盖, 会先询问修订、重写还是重开某一节
- 固定 13 节模板 + AARRR 标签体系: 输出结构固定为 13 节, 每条建议必须标注所服务的漏斗阶段 (Acquisition/Activation/Retention/Referral/Revenue); 模板、评分表、预算公式等细节由 references/ 目录下的参考文件提供 (methodology.md, plan-template.md, current-state-rubric.md 等)
- 外部依赖: INIT 阶段的数据获取依赖已接线的 MCP/API 工具 (Ahrefs, GA4 MCP, Stripe MCP 等); 最终交付物是可直接粘贴进 Notion 的单个 markdown 文件, 校验环节会交叉核对 marketing-ideas 的 139 条 idea 编号与相关 skill 引用
