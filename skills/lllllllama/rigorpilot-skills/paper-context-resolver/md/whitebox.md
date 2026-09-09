# paper-context-resolver (`lllllllama/rigorpilot-skills/paper-context-resolver`)

## whitebox

- 接收编排方 (orchestrator) 传入的四类输入: 目标仓库元信息、具体复现问题、已有 README/仓库证据、已知论文链接。
- 过适用性闸门: 校验问题确属 README/仓库留下的窄缺口 (数据集版本/划分、预处理、评测协议、checkpoint 映射、运行时假设五类之一); 若仅是论文标题、要求全文总结、或 README 已给出足够细节, 则不进入主流程。
- 按技能内参考文档 references/paper-assisted-reproduction.md 的指引, 从原始论文来源中定位并解析该具体细节。
- 输出收窄后的来源清单 + 仅回答该复现问题; 若发现 README 与论文冲突, 显式记录冲突; 并区分哪些是直接证据、哪些是推断。

- 适用性闸门 (输入校验): 双向判定 — 四类输入齐全且问题落在五类复现关键缺口内才触发; 逆向排除纯论文讲解、无具体问题的标题查询。定位为 helper-tier 技能, 通常由主流程编排方调用, 补充而非替代 README-first 主流程。
- README-first 冲突记录: 只做窄证据补充, 不覆盖 README 指引; 一旦论文与 README 矛盾, 必须在输出中显式注明冲突 (不记录冲突就推翻 README 属于越界行为)。
- 证据纪律 (输出转换): 交付收窄的来源清单, 只回答复现相关问题 (不做全文摘要), 并明确区分直接证据与推断。依赖: SKILL.md 仅声明本地参考文档 references/paper-assisted-reproduction.md, 未声明任何外部工具/库/模型 API。
