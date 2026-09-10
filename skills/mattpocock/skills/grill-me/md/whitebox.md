# grill-me (`mattpocock/skills/grill-me`)

## whitebox

- 用户显式点名触发 grill-me — frontmatter 声明 disable-model-invocation: true, 模型不会自动调用, 必须用户手动触发
- 加载 skill.md, 全文只有一条指令: 用 "grilling" 调用 Skill tool
- Agent 按指令调用 Skill tool, 传入参数 "grilling"
- grilling 技能加载并接管对话, 对用户的 plan/design 展开不留情面的连续追问, 直到方案被打磨锋利

- 触发闸门: frontmatter 的 disable-model-invocation: true 是一道防误触校验 — 只允许用户主动调用, 杜绝模型自作主张空转
- 单一委托: 本体零业务逻辑, 解析后的唯一动作是把执行权转交给 Skill tool 的 "grilling" 技能; 具体的追问与打磨逻辑全部在 grilling 内部, 本 skill.md 未展开其细节
- 零外部依赖: 未引用任何外部库、文件或模型 API, 唯一依赖是宿主环境提供的 Skill tool
