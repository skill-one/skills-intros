# writing-plans (`obra/superpowers/writing-plans`)

## whitebox

- 读 spec 做范围检查：若覆盖多个独立子系统，建议拆成多份计划，每份独立可交付、可测试
- 先画文件结构：列出每个要新建/修改的文件精确路径 + 单一职责，以此锁定任务切分方式
- 按固定模板写计划文档：每个任务拆成 2-5 分钟的单步 checkbox（写失败测试→跑→最小实现→跑→提交），步骤里嵌真实代码和命令
- 保存到 docs/superpowers/plans/YYYY-MM-DD-<feature>.md，然后自查三遍：spec 覆盖率、占位符扫描、跨任务类型/签名一致性，发现问题就地改
- 交接：让用户二选一 —— subagent-driven（每任务派新子代理+两阶段审查）或 inline（executing-plans 批量执行带检查点）

- 任务自包含契约：每个任务带 Files（精确路径/行号）+ Interfaces（consumes/produces 精确签名），因为执行者默认只看得到自己那一个任务，名字和类型全靠这个块传递
- No Placeholders 禁令：任何一步出现 'TBD'、'类似任务N'、'适当处理错误' 而无真实代码，即判定计划失败；工程师可能跳序阅读，代码必须重复展开
- 无外部库/模型 API，纯文档工程；仅依赖同族 superpowers 技能做交接：using-git-worktrees（执行时建隔离 worktree）、subagent-driven-development 或 executing-plans（按用户选择二选一）
