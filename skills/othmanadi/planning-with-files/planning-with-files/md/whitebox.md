# planning-with-files (`othmanadi/planning-with-files/planning-with-files`)

## whitebox

- 用户提交 prompt → UserPromptSubmit hook 调 scripts/skill-hook.sh --event=userprompt, 注入纯文本上下文
- 模型按 resolve-plan-dir.sh 顺序定位唯一计划目录 ($PLAN_ID 严格绑定 → .planning/.active_plan → 最新 .planning/<dir>/ → 根目录 legacy task_plan.md), 读取 task_plan.md / findings.md / progress.md 恢复状态
- 每次工具调用前, PreToolUse hook (匹配 Write|Edit|Bash|Read|Glob|Grep) 注入该事件的 additionalContext JSON
- 模型执行任务: 每 2 次查看/搜索后立即把发现写入 findings.md (2-action rule); 每完成一个阶段, 更新 task_plan.md 阶段状态 + 刷新 Next Step + 追加 progress.md
- 每次 Write/Edit 后 PostToolUse hook 注入提醒 (进度提醒每轮至多一次); Stop / PreCompact 时输出诊断信息与已记录的 Plan-SHA256

- 生命周期钩子注入: 5 个宿主事件 (UserPromptSubmit/PreToolUse/PostToolUse/Stop/PreCompact) 各注册一条 POSIX sh 命令, 统一调 scripts/skill-hook.sh --event=<event>; 脚本读宿主 JSON 会话身份决定注入纯文本还是 additionalContext; 检测到 CLAUDE_PLUGIN_ROOT 时直接退出 0 (plugin 安装走独立路由, 额外带 SessionStart 启动恢复). 依赖: POSIX shell, 无其他运行时
- 计划解析与防串扰: PLAN_ID 是硬绑定 — 解析失败即停止注入, 绝不 fallback 到其他计划; 存在多个具名计划且无 PLAN_ID → 拒绝选择; PWF_PLAN_ROOT 钉绝对根路径; 歧义场景 (当前 cwd 有 active plan 且紧邻嵌套项目自带 plan) → 不注入任何内容并提示 pin. 附加校验: attest-plan.sh 用 SHA-256 锁定 task_plan.md 内容, 文件偏离哈希时 hook 拒绝注入计划内容
- 磁盘记忆 + 显式会话回放: 核心模式为 '上下文窗口=RAM, 文件系统=磁盘', 由宿主模型用标准 Read/Write/Edit 维护三个 markdown 文件, 全靠 SKILL.md 中的行为规则驱动 (2-action rule / 错误日志表 / 3-strike 协议). 外部依赖仅 Python 标准库 + SQLite: session-catchup.py 只在用户显式要求时读 OpenCode 的本地只读库 (--metadata 仅出聚合计数, --replay 出有界 nonce 框定摘录); 无网络上传路径, 不依赖任何模型 API
