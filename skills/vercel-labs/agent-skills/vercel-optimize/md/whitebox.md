# vercel-optimize (`vercel-labs/agent-skills/vercel-optimize`)

## whitebox

- 预检与采集: 读 package.json 识别框架, 通过 Vercel CLI 拉取 14 天生产指标 (metrics/usage/contract), 扫描代码库, 合并为 signals.json
- 阻断检查: 校验框架支持、项目链接与账号 scope、Observability Plus 可用性, 任一阻断即停下向用户确认, 不静默降级
- 确定性筛选: gate-investigations.mjs 依据指标证据选出至多 6 个代码候选 + 平台级建议, 排除无指标支撑的方向
- 逐候选深挖: 为每个候选生成调查简报 (brief), 只读简报列出的文件, 输出 JSON 建议或'无需改动'结论, 再 reconcile 汇总
- 校验并渲染: verify-and-regen.mjs 校验文件/引用/框架版本并重生成失败项, render-report.mjs 产出报告, 原样打印 final-message.json 后停止

- 指标先行 + 确定性门控: 调查对象完全由脚本从 Vercel 生产信号 (14 天固定窗口, 依赖 Vercel CLI v53+ 与 Observability Plus) 决定; 代码阅读范围被限定为候选文件及其路由局部导入链, 禁止全库 grep
- 管道式 JSON 工件传递: 各阶段 (collect/merge/gate/deep-dive/reconcile/verify/render) 由 Node.js 20+ 脚本串联, 每步消费并产出结构化 JSON 工件 (存于独立临时 run 目录), stdout 与 stderr 分离, 校验失败即中止
- 版本感知的输出校验: verify 阶段抽取建议中的声明, 核对引用的文件与行号; 引用只能来自 references/docs-library.json 且须匹配检测到的框架版本, 不合格引用被剔除、不合格建议按 regenPlan 重生成; 建议只允许定性成本措辞, 禁止具体 $N 金额
