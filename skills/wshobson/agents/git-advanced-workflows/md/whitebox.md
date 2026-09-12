# git-advanced-workflows (`wshobson/agents/git-advanced-workflows`)

## whitebox

- 接收用户的 Git 任务: 整理提交历史、跨分支取提交、定位引入 bug 的提交、多分支并行开发、或抢救丢失/误删的工作
- 从技能工具箱中匹配对应技术: interactive rebase / cherry-pick / bisect / worktree / reflog
- 主文档不够用时, 读取 references/details.md 获取详细的模式文档和完整示例
- 给出具体 git 命令, 按安全规范执行: 危险操作前先建 backup 分支, 推送改写历史用 --force-with-lease
- 若中途出错, 走恢复路径: git rebase --abort 等命令中止, 或用 reflog 找回提交 (90 天内有效)

- 全部能力基于本地 git CLI 命令实现 (git rebase -i、cherry-pick、bisect run 自动化二分、worktree、reflog), 不依赖任何外部库、框架或模型 API
- 两层文档结构: skill.md 正文提供核心命令速查导航, 复杂场景时按需加载 references/details.md 的详细模式与实例
- 安全网机制内置于每个操作: 操作前 backup 分支 + reflog 兜底 + --force-with-lease 防覆盖他人提交, 每个进行中的操作都有对应的 --abort/--reset 退出命令
