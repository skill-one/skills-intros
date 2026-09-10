# writing-skills (`obra/superpowers/writing-skills`)

## whitebox

- 判断是否值得做成 skill: 技术非直觉、可跨项目复用才建; 一次性方案、常规惯例直接否掉。
- 先跑基线测试 (RED): 设计压力场景派给 subagent (子代理), 记录它没有 skill 时如何失败、用什么借口违规。
- 针对基线暴露的具体违规和借口写 SKILL.md (存放在如 ~/.claude/skills/ 的技能目录)。
- 重跑相同场景验证 (GREEN): agent 现在能遵守规则才算通过, 不过关就改。
- 重构补漏: 回归中出现的新借口逐条封堵 (借口表、明文禁止变通), 再验证直至稳定。

- TDD 映射: 测试用例=subagent 压力场景, 被测产物=SKILL.md; 铁律是没见过失败基线就不写 skill, 对已有 skill 的编辑同样适用。依赖 subagent 能力执行测试。
- 防借口 (Bulletproofing): 基线出现的每个借口进借口表并明文封死每个变通路径; 先按失败类型选形式——压力下违规用'禁止+借口表', 输出形状错误用'正面配方'(堆禁止条款反而适得其反)。
- 可发现性 (SDO) 与省 token: description 只写触发条件 'Use when...'、绝不总结流程 (防止 agent 只读描述走捷径); 跨引用其他技能用名称+REQUIRED 标记、禁用 @ 语法强制加载; 高频技能控制在 200 词内。流程图仅在非直观决策点使用, 用 graphviz dot 编写、由技能目录自带 render-graphs.js 渲染成 SVG。
