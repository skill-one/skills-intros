# git-commit (`github/awesome-copilot/git-commit`)

## whitebox

- 用 Bash 执行 git diff --staged (有暂存) 或 git diff, 配合 git status --porcelain 查看真实改动
- 若需要重新分组, 用 git add 选择性暂存文件 (严格排除 .env、密钥等敏感文件)
- 基于 diff 内容推断 type (feat/fix/refactor 等 11 类)、scope 和一句祈使语气的描述 (<72 字符)
- 用 git commit -m 提交, 多行消息 (body/footer) 时用 heredoc 传参

- 无第三方库或模型 API 参与, 全程依赖 Bash 工具调用 git 原生命令 (diff/status/add/commit) 完成解析与执行
- 消息模板严格遵循 Conventional Commits 规范 `<type>[scope]: <description>`, 破坏性变更通过 `!` 后缀或 BREAKING CHANGE footer 标注
- 内置安全协议: hook 失败时修复后新建 commit (绝不 amend)、不跳过 --no-verify、不执行 --force/hard reset 等破坏性命令
