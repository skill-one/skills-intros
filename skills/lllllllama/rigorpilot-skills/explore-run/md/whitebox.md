# explore-run (`lllllllama/rigorpilot-skills/explore-run`)

## whitebox

- 确认触发条件: 研究者已明确授权探索性运行 (小样本验证/短周期试跑/批量扫描等), 否则不适用本 skill
- 解析 variant spec (variant_axes/subset_sizes/short_run_steps/selection_weights/primary_metric/metric_goal), 构建候选维度网格
- 按 cost / success_rate / expected_gain 三因素打分选候选, 默认保守权重, 再按 max_variants / max_short_cycle_runs 做预算剪枝
- 优先安排小样本、短周期检查; 把实际命令执行交接给 minimal-run-and-audit 或 run-train, 并保持探索状态与可信基线隔离
- 一旦有真实执行结果, 排名切换为真实执行证据, 并写出 explore_outputs/ 下五份输出文件

- 候选规划与打分: scripts/plan_variants.py 按 explore-variant-spec.md 的约定解析 variant_axes / subset_sizes / selection_weights 等字段, 用保守默认权重做启发式预执行排序, 并通过 max_variants / max_short_cycle_runs 剪枝
- 执行交接与隔离: 本 skill 只负责探索执行的规划与总结, 实际跑命令交给 minimal-run-and-audit / run-train; 探索实验状态与 trusted baseline 隔离; 判断依据来自 references/execution-policy.md、deep-learning-experiment-principles.md、agent-operating-principles.md
- 证据输出与边界声明: scripts/write_outputs.py 生成 explore_outputs/CHANGESET.md、SCIENTIFIC_CHANGELOG.md、COMPARABILITY_REPORT.md、TOP_RUNS.md、status.json; 结果一律标注为 bounded evidence (有界证据), COMPARABILITY_REPORT.md 声明哪些对比并不公平, 不做过度结论
