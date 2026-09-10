# safe-debug (`lllllllama/rigorpilot-skills/safe-debug`)

## whitebox

- 触发识别: 用户贴入具体失败症状 (traceback、CUDA OOM、checkpoint 加载失败、shape 不匹配、NaN loss 等训练失败) 且期望先诊断后改码, 才接单。
- 先诊断: 只做根因定位与收敛分析, 默认不改动任何仓库代码。
- 提最小补丁: 给出最小修复方案后停下, 等待用户明确批准, 未批准不动手。
- 风险升级: 若变更为中/高风险, 先建议创建 savepoint (存档点) 或分支再继续。
- 产出三件套: 写出 debug_outputs/DIAGNOSIS.md、PATCH_PLAN.md、status.json。

- 症状路由与边界拒绝: 按 skill.md 的适用/不适用清单分流 —— 有具体报错+要保守诊断才处理; 泛化重构、无故障的仓库导览、投机性代码改编、大范围可读性重写一律拒单。
- 参考文档驱动诊断: 全程遵循四份本地参考文件 —— debug-policy.md (调试策略)、research-rigor-principles.md (科研严谨原则)、research-pitfall-checklist.md (科研坑清单)、与 ai-research-reproduction 技能共享的 agent-operating-principles.md (操作原则); 不依赖任何外部工具、库或模型 API。
- 人工审批闸门 + 贡献边界声明: 一切代码变更需显式批准、高风险先建分支/存档; 且若补丁会改变实验含义或结果可比性, 必须显式声明 '调试修复 ≠ 研究贡献'。
