# convex-migrate-rehearse (`get-convex/agent-skills/convex-migrate-rehearse`)

## whitebox

- 前置检查: 确认有 Preview Deploy Key (付费功能, 设为 CONVEX_DEPLOY_KEY), 并向用户明确 prod 既是数据源也是改动目标, 拿到对 prod 上线的预先确认
- 只读导出 prod 快照 (npx convex export), 再用改前代码创建预览部署并把快照导入作种子 —— 保证导入的数据仍符合旧 schema
- 在预览副本上按 migrate 顺序演练: 新字段先设 optional → 推送 → 跑 @convex-dev/migrations 回填 → 验证 → 收紧校验器再推送, 让 schema 一致性门槛在副本上暴露问题而非 prod
- 在预览上用应用函数/查询验证迁移后数据的行为与形状
- 拿到新的明确'是'后, 把同一序列原样重放到 prod (可选 → 回填 → 收紧), 快照留作回滚产物并提醒: 恢复快照会丢失其后写入的数据

- 数据一致性门槛利用: Convex schema push 会校验每条既有文档, 任何一行不合规即拒绝整个推送 —— 本技能先用改前代码建预览并导入 prod 快照, 让这个门槛在副本上失败/通过, prod 上的推送因此只是'重放已验证的运行'
- optional-then-tighten 顺序: 首次推送若字段是必填会被存量行拒绝, 所以必须先可选 → 回填 → 再收紧 (required / 收窄 union); 顺序不可跳过
- 外部依赖: npx convex CLI (export / import --deployment / deploy --preview-create·--preview-name), @convex-dev/migrations 库 (分批、可续跑、可 dry-run 的回填), Preview Deploy Key (CONVEX_DEPLOY_KEY, 无预览密钥时降级到个人 dev 环境), MCP 的 run / runOneoffQuery 用于预览验证
