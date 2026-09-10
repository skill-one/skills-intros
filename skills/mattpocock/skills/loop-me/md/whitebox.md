# loop-me (`mattpocock/skills/loop-me`)

## whitebox

- 用户手动以 `/loop-me [想设计的工作流]` 触发 (skill 声明 disable-model-invocation: true, 模型不能自启)
- 若 NOTES.md 为空或太薄, 先访谈用户真实世界 (日常工具、信息渠道、他自己的行话), 把原始笔记落进 NOTES.md
- 以 grilling 方式推进: 一次只发一轮问题, 每问附一个推荐答案; 用 'loop 视角' 盘问——把用户的生活看成可循环、可委托的模式, 也会主动指出他没意识到的循环
- 随盘问结论实时创建/修改/删除 workflows/*.md 里的工作流规格; 模糊说法一旦收敛就固化为 NOTES.md 中的规范术语
- 判定完成: 实现者 agent 能照规格零提问地建出来 → 会话结束; 否则继续盘问

- 状态外置于文件系统: workflows/*.md 是唯一事实源 (每个工作流一份规格), NOTES.md 存用户世界的原始笔记与规范术语——无内存态, 跨会话靠文件续接
- 复用上游 /grilling 会话纪律 (skill 声明'运行一个 stateful /grilling 会话', 但该技能定义不在本文档内): 多轮追问、每问带推荐答案、人在回路的 checkpoint 尽量后推 (push right); 注意 Trigger/Checkpoint/Brief 只是词汇表, 不强制任何结构——无 AI/无 checkpoint/无定时均可, 一切由盘问结果决定
- 硬性完成标准做校验: '实现者无需问任何一个问题就能构建' 是唯一 done 条件, 有问题残留就未完成; 产出面向 checkpoint 的 Brief 是决策摘要而非原始草稿 (是什么、为什么、链接到资产)
- 无外部工具/库/模型 API 依赖: 全部能力来自 prompt 指令 + 工作区文件读写, 唯一外部依赖是对 /grilling 技能的引用
