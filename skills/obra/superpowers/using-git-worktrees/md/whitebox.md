# using-git-worktrees (`obra/superpowers/using-git-worktrees`)

## whitebox

- Step 0: 用 git 内部命令检测当前是否已在隔离工作区 (比对 git-dir 与 git-common-dir, 并排除子模块误判); 已隔离则跳过创建
- 若在普通仓库, 先向用户确认是否创建 worktree (用户拒绝则原地工作)
- Step 1: 优先用平台原生 worktree 工具创建; 无原生工具才用 git worktree add 手动兜底 (创建前先确认目录已被 .gitignore 忽略)
- Step 2: 按项目标志文件 (package.json / Cargo.toml / requirements.txt / go.mod 等) 自动探测技术栈并安装依赖
- Step 3: 运行基线测试, 全部通过即报告 "工作区就绪, 可以开工"

- 隔离检测机制: 依赖 git 命令行 (rev-parse --git-dir / --git-common-dir / --show-superproject-working-tree) 判断环境, 两个路径相等即普通仓库; 内置子模块护栏防止误判
- 工具优先级 + 安全校验: 原生 harness 工具 (如 EnterWorktree 类) > git worktree 兜底 > 原地工作; 项目本地 worktree 目录创建前必须通过 git check-ignore 校验, 未忽略则先写入 .gitignore 并提交, 防止工作树内容被误提交进仓库
- 环境自动适配: 靠标志文件探测技术栈, 调用对应包管理器 (npm / cargo / pip / poetry / go mod) 装依赖, 再用项目惯用命令跑测试; 无标志文件则跳过安装
