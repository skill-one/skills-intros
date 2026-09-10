# spec-driven-implementation (`warpdotdev/common-skills/spec-driven-implementation`)

## whitebox

- 先判断是否值得写 spec: 评估规模、模糊度、风险, 小改动直接跳过走验证
- 无对应 Linear 工单则先用 Linear MCP 工具创建, 再写产品 spec specs/<工单号>/PRODUCT.md
- 实现跨多个子系统或有重要权衡时, 追加写技术 spec specs/<工单号>/TECH.md
- spec 获批后按 implement-specs 流程实现, spec+代码+测试放进同一个 PR
- 实现偏离 spec 就同步更新 spec, 最后用测试/截图等把验证结果对回 spec

- 文件路径约定驱动: spec 固定放在 specs/<linear-ticket-number>/ 下, 工单号即目录名, specs/ 下不允许工程师名或功能名子目录
- 依赖 Linear MCP 工具集成: list_teams 查团队 → list_issue_labels 查标签 → save_issue 建工单; 团队/标签不明时用 ask_user_question 问而不是猜
- 复用三个子技能分工: write-product-spec 产出产品向 spec, write-tech-spec 产出实现向 spec, implement-specs 按批准的 spec 落地; 大型功能可选追加 PROJECT_LOG.md / DECISIONS.md 追踪决策
