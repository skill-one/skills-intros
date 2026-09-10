# write-tech-spec (`warpdotdev/common-skills/write-tech-spec`)

## whitebox

- 确认资格并定 id: 只接跨模块、有架构取舍的功能(纯 UI/简单修复跳过);确定规格目录 id(Linear 工单号 / `gh-` 前缀 issue / 短横线功能名),缺 id 就向用户要
- 写前调研: 读产品规格(如有), 直接翻代码而非猜测, 摸清主要文件、类型、数据流与所有权边界
- 起草 TECH.md: 按 Context / Proposed changes / Testing and validation / Parallelization 骨架写, 设计贴合现有代码模式, 关键代码引用钉住 commit SHA
- 落盘到 specs/<id>/TECH.md: 按长度启发式控制篇幅(跨模块改动约 80–150 行), 空节整节省略
- 保持同步: 实现中若模块边界、风险或验证策略变了, 在同一 PR 里更新 TECH.md, 让文档描述真正上线的那版实现

- 代码钉引用机制: 用 `git rev-parse HEAD` 抓取每个调研仓库的当前 commit SHA, 把代码引用转成 GitHub `blob/<sha>/...#Lx-Ly` 链接, 读者能回看调研时看到的原始代码。外部依赖: git
- 行为→验证映射机制: 不复述产品行为, 直接引用 PRODUCT.md 的编号 Behavior 不变量, 每条不变量映射到具体测试/验证步骤——验证责任全部归 TECH.md。外部依赖: GitHub 远端(用于生成代码链接)
- 并行执行评估机制: 若 `run_agents` 可用则评估子代理并行(每个 agent 定角色、执行模式 local/remote、worktree/分支/PR 策略、协调边界, 依赖复杂时配 Mermaid 图); 不可用则整节省略, 决定不并行时写一句理由。外部依赖: `run_agents` 子代理、Linear MCP / `gh` CLI(仅当用户明确要求建单/建 issue 时用)
