# directory-submissions (`coreyhaines31/marketingskills/directory-submissions`)

## whitebox

- 先读上下文: 若存在 .agents/product-marketing.md (或 .claude/ 版、旧版文件名) 直接读取, 只追问缺口信息
- 就绪评估: 问 9 个问题; 1–7 任何一问为否即硬阻塞, 先补齐缺失件 (定价页/条款/素材/GEO 落地页) 再提交
- 选层: 按产品类型从 references/directory-list.md 的 13 个层级中筛出真正匹配的目录, 不合身的不投
- 生成分层文案: 从 references/positioning-variations.md 提取变体, 按层级改写 tagline / 短描述 / 长描述 / 标签
- 批量提交: 用 references/submission-tracker-template.csv 建追踪表, 逐条提交并登记日期/URL/状态, 上线后验证外链

- 文件驱动, 无模型依赖: 全部数据来自随附的 3 个参考文件 — directory-list.md (13 层目录清单)、positioning-variations.md (定位文案库)、submission-tracker-template.csv (追踪表); 唯一外部工具是 curl, 用于 `curl -sIL <listing> | grep -i rel=` 验证外链是否 dofollow
- 双重前置门禁: Rule 1 落地页就绪清单 (单一 H1、定价页、隐私/条款、PNG/SVG/方形 logo、5–8 张截图 + 60–90s 视频、FAQ schema、Organization/Product 结构化数据) + Rule 2 目的地页面先行 (3–5 个 alternatives 页、use-case 页必须在提交前上线) — 缺件只建不投
- 定位变换: 同一产品不复制粘贴同一描述, 按目录受众切换叙事 (创业目录讲结果 / SaaS 目录讲 "某某替代品" / AI 目录讲 AI-first / 评审站讲 ROI + 案例), 避免 AI 引擎对重复内容交叉降权
