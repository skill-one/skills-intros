# git-guardrails-claude-code (`mattpocock/skills/git-guardrails-claude-code`)

## whitebox

- 询问安装范围: 仅本项目 (.claude/settings.json) 还是全局 (~/.claude/settings.json)
- 把捆绑的 block-dangerous-git.sh 复制到对应 hooks 目录并 chmod +x
- 将 PreToolUse 钩子 (matcher: Bash) 合并写入对应 settings.json, 已有配置则合并不覆盖
- 询问是否增删拦截模式, 按需编辑脚本
- 验证: echo 一条 git push 的 JSON 管道进脚本, 期望退出码 2 且 stderr 输出 BLOCKED

- PreToolUse 钩子: Claude Code 在执行任何 Bash 命令前调用脚本, 命令以 JSON (tool_input.command) 从 stdin 传入
- 模式匹配 + 阻断: 脚本比对危险命令 (git push 全部变体 / reset --hard / clean -f/-fd / branch -D / checkout . / restore .), 命中即以退出码 2 + stderr 消息拦截, Claude 会收到『无权执行』提示
- 外部依赖: 仅 Claude Code 内置 hook 机制 + 一个捆绑 shell 脚本, 无第三方库、无模型 API
