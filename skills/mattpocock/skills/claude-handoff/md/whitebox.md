# claude-handoff (`mattpocock/skills/claude-handoff`)

## whitebox

- 接收触发 (仅用户手动触发, frontmatter 声明 disable-model-invocation: true, 模型不会自动调用), 若用户带参数, 则把参数视为"下一会话的用途说明", 据此裁剪摘要重点
- 把当前对话浓缩成一份交接摘要: 只引用既有产物 (specs/commits/issues 等) 的路径或 URL, 不复述其内容; 摘要中写明下一任应调用哪些 skill (suggested skills 段落)
- 脱敏: 清除摘要中的 API key、密码、个人敏感信息——因为摘要会原样变成新 agent 的 prompt
- 执行 `claude --bg --name "<描述性名称>" "<交接摘要>"` 启动后台 agent: 摘要即它的初始 prompt, 它在当前工作目录启动并立即返回
- 结束: agent 已在后台跑, 用户通过 `claude agents` 查看和管理它

- 依赖外部工具: claude CLI 本身——用 `--bg` 旗标把 agent 放到后台运行, 用 `-n/--name` 设置显示名 (出现在任务列表、会话选择器、终端标题中); 不涉及额外库或模型 API, 交接摘要直接作为新 agent 的 seed prompt
- 信息不重复原则: 摘要不复制已在其他产物 (计划、ADR、commit diff) 里的内容, 一律按路径/URL 引用, 保证摘要短且不产生第二份真相
- 安全机制: 因摘要会持久化为新 agent 的输入, 敏感信息 (密钥/密码/PII) 必须在写入前脱敏
