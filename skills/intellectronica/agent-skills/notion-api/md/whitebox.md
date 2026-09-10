# notion-api (`intellectronica/agent-skills/notion-api`)

## whitebox

- 鉴权: 检查环境变量 NOTION_API_TOKEN, 缺失则向用户索要, 并调 /v1/users/me 验证密钥可用
- 构造请求: 按目标端点 (search/pages/blocks/databases/comments) 拼出 REST 调用, 必带三个头 Authorization、Notion-Version: 2025-09-03、Content-Type: application/json
- 写入操作前先向用户确认一次 (同组相关操作只需一次确认)
- 用 curl 发送请求, 响应管道给 jq 解析, 读取需要的字段
- 分页收尾: 若 has_more 为 true 则携带 next_cursor 继续请求, 直到取完所有结果

- 纯 REST + JSON: 全部操作通过 curl 直连 https://api.notion.com, 无 SDK/模型依赖; 资源定位靠 UUIDv4 ID (页面 ID、块 ID、数据库 ID), 令牌只出现在 Authorization 头, 绝不回显或落日志
- 校验双层: 发送前遵守硬性限制 (每次最多 100 个 block、payload ≤ 500KB、rich_text ≤ 2000 字符等); 发送后按 HTTP 状态码表判错——401/403/404 常见为令牌无效或页面未授权给集成, 429 读 Retry-After 头做指数退避重试
- 分页游标机制: 列表类端点统一返回 has_more/next_cursor, 用 start_cursor 循环迭代, 适配大数据量场景
