# to-tickets (`mattpocock/skills/to-tickets`)

## whitebox

- 收集上下文: 读对话里已有的计划/规格; 若参数给了 spec 路径或 issue 编号/URL, 拉取其正文与评论。
- (可选) 探查代码库: 让票的措辞对齐项目领域词汇与 ADR, 并寻找可先行的预重构 (prefactor) 机会。
- 起草垂直切片: 拆成 tracer-bullet 票, 逐票声明 blocking edges (哪些票必须先完成); 宽面重构不走切片, 改走 expand–contract 序列。
- 向用户求证: 以编号清单展示各票的标题 / 阻塞关系 / 交付物, 按反馈迭代粒度与依赖边, 直到用户认可。
- 发布: 按依赖顺序 (blocker 在前) 逐张发到已配置的 tracker — 本地每票一个 md 文件, 或真实 tracker 每票一个 issue。

- 垂直切片规则 (核心转换逻辑): 每张票贯穿 schema/API/UI/测试各层的一条窄而完整的路径, 独立可演示或可验证, 体量以'单个全新上下文窗口装得下'为准; 需要预重构则先做预重构。
- 依赖建模与校验: 每票声明 blocking edges, 编号与发布均按依赖序; 无阻塞的票立即可开工 (从 frontier 推进); 宽面重构例外 — 先并排加新形态, 按影响面分批迁移调用点保持 CI 持续绿, 最后单独一票删旧形态收口; 发布前用向用户求证这一步做人工校验。
- 发布落点与外部依赖: 唯一外部依赖是 /setup-matt-pocock-skills 配置的 issue tracker (未配置则提示用户先跑 setup) — 本地文件形态写 `.scratch/<feature-slug>/issues/NN-<slug>.md` 单票单文件 (含验收勾选项, 状态 ready-for-agent); GitHub/Linear 等真实 tracker 则用平台原生 blocking/sub-issue 关系; 内容上避免具体文件路径和代码片段以防过期。
