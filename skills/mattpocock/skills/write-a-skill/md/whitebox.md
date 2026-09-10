# write-a-skill (`mattpocock/skills/write-a-skill`)

## whitebox

- 问需求: 向用户确认技能覆盖的任务领域、具体用例、是否需要可执行脚本、是否附参考资料
- 起草: 按固定模板生成 SKILL.md —— frontmatter (name/description) + Quick start + Workflows + Advanced features
- 按需扩展: 内容超 500 行或领域不同则拆 REFERENCE.md/EXAMPLES.md, 确定性操作 (校验/格式化) 则写 scripts/ 下的工具脚本
- 复盘: 把草稿交给用户, 逐项确认覆盖度、缺失点、各节详略, 按反馈迭代
- 终检: 过一遍 Review Checklist (有触发词、<100 行、无时效信息、术语一致、有具体示例、引用只一层) 后交付

- 触发靠 description 字段: 它是 agent 决定是否加载技能前唯一可见的信息, 要求第三人称写 '第一句做什么 + 第二句 Use when 具体触发词/场景' (≤1024 字符), 好坏示例的差别就在能否与其他技能区分
- 渐进披露: SKILL.md 控制在 100 行内保证低加载成本, 少用的进阶内容外移到 REFERENCE.md/EXAMPLES.md, 引用深度只允许一层
- 零外部依赖: 不调用任何外部工具/库/模型 API, 产出物就是纯 Markdown 文件; 唯一 '代码' 是为目标技能附带的 utility scripts (如 helper.js), 用于替代反复现场生成相同代码
