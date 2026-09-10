# documentation-and-adrs (`addyosmani/agent-skills/documentation-and-adrs`)

## whitebox

- 识别触发点: 出现架构决策、API 变更、功能上线等值得记录 "为什么" 的时刻
- 先扫描仓库已有约定: 检查现有 ADR 的位置/格式/编号, 以及 CLAUDE.md、.adr-dir 等配置; 有约定则遵循, 不自创
- 按模板写 ADR (Context → Decision → Alternatives Considered → Consequences), 存入 docs/decisions/ 并续接现有编号
- 补内联文档: 注释只写 why 不写 what, 在关键处记录已知坑 (gotcha), 删除注释掉的代码和过期 TODO
- 按 Verification checklist 核验: 重大决策有 ADR、README 可跑通、API 有参数/返回类型文档、无残留注释代码

- 约定探测优先于默认模板: 先匹配项目现有 ADR 的目录、文件扩展名 (Markdown vs reStructuredText)、编号命名 (如 ADR-004-Title.rst / 0004-title.md), 可识别 adr-tools 等工具配置; 证据冲突时上报给用户, 不默默引入新方案
- ADR 生命周期管理: 旧 ADR 永不删除 (保留历史上下文), 决策变更时写新 ADR 引用旧版并标注 Superseded; 状态流转 PROPOSED → ACCEPTED → SUPERSEDED/DEPRECATED
- 文档分层输出: 代码注释只记非显然意图; REST API 用 OpenAPI/Swagger, TypeScript 接口用类型注解 (@param/@throws/@example); README/Changelog/CLAUDE.md (供 AI agent 读取的约定文件) 按固定结构生成; 不依赖外部模型 API
