# implement-spec (`mattpocock/skills/implement-spec`)

## whitebox

- 读 spec 和 tickets, 理解任务图 (task graph) 及其阻塞关系
- (可选) 派探索子代理调研代码库/文档, 笔记存到仓库外的共享目录
- 建分支 + 草稿 PR, 标记为 closing 对应的 spec issue 和 tickets
- 循环推进 frontier: 派实现子代理在各自独立 worktree + 分支上实现就绪的 ticket, 完成后由合并子代理合入 PR 分支, 阻塞解除则立即派发下一批
- 全部 ticket 完成后跑 /code-review, 由单个实现子代理一次性修复所有问题, PR 标记为 ready for review, 清理所有 worktree

- 任务图调度: tickets 是带阻塞关系的图而非步骤清单, 任意时刻都存在一个 frontier (当前无阻塞、可开工的 ticket 集合); 实现子代理后台运行以最大化并发, 每次合并后重算 frontier 并补派新任务
- 稀疏通信: 子代理之间不传大段内容, 只交换上下文指针 (指向 spec、tickets、研究笔记、已有 commit); 探索产物统一存放在仓库外的共享目录, 供后续所有实现子代理直接引用
- 隔离与合流: 每个实现子代理在独立 git worktree + 独立分支上工作, 互不干扰; 完成后由 merger 子代理统一合入 PR 分支; 依赖的外部工具为 git (branch/worktree/merge)、GitHub PR、以及 /code-review 技能
