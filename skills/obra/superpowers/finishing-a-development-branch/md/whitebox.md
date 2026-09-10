# finishing-a-development-branch (`obra/superpowers/finishing-a-development-branch`)

## whitebox

- 跑项目完整测试套件 (npm test / cargo test / pytest / go test), 失败立即停止上报, 绿了才往下走
- 用 git rev-parse 对比 --git-dir 与 --git-common-dir 判定环境 (普通仓库 / worktree / detached HEAD), 顺带记录 WORKTREE_PATH 供后续清理用
- 确定分支的 base branch (来源通常是计划、对话或上游); 拿不准就先向用户确认, 确认前不合并
- 按环境呈现固定选项菜单 (正常路径 3 项: 本地合并 / 推送建 PR / 原样保留; detached HEAD 减为 2 项), 停下来等用户选
- 执行所选: 合并结果必须复测通过, 才清理 worktree 并删分支; 推送建 PR 则保留 worktree; '原样保留' 只报告分支与 worktree 位置

- 环境判定与清理归属: git-dir 与 git-common-dir 相等即普通仓库, 不等即 worktree; 只有 .worktrees/ 或 worktrees/ 下的自建 worktree 才执行 git worktree remove + prune, 其余归宿主环境所有、一律不动
- 多层安全闸: 测试绿才出菜单; 合并结果复测失败则冻结现场调查; 集成决策永远交给用户; 删除只接受用户原字输入 'discard'; --force / force-push 一律不主动使用; worktree 删除被拒时用 git status --porcelain -uall 列出未提交文件, 让用户三选一
- 外部依赖: git CLI; 项目自带测试运行器 (npm/cargo/pytest/go test); forge 的 CLI 或 push 时打印的 PR 创建链接 (用于建 PR)
