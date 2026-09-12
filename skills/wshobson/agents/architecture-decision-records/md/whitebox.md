# architecture-decision-records (`wshobson/agents/architecture-decision-records`)

## whitebox

- 先对照"该写/不该写"清单过滤任务：新框架选型、数据库选型等写 ADR，Bug 修复、小版本升级直接不写
- 按决策重量从 5 套内置模板中选一个：标准 MADR / 轻量版 / Y-Statement / 废弃迁移版 / RFC 征求意见版
- 填充三要素：Context（为什么必须决策）→ Decision（定了什么、备选方案优缺点）→ Consequences（正面/负面/风险后果），诚实列出真实缺点
- 设置生命周期状态（Proposed→Accepted→Deprecated/Superseded/Rejected），链接相关 ADR；改决策时不改旧文档，而是新写一篇并标注 Supersede
- 归档到 docs/adr/NNNN-title-with-dashes.md，更新 README.md 索引表，提交评审走 checklist

- 模板驱动生成：输出结构完全来自内置 5 套模板，按决策重要性匹配格式轻重（重大决策用完整 MADR，小决策用 3 行 Y-Statement），且强制控制在 1-2 页内
- 状态机约束：Status 只能在 Proposed/Accepted/Deprecated/Superseded/Rejected 中取值；核心规则是"已接受的 ADR 不可修改"，只能被新 ADR 取代，保证决策历史不可篡改
- 外部工具依赖：仅 adr-tools CLI（brew install adr-tools），负责目录初始化、新建议录、supersede 链接、相关 ADR 互链和 generate toc 生成索引表；不依赖任何模型 API 或第三方库
