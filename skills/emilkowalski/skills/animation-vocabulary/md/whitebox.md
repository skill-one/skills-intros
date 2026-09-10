# animation-vocabulary (`emilkowalski/skills/animation-vocabulary`)

## whitebox

- 接收用户的模糊动效描述 (如 "弹一下才停"、"从按钮里长出来"), 读意图而非关键词
- 把感受映射到 SKILL.md 内嵌的动画术语表, 定位匹配术语
- 逐字引用术语表条目, 以固定格式输出: **术语 — 一句定义**
- 若多个术语近似, 最佳匹配放首位, 附 1~2 个备选并一句话点出区别
- 若无精确匹配, 给出最接近术语并明说是近似, 或用词表词汇描述效果; 真不在表里就直说, 不造词

- 单一权威数据源: 匹配完全依赖 skill.md 内嵌的策展术语表 (镜像项目 /vocabulary 页, 双方改动需同步), 输出时逐字引用原文、不改写——无任何外部工具、库或模型 API 依赖, 纯提示词驱动
- 歧义消解规则: 对易混术语对 (Clip-path vs Mask、Pop in vs Bounce、Shared element transition vs Layout animation) 主动对比说明差异; 边界情况允许用词表内词汇组合描述 (如 "stagger 的 scale-in 入场")
- 输出纪律: 命名问题给名字不给论文——术语前置, 默认不展开, 用户追问才扩展; 效果命名, 不涉及设计或实现动效
