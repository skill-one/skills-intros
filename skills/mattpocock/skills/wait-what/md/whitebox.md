# wait-what (`mattpocock/skills/wait-what`)

## whitebox

- 用户显式触发本技能 (frontmatter 声明 disable-model-invocation, 模型不能自行调用)
- 读取仓库中的 CONTEXT.md; 若仓库里有多个, 先查 CONTEXT-MAP.md 定位正确的那份
- 对上一条消息做 re-pitch: 补充少量上下文, 把它重新讲清楚
- 按 ASD-STE100 Simplified Technical English 的写法输出, 术语统一取自 CONTEXT.md 的 ubiquitous language (术语表)

- 触发门禁: disable-model-invocation: true, 仅用户手动调用, 适用场景是"上一条消息没被理解, 要求重讲"
- 词汇路由: CONTEXT.md 是唯一术语来源; 多个 CONTEXT.md 时由 CONTEXT-MAP.md 充当索引做分发
- 语言改写: 输出强制为 ASD-STE100 简化技术英语 (受控英语规范, 非外部工具); 全程只读仓库文件, 不调用任何工具/库/模型 API
