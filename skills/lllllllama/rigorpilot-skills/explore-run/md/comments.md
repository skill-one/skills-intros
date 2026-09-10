# explore-run (`lllllllama/rigorpilot-skills/explore-run`)

## comments

- user: 研二炼丹新手, category: 坑, comment: 我把 TOP_RUNS 的分数直接当结论写进周报, 被导师打回——那是小子集短跑的 bounded evidence, 只能用来排序候选, 不能当可信结果。
- user: 第一次用的实习生, category: 注意, comment: 别只说'帮我试几个配置', 不显式授权探索它不会走这套流程。要说清'授权探索性运行', 并给 variant_axes 和预算, 才能得到候选排序。
- user: 实验室管GPU的, category: 妙用, comment: 周末 GPU 闲置, 配好 variant_axes 挂机跑短周期 probe, 周一 TOP_RUNS.md 直接告诉我哪几个值得全量训练, 一晚筛掉大半废配置。
- user: 带学生的副教授, category: 妙用, comment: 最值钱的是 COMPARABILITY_REPORT.md: 它会明说哪些对比不公平。以前学生拿不同子集的结果硬比, 现在坑先被标出来了。
- user: 组里做复现的, category: 注意, comment: selection_weights 默认偏保守, TOP_RUNS 总是低成本稳候选排前。想博高收益要显式给权重, 再用 max_variants 控住预算别撒太多。
- user: 冲SOTA被拒稿的, category: 启发, comment: 想靠它直接出 SOTA 结论文档的省省, 它明确不做可信结论。我改成先探索排序、再用可信跑验证, 反而少跑了一堆废实验。
