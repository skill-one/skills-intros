# planning-and-task-breakdown (`addyosmani/agent-skills/planning-and-task-breakdown`)

## whitebox

- 进入只读规划模式：读 spec 与相关代码、识别依赖和风险，期间不写任何实现代码。
- 画依赖图：梳理组件间『谁依赖谁』，实现顺序自底向上、先地基后功能。
- 纵向切片：按用户功能路径（如注册、登录）切任务，而非按数据库/API/UI 横向分层。
- 写任务清单：每个任务含验收标准、验证命令、依赖关系、涉及文件和规模估计，写入任务列表目标（默认 tasks/todo.md）。
- 排序并设检查点：依赖排序、每 2~3 个任务后插入 checkpoint，交人工评审后才进入实现。

- 纵向切片转换：把『先建完数据库→再建完 API→再建完 UI』的横向分层，转换为每个任务都端到端可交付、可测试的功能路径；切片依据是依赖图的拓扑顺序。
- 规模校验与拆分触发：内置 XS~L 文件数分级表（L=5~8，XL=8+ 必须再拆）；触发条件包括验收标准写不出 3 条以内、任务涉及两个以上独立子系统、标题里出现 'and'。
- 输出路由与写保护：默认写 tasks/plan.md + tasks/todo.md；若项目规则文件（CLAUDE.md/AGENTS.md）或用户指定外部 tracker（GitHub Issues / Jira / Linear / beads），则改为每个任务一个 tracker item 并映射字段结构；写入前先检查旧 plan/todo 是否还有未勾选任务，是则停下来问人，绝不覆盖。
