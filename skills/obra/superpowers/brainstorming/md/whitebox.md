# brainstorming (`obra/superpowers/brainstorming`)

## whitebox

- 先分类请求为 spike（可行性探针）/ bounded（小改动）/ architectural（新项目或重构），并当面宣布走哪条路，定下流程轻重
- 探索项目现状（文件、文档、近期提交），然后一次只问一个问题，澄清目的、约束、成功标准
- 呈现设计：bounded 在聊天里给几句话的短设计；architectural 先提 2-3 个带权衡的方案，再分节展示设计并逐节确认
- 停下等用户明确批准——批准前不写任何代码、不搭脚手架、不调用任何实现技能
- 批准后按路径收尾：spike 报告结论（代码标注为一次性）；bounded 直接进入常规开发流程；architectural 把设计写成 spec 文档、自审、请用户复审，然后调用 writing-plans 技能

- 三路径分类门（解析入口）：按任务性质决定流程产物（spike→答案，bounded→聊天内短设计，architectural→完整 spec）；两个路径间拿不准就取更重的；中途发现隐藏复杂性只能单向升级，绝不降级
- HARD-GATE 审批门（校验核心）：一切实现动作（写代码/建项目/调其他实现技能）前必须先展示意图并获得明确批准；设计长度随任务缩放，但审批门永不缩水——哪怕改个配置也要过；spike 获批也只覆盖探针本身，后续改动需重新分类重新批准
- 产出与移交（转换出口）：architectural 路径将设计写入 docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md 并 git 提交，随后自审（占位符/内部一致性/范围/歧义四项）并请用户复审；终态由路径绑定，唯一可调用的下游是 writing-plans 技能。依赖：git、可选的浏览器版 visual companion（首次遇到'展示比描述更清楚'的问题时单独一条消息提供）、可选的写作润色技能；不依赖任何外部库或模型 API
