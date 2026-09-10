# skill-creator (`anthropics/skills/skill-creator`)

## whitebox

- 捕获意图：优先从当前对话提取要固化为技能的工作流（用过哪些工具、步骤顺序、用户做过的纠正），信息缺口再向用户追问（目的/触发时机/输出格式/要不要测试）
- 写 SKILL.md：YAML frontmatter（name + 措辞偏"激进"的 description，用于触发）+ Markdown 正文（<500 行），按需捆绑 scripts/references/assets
- 双轨测试：每个测试用例同一轮并行派两个 subagent——带技能 vs 基线（无技能，或 cp -r 快照的旧版技能）——结果存 <skill>-workspace/iteration-N/，趁运行间隙起草断言
- 评分与出报告：按 agents/grader.md 核对断言（能量化就跑脚本），aggregate_benchmark.py 汇总 pass_rate/耗时/tokens 生成 benchmark.json，再启动 generate_review.py 查看器，让用户逐条看产出并留反馈
- 迭代：用户提交后读 feedback.json → 改技能（泛化问题、解释 why、抽取重复出现的辅助脚本进 scripts/）→ 重跑下一轮，循环到满意

- 渐进式三层加载：metadata（name+description，约 100 词）常驻上下文兼做触发开关；SKILL.md 正文触发后才载入；捆绑资源（脚本可执行不占上下文）按需加载。description 特意写得更"外向"、枚举触发短语，对抗技能该触发却不触发的倾向
- 成对对照校验：每个用例必须同轮跑 with_skill + 基线两组；断言只收客观可验证项（文风类主观产出留给人工评）；grading.json 字段固定为 text/passed/evidence；汇总时加一轮分析师检查，揪出误导性统计（如永真断言、高方差用例）。timing.json 必须在 subagent 完成通知到达时立即落盘，否则丢失
- 外部依赖：运行载体就是 Claude 本体（技能本身是纯 Markdown 指令，无自有执行逻辑，唯一可执行部分是捆绑的 Python 脚本）——eval-viewer/generate_review.py（浏览器查看器，无显示环境用 --static 生成独立 HTML）、scripts/aggregate_benchmark.py（基准聚合）；调研可借力 MCP；测试用例统一定义在 evals/evals.json
