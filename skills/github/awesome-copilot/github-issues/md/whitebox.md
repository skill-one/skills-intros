# github-issues (`github/awesome-copilot/github-issues`)

## whitebox

- 判定动作: 创建 / 更新 / 查询 issue
- 收集上下文: 确认仓库, 按需读取现有 labels、milestones
- 结构化内容: 按用户意图匹配 references/templates.md 中的模板 (Bug Report / Feature Request / Task) 组织标题与正文
- 执行: 读操作走 MCP 工具, 写操作走 gh api
- 确认: 向用户回报 issue URL

- 双通道工具路由: 读取走 @modelcontextprotocol/server-github MCP 工具 (issue_read / list_issues / search_issues / projects_*), 写入走 gh api (GitHub REST); MCP 未连接或需 REST 专有字段 (如 issue type, gh issue create CLI 不支持 --type) 时回落到 gh api
- 模板驱动的内容生成: 依据请求措辞选 Bug / Feature / Task 模板; 标题 <72 字符且设 type 后不加冗余前缀 ([Bug] 之类); 分类优先用 issue type 而非等价 label, 可用 GraphQL 查询 org 已配置的类型
- 写入侧防错: labels[]/assignees[] 等参数须整体加引号, 否则 zsh 会把 [] 当 glob 报 'no matches found'; 更新前先读当前 issue, PATCH 只传变更字段以免覆盖已有内容
