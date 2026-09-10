# golang-design-patterns (`samber/cc-skills-golang/golang-design-patterns`)

## whitebox

- 触发: 任务涉及 *.go 文件或用户点名本技能, 加载 SKILL.md
- 分流: 新建 API/包/结构 → Design mode; 审查现有代码 → Review mode
- Design: 先用 AskUserQuestion 问架构偏好 (clean/hexagonal/DDD/flat), 只选满足需求的最小模式, 反对过早抽象
- Review: 用 Read/Grep 扫描 init() 滥用、无界资源、缺失超时、隐式全局状态, 先报告问题再谈重构
- 用 Edit/Write 落地惯用模式 (函数式选项、defer Close、超时等), 最后经 Bash 跑 go / golangci-lint 验证

- 规则驱动的代码生成: 内置约 22 条硬性准则约束产出 — 构造器用函数式选项且校验失败必须返回 error、枚举从 1 起留零值为非法态、panic 只留给 bug、defer Close 紧跟 open、每个外部调用套超时、重试间隙检查 ctx.Err()
- 按需加载与路由: 深入主题 (架构/整洁架构/六边形/DDD/资源管理/大数据处理) 读 references/ 下的文档; 错误包装、DI 组装、context 传播等细分话题显式转交 golang-error-handling、golang-dependency-injection、golang-context 等兄弟技能, 不越界
- 外部工具: 依赖 go 工具链 (requires.bins: go), 经白名单命令执行 — Bash(go:*), Bash(golangci-lint:*), Bash(git:*); 工具面限定 Read/Edit/Write/Glob/Grep/Agent/AskUserQuestion
