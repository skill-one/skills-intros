# setup-matt-pocock-skills (`mattpocock/skills/setup-matt-pocock-skills`)

## whitebox

- 探测仓库现状: 读 git remote、CLAUDE.md/AGENTS.md、docs/agents/、.scratch/、monorepo 信号、triage skill 是否已装, 不做任何假设
- 按节顺序提问: A) issue tracker (按 remote 推荐 GitHub/GitLab/本地 markdown/其他), B) triage 标签 (仅当 triage skill 已装, 默认直接采用), C) domain docs (默认单上下文, 不问)
- 展示写入草稿: `## Agent skills` 块 + docs/agents/ 各配置文件内容, 交用户编辑确认
- 写入: 编辑已有的 CLAUDE.md (否则 AGENTS.md, 两者都无则问用户), 并用 skill 自带种子模板生成 docs/agents/issue-tracker.md、domain.md 等文件
- 收尾: 告知用户哪些工程 skill 现在会读取这些配置文件

- 探测驱动分支: 全部行为由仓库实测状态决定 — git remote 指向决定 issue tracker 类型与模板 (GitHub→gh CLI, GitLab→glab CLI); monorepo 信号决定单/多上下文; triage skill 未装则整节跳过, 不生成 triage-labels.md
- prompt-driven 非脚本: 逐节提问, 每节先给推荐答案供一词确认, 写入前强制展示草稿让用户编辑; 探测已解决的问题直接跳过该节
- 写入保护规则: CLAUDE.md 与 AGENTS.md 只编辑已存在的那个, 两者都无才询问创建哪个; 已有 `## Agent skills` 块则原地更新, 不覆盖用户对周边章节的修改; PRs-as-request-surface 标志默认关闭且不主动提及
