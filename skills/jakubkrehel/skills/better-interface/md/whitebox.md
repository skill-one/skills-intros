# better-interface (`jakubkrehel/skills/better-interface`)

## whitebox

- 先定范围: 从请求与工作区推断待评审的界面/流程/仓库; 若给的是分支、PR、提交区间或未提交改动, 则改判为变更评审并让用户去跑 interface-review (本技能不处理)。
- 先侦察后评审: 识别框架、样式体系、组件库、设计 token、支持的视口和可用的预览/测试命令, 并阅读项目自述文档 (CONTRIBUTING.md、CLAUDE.md、设计系统文档等) 以确定 finding 归属。
- 按固定顺序跑六个领域评审: accessibility → layout → writing → typography → colors → ui, 每域引用其检查清单, 收集带 path/to/file:line 的证据; 运行时行为相关的视觉结论须实际操作界面验证。
- 合并收口: 一根因一条 finding 并列出全部位置, 套用统一严重度与升级触发器, 上限 15 条按用户影响排序, 同级优先选影响面大、一次修复收益高的。
- 按 review-format.md 输出唯一一份报告: 范围与覆盖面 (含未覆盖的领域/状态)、findings 表、验证结果、Approve/不通过结论。

- 路由与所有权 (解析核心): 本技能只做编排, 规则全部委托给六个 better-* 领域子技能; 一个问题只归其底层规则的领域所有, 报一次并注明次要影响; 某领域技能不可用就标 Not reviewed, 绝不凭记忆重造其规则。依赖物: better-accessibility/layout/writing/typography/colors/ui 六个子技能、变更评审入口 interface-review (用户主动调用, 本技能无法代启)、输出模板 review-format.md。无第三方库或模型 API 依赖。
- 证据闸门 (校验): 每条 finding 必须引用 path/to/file:line 并展示现状代码; 视觉类结论不能只靠源码推断、代码类结论不能只靠截图推断, 须实测渲染状态并报出确切命令/交互与结果, 测不了的标 Not verified; 刻意的项目选择不算问题, 只报证据而非口味。
- 严重度与修复阶梯 (转换): 13 条升级触发器一票定 HIGH 不得摊薄 (如无可访问名称、无焦点指示、仅靠颜色传义、破坏性操作无确认等); 修复按成本取最早的可行解: 删除 → 用平台原生 → 复用项目已有 token/组件 → 修正数值 → 新增; 在该删的地方新增, 本身就是一条 finding。评审默认只读, 除非用户同时要求落实修复。
