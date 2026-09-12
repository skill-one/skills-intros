# lavish (`kunchenguid/lavish-axi/lavish`)

## whitebox

- 判定输入: 若 /lavish 后带参数 ($ARGUMENTS 非空) 则按参数定主题, 为空则从对话推断该可视化的内容 (计划、对比、表格、代码 diff、报告等)。
- 先跑 npx -y lavish-axi (--help / design / playbook <id>) 取最新工作流与设计指南 — skill.md 明确要求不遵循文件内嵌说明, 因为安装副本会过期。
- 按取回的指南生成 HTML 工件: 把原本要用纯文字表达的内容转成页面形式。
- 执行 npx -y lavish-axi <html-file> (免全局安装) 在浏览器打开页面, 供人查看并标注。
- 若 CLI 输出给出以 lavish-axi 开头的后续命令, 改写为 npx -y lavish-axi ... 运行, 进入"人标注 → 反馈回流 agent"的评审循环。

- 解析/分流: 以 $ARGUMENTS 是否为空作开关 — 非空 = 显式调用, 按参数构建; 空 = 从对话上下文推断; 判定要不要触发的标准是"作为页面比作为文字更易读"的内容 (计划、对比、图、表、代码 diff、报告、评审循环)。
- 转换: 依据运行时从 CLI 取回的指南, 把文字意图转换成可批注的 HTML 页面; design 命令提供设计方向优先级与当前代码片段, playbook <id> 提供特定工件类型的聚焦指南。
- 校验/防过期: skill.md 自声明"文件内嵌的工作流/设计/流程说明会过期", 唯一可信来源是运行时 CLI 输出; 因此先取指南再动手, 且任何后续命令强制以 npx -y 前缀执行。
- 外部依赖: 仅 lavish-axi CLI (经 npx -y 按需拉起, Node.js 包执行器) + 浏览器 (负责展示与人工标注); skill.md 未提及任何模型 API 或其他库, 故不虚构。
