# data-storytelling (`wshobson/agents/data-storytelling`)

## whitebox

- 触发判断: 识别任务属于"把数据讲给人听"的场景 (向高管汇报、季度回顾、投资人演示、数据报告、给非技术人讲洞察)
- 提炼钩子: 从数据中找出最关键/最反直觉的那个洞察, 前置到开头 ("so what" 优先)
- 套故事骨架: 按 Setup (背景基线) → Conflict (问题或机会) → Resolution (洞察与建议) 组织全部内容
- 三支柱装配: 每个部分补齐 Data (数字证据) + Narrative (含义与因果) + Visuals (图表/高亮)
- 红线裁剪收尾: 按 Do/Don't 删掉数据堆砌、术语、方法论前置; 以明确的 Call to Action 收尾; 细节不够时查 references/details.md

- 双模板驱动输出: 三个结构模板固定套用——故事结构 (Setup→Conflict→Resolution)、六段叙事弧 (Hook→Context→Rising Action→Climax→Resolution→Call to Action)、三分法 (要点/对比各限 3 个), 内容填入固定骨架, 不自由发挥结构
- 三支柱校验 + 硬规则裁剪: 每个输出点检查是否同时具备证据/含义/视觉三要素; 内容按 Don't 清单做减法 (禁数据堆砌、禁埋没洞察、禁术语、禁方法论先行), 按 Do 清单做加法 (洞察前置、贴合受众目标)
- 零外部依赖: 无任何外部工具、库或模型 API; 唯一的"外部"资源是本地文件 references/details.md (详细模式与案例库), 仅在 skill.md 导航层不够用时按需读取; 所有转换由模型按 skill.md 文本指令完成
