# planning-with-files-zh (`othmanadi/planning-with-files/planning-with-files-zh`)

## whitebox

- UserPromptSubmit 钩子触发：按 PWF_SCRIPT_DIR→CLAUDE_SKILL_DIR→用户级安装路径顺序解析出第一个存在的 skill-hook.sh 并执行 --event=userprompt，注入规划上下文（只有这个钩子会在脚本缺失时报错）。
- 恢复状态：用 resolve-plan-dir.sh 结合 PLAN_ID 和 PWF_PLAN_ROOT 选定计划目录，读取 task_plan.md / findings.md / progress.md，并跑 git diff --stat 检查未记录的代码变更。
- 初始化或复用计划：独立任务跑 scripts/init-session.sh "任务名" 生成 PLAN_ID 并固定到主机，用模板在选定任务目录中只补建缺失的三个规划文件。
- 执行中：PreToolUse 钩子在每次 Write/Edit/Bash/Read/Glob/Grep 调用前重新读取并注入 task_plan.md；遵循两步操作规则（每两次查看/搜索后立即把发现写入 findings.md），阶段完成更新 task_plan.md，全程写 progress.md。
- 收尾与压缩：PostToolUse（Write|Edit）同步状态，上下文压缩前 PreCompact 注入选定计划，Stop 钩子收尾（不带计划正文）。

- 生命周期钩子注入：5 个钩子共享一个模板调用同一个 skill-hook.sh；不对称设计——只有 UserPromptSubmit 报告脚本未解析（每提示一次），PreToolUse/PreCompact/Stop 静默以避免刷屏。这使 task_plan.md 在每次工具调用前被重复注入上下文。
- 三文件磁盘记忆模型：task_plan.md（阶段/决策）、findings.md（研究/发现）、progress.md（会话日志）存放在项目内选定任务目录（不是技能安装目录）；配套两步操作规则、错误表、三次失败协议防止重复失败。
- 安全与外部依赖：外部内容（网页/搜索结果）只许写 findings.md，绝不写会被钩子反复读取的 task_plan.md（防间接提示注入）；Markdown 中声明的命令绝不执行，且无网络上传路径。依赖 POSIX sh（钩子脚本）、python3/python（session-catchup.py，仅在显式 --metadata/--replay 时读本机同项目会话元数据）、git（diff 检查）。无模型 API 依赖。
