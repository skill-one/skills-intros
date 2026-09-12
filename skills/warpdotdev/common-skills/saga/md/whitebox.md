# saga (`warpdotdev/common-skills/saga`)

## whitebox

- 触发: 用户要求端到端自主实现一个中大型功能 (或续跑 ~/.sagas 下的已有 saga), 我以 orchestrator (编排者) 身份接管全流程。
- Phase 1 规划: 用 ask_user_question 带选项追问直到需求零歧义, 把需求写成 spec 树 (SAGA.md + milestones/tasks + PROGRESS.md) 落盘到 ~/.sagas/<name>/, 并定出 saga 级退出标准, 用户批准后才进入下一阶段。
- Phase 2 执行: 逐里程碑用 run_agents 批量派发 worker 子代理, worker 在独立分支上实现并按任务 spec 里的验证标准自检循环 (修→验直到通过), 我合并各分支跑里程碑级验证; 途中受阻只优先查 spec, 查不到才升级问用户。
- Phase 3 验收: 我跑完整套 saga 退出标准并汇报证据, 用户手动验收; 有问题则回到 Phase 2 开小循环修复, 用户确认接受才算完成。
- 全程可恢复: 状态全部在 saga 目录和 PROGRESS.md 里, 新 orchestrator 读盘即可续跑, 换会话/上下文压缩不丢。

- 契约驱动, 无留白: 所有歧义在 Phase 1 用 ask_user_question (带具体选项) 消除; 每个任务的验证标准+验证方法 (computer use / 交互式 CLI / 单测+集成测试, 选型依据 references/validation-strategies.md) 在实现前写成显式契约, 写不出硬标准的任务必须拆分或回问用户 — 不给 worker 留自由裁量。
- 上下文保护 + 磁盘状态机: 我不写功能代码, 重活 (读码/调研/实现) 全部派给 run_agents 启动的 worker, 只回收简报 (分支名、commit/patch、验证证据、pass/blocked); 状态落盘于 spec 树和 PROGRESS.md, 需要时重读而非常驻上下文; worker 子代理本身是执行单元, skill.md 未声明其他外部模型 API。
- 隔离与持久交接: 同仓库并行时每个 worker 独占一个 git worktree + 分支 (命名 saga/<saga-name>/mMtT-<slug>), 验证通过后先 commit/push 留下持久交接再删 worktree, 严禁丢弃唯一副本; 里程碑边界把各分支合并到集成分支做整体验证; GUI/web 验证依赖 computer use (浏览器/图形界面自动化) 能力, 本地没有就派远程 worker 并要求回传分支/PR/patch。
