# explore-code (`lllllllama/rigorpilot-skills/explore-code`)

## whitebox

- 1. 门控校验: 确认研究者明确授权探索性改动, 且任务在范围内 (模块移植 / backbone 适配 / 插 LoRA·adapter / 换 head 等低风险迁移), 否则拒接或转交兄弟 skill。
- 2. 建立隔离: 在独立 branch 或 worktree 上工作, 保证候选改动不污染可信基线。
- 3. 实现候选: 以源码为锚的复制 + 最小适配, 用 scripts/plan_code_changes.py 规划改动, 不做自由重写。
- 4. 记录回滚信息: 写明改动为何有意义、如何回滚、为何仍是 candidate 而非已验证贡献。
- 5. 落盘产出: 用 scripts/write_outputs.py 写出 explore_outputs/ 五件套 (CHANGESET.md / SCIENTIFIC_CHANGELOG.md / COMPARABILITY_REPORT.md / TOP_RUNS.md / status.json); 训练执行可交接给 minimal-run-and-audit 或 run-train。

- 边界门控: 只接受明确授权的隔离探索任务; 基线复现、保守调试、端到端探索编排、大重构一律不接, 涉及跨域协调时转给 ai-research-explore, 执行阶段交接 minimal-run-and-audit / run-train。
- 源锚定最小适配: 依赖 references/explore-policy.md + 共享的 agent-operating-principles.md / research-rigor-principles.md 约束改动方式; 用 scripts/plan_code_changes.py 做变更规划, 保证每处改动可溯源。
- 可审计产出: scripts/write_outputs.py 生成 explore_outputs/ 下的 CHANGESET.md、SCIENTIFIC_CHANGELOG.md、COMPARABILITY_REPORT.md、TOP_RUNS.md、status.json, 记录候选理由、回滚路径与候选/已验证状态, 支持对比可比性。
