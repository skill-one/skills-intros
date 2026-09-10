# implement-specs (`warpdotdev/common-skills/implement-specs`)

## comments

- user: 后端老兵, category: 妙用, comment: 以前代码写完才补文档, reviewer 审的全是过时设计。现在设计一变就同步改 TECH.md, 和代码推同一个 PR, 评审全程锚定真正要上线的功能。
- user: 第一次用的新手, category: 坑, comment: 没确认 spec 过审就开工, 做到一半产品方向变了, 白干。前提是 PRODUCT.md 存在、TECH.md 按需、且已获批, 先检查这三样再动手。
- user: 全栈独立开发, category: 注意, comment: 小功能别硬凑 TECH.md, 该有才写。我小改动只放 PRODUCT.md 就能跑, spec 按 specs/工单号/ 目录存放, 别为流程而流程。
- user: AI 协作重度用户, category: 妙用, comment: 大功能做了几天, 中断后重新探索一遍路径浪费半天。现在开工先开 PROJECT_LOG.md 记检查点和已试路径, 续上读一遍就能接着干。
- user: 互联网小团队 TL, category: 注意, comment: 发现行为要变时我只改代码, spec 更新攒到最后统一补, 结果 PR 里两者对不上。正确做法: 发现偏差立刻同步改 spec, 和代码一起提交, 别攒。
- user: 测试工程师, category: 启发, comment: 以前"能跑"就算完。这技能要求最后对照当前 spec 验证: 按仓库测试约定补单测, 关键流程加集成测试, 不然 spec 和代码悄悄脱节根本发现不了。
