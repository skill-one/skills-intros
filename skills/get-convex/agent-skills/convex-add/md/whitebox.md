# convex-add (`get-convex/agent-skills/convex-add`)

## whitebox

- 解析请求, 确定用户想添加的能力名称
- 拉取在线能力目录 capabilities.json (4秒超时), 将请求与条目的 title/summary/trigger 匹配
- 命中后拉取 /capability/<id>.md 文档
- 按文档中的 Procedure+Rules 步骤执行, 将能力接入当前 Convex 应用
- 向用户确认完成, 附结果 URL (托管) 或组件名

- 在线目录优先: 服务端托管的目录/文档是唯一事实来源, 永远最新, 优先级高于内置知识; 且文档内容是流程指令而非可直接执行的命令, 需运用正常判断
- 双路兜底: 目录不可达或未命中时不硬失败 — 'hosting' 走内置 /add-hosting, 其余跑 /add-component 搜索脚本, 从实时返回的 CANDIDATES 列表安装最佳匹配 (绝不硬编码组件映射)
- 外部依赖: 需网络 (curl/bash) 访问 https://basic-anteater-667.convex.site; 若沙箱拦截, 提示用户放开网络后重试
