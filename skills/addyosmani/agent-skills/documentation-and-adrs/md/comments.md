# documentation-and-adrs (`addyosmani/agent-skills/documentation-and-adrs`)

## comments

- user: 后端老兵, category: 妙用, comment: 选型别重吵, 先翻 docs/decisions/ 里的旧 ADR, 三年前 rejected 的理由直接终结争论; 决策变了别删旧的, 写新的标 Superseded.
- user: 第一次用的新手, category: 坑, comment: 我给每行都写注释被打回: 只写代码看不出的 why, 比如限流为何在窗口边界重置. 注释掉的旧代码也删掉, git 有历史.
- user: 接手老项目的工程师, category: 注意, comment: 进仓库先找现有 ADR 约定再动笔. 我自建了 docs/adr/001.md, 结果项目用 rst 格式且已编到 014, 只能返工重编号.
- user: 带 AI 写码的独立开发者, category: 妙用, comment: 把选型写成 ADR 后, AI 助手不再反复建议换库——rejected 理由都在里面; 踩过的坑写成 IMPORTANT 注释, 它直接绕开.
- user: 开源维护者, category: 妙用, comment: changelog 按 Added/Fixed/Changed 三段写, 发版说明十分钟拼完; 发版前照技能里的验证清单逐项过, 能拦下死代码和陈年 TODO.
- user: 刚带小组的组长, category: 启发, comment: 以前想等 API 稳了再补文档, 写 ADR 才发现过程就是设计检验——列备选方案时才看出 SQLite 并发写不行. 现在吵超十分钟就先写 ADR.
