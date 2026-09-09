# minimal-run-and-audit (`lllllllama/rigorpilot-skills/minimal-run-and-audit`)

## whitebox

- 前置校验: 确认输入齐备——已选定的复现目标、可运行的 (smoke/文档化推理/评估) 命令、环境与资产假设; 任一未定义则不执行 (非主路径)
- 用 scripts/run_command.py 执行给定命令, 捕获执行证据并产出执行结果摘要
- 依据 references/reporting-policy.md, 用 scripts/write_outputs.py 把证据归一化写入标准化 repro_outputs/ 文件
- 若执行中仓库文件有改动: 写 PATCHES.md, 并在 SCIENTIFIC_CHANGELOG.md 记录科学含义变化, 另出 COMPARABILITY_REPORT.md 做 README/论文/基线可比性对比
- 按证据状态给出结论, 明确区分 verified / partial / blocked 三态

- 执行层: scripts/run_command.py 统一执行命令并留存证据; 也接收主 skill 或薄助手传入的证据——本技能只负责归一化报告, 不自选复现目标, 不管训练启动/续训
- 报告层: scripts/write_outputs.py + references/reporting-policy.md 决定输出格式; 共享运行原则来自 ../ai-research-reproduction/references/research-rigor-principles.md 与 agent-operating-principles.md
- 审计门禁: 不把风险代码改动洗白为可接受做法, 必须隐藏任何改变评估/预处理/checkpoint/指标等科学含义的改动 → 全部显式落到 PATCHES.md 与 SCIENTIFIC_CHANGELOG.md
