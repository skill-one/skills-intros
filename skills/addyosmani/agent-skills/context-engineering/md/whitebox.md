# context-engineering (`addyosmani/agent-skills/context-engineering`)

## whitebox

- 诊断触发场景 (新会话/输出质量退化/切换任务), 对照红旗清单 (捏造 API、偏离约定、会话越长质量越差、无规则文件) 确认是上下文问题
- 审计五层上下文层级: 规则文件 → 规格文档 → 相关源码 → 错误输出 → 会话历史, 找出缺失层、过时层、被淹没层
- 按任务选择性装载: 只取当前任务相关的部分, 控制在 <2,000 行, 任务关键内容排在上下文末尾
- 多步任务执行前先发轻量 PLAN; 遇歧义或需求缺口时以 CONFUSION/MISSING REQUIREMENT 块列出选项 A/B/C, 停下询问而非擅自猜测
- 执行后按验证清单核对: 规则文件存在、输出引用真实项目文件与 API、长会话中持续修剪失效内容并保护任务关键信息

- 分层装载协议: 第 1 层规则文件常驻每个会话 (按 agent 工具选格式: CLAUDE.md / .cursorrules / .windsurfrules / copilot-instructions.md / AGENTS.md), 覆盖技术栈、命令、约定、边界; 第 2~4 层按需装载; 上下文打包用三种结构模板: Brain Dump (会话开始全量结构化输入)、Selective Include (只含相关文件+模式示例+约束)、Hierarchical Summary (大项目分区索引)
- 预算与排序: 75% 容量即开始修剪, 不等窗口满 (满了注意力已碎片化); 压缩优于删除 — 把失败尝试/冗长工具输出压成一句结论, 决策保留、细节丢弃; 保护项: 原始任务定义、当前报错、正在编辑的文件; 任务关键内容置尾, 依据 lost-in-the-middle 效应 (Liu et al., 2023)
- 外部依赖: 本技能零代码、零自研库、不绑定特定模型, 纯操作规程; 唯一可扩展点是 MCP 服务器作为上下文来源 (按需选接): Context7 (自动拉取库文档)、Chrome DevTools (浏览器实时状态)、PostgreSQL (schema 与查询结果)、Filesystem (项目文件)、GitHub (issue/PR)
