# respond-to-pr-comments-in-blocklist (`warpdotdev/common-skills/respond-to-pr-comments-in-blocklist`)

## whitebox

- 复用上下文中已有的 PR 评论; 缺失时先拉取并展示, 再过滤掉自动化/bot 评论和当前用户已回复过的评论
- 用 ask_user_question 确定响应模式: 逐条处理 (边定边改) 或批量收集决定后统一修改
- 逐条走查评论 (作者 / path:line 位置 / 摘要), 收集处理决定: 推荐修复 / 先解释再定 / 仅确认不改 / 自定义, 并为每条维护决策记录
- 按决定修改代码, 审查 git diff 并跑最小验证 (lint/类型检查/测试), 然后询问是否 commit + push 到 origin
- 展示逐条回复与 resolve 预览, 用户批准后才发布: REST API 发 [Warp Agent] 前缀回复, GraphQL 关闭已批准线程

- 双通道写 GitHub: 评论回复走 gh REST API (回复体先写临时文件 → python3 包成 JSON → --input 传入, 规避命令行转义问题); resolve 线程走 GraphQL (分页查询 reviewThreads, 把 comment ID 映射到 thread ID 后调 resolveReviewThread)。外部依赖: GitHub CLI (gh)、python3、git
- 出站门禁: 任何回复/resolve 必须先经用户批准的预览, 不可跳过; 发布前校验 body 以 `[Warp Agent]` 开头, 否则补上; commit 先于回复发布 (保证 reviewer 先看到代码), 提交信息含 Co-Authored-By: Warp Agent
- 评论过滤与决策记录: 用 `gh api user` 识别当前用户, 结合线程 resolution 状态和最新回复作者, 跳过自动化评论/已答评论 (仅内部记 skipped 清单, 不进走查); 每条评论保留决策记录: 处置方式、代码改动、验证情况、draft reply、是否 resolve
