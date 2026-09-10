# ai-research-reproduction (`lllllllama/rigorpilot-skills/ai-research-reproduction`)

## whitebox

- 先读 README，由内置 repo-intake-and-plan 阶段从仓库提取文档化命令与可跑目标。
- 选定并论证最小可信目标：文档化推理/评测优先，完整训练须用户明确确认。
- 跑 env-and-assets-bootstrap，只补齐该目标所需的环境、checkpoint、数据集与缓存。
- 用 minimal-run-and-audit 执行目标（训练目标则走 run-train），所有命令在确定性入口 orchestrate_repro.py 下运行并留存证据。
- 在记录的容差内比对显式预期指标后才授予 result-match，随后写出标准化 repro_outputs/ 产物包（SUMMARY/COMMANDS/LOG/status.json/ANNOTATED_README 等）。

- 确定性编排与运行留痕：入口 scripts/orchestrate_repro.py 自带 _bundled/ 独立运行时（单独安装即可工作，伴生 skill 可选）；每次执行按 run_id 写入生命周期状态、append-only 事件流和完整 stdout/stderr 到 repro_outputs/_runtime/<run_id>/，运行目录放 CANCEL 文件即触发进程树取消；可选 agent 循环走 scripts/run_agent.py。
- README 逐字节保真校验：ANNOTATED_README.md 逐字节重放原 README（保留图片/GIF/视频/HTML 标记），仅在每个标题块后加一条彩色标注，必须通过内置 strip/check 往返校验才会保留。
- 补丁边界与结果判定：默认不改仓库（优先命令行参数/环境变量/依赖版本修复），确需改动则建 repro/YYYY-MM-DD-short-task 分支并在 PATCHES.md 记录对 README 保真度的影响；result-match 只有在显式预期指标按记录容差比对通过后才授予（仅有观测值不算复现成功）；失败与后解决的运行经 shared/scripts/lessons_store.py 自动归档为 lessons（RIGORPILOT_LESSONS=0 可关闭）。技能未指定任何外部模型 API，工具依赖即上述自带脚本。
