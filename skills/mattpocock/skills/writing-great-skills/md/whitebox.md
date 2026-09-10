# writing-great-skills (`mattpocock/skills/writing-great-skills`)

## whitebox

- 定触发方式: 技能需被模型自主 (或其他技能) 到达则 model-invoked, 仅手动触发则 user-invoked 以省 context 负担
- 写 description: leading word 前置, 每个 branch 一个触发条件, 删去正文已含的身份信息
- 内容放上信息阶梯: 有序步骤 (带可检验、穷尽的完成标准) 留在 SKILL.md, 仅部分分支需要的材料用 context pointer 推到链接文件
- 评估拆分: 有独立 leading word 或他技能需到达 → 按触发方式拆; 后续步骤诱发抢完成 → 按顺序拆; 划算才拆
- 逐句修剪: 单一事实来源, 删 no-op 与 duplication, 用 leading word 折叠重复表述

- 解析 — 信息阶梯分层: 按即时性把内容归为 in-skill step (带可检验完成标准) / in-skill reference / pointer 后的外部参考; branch 决定哪些内联、哪些披露。本技能自身纯 reference, 术语定义披露到同级 GLOSSARY.md
- 转换 — leading word 折叠 + 渐进披露: 调用模型预训练已有的紧凑概念 (如 _red_、_tight_) 把多处重述收成一个词, 把仅部分分支需要的材料移到链接文件。依赖仅 LLM 自身先验, 无外部工具/库/模型 API
- 校验 — 逐句 no-op 测试 + 完成标准检查: 每句问「相比默认行为是否改变」, 每步完成标准须可判 done/not-done 且穷尽, 直接对抗 premature completion
