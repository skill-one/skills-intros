# nodejs-backend-patterns (`wshobson/agents/nodejs-backend-patterns`)

## whitebox

- 接任务: 创建 Node.js 服务 (REST API、GraphQL 后端、微服务等)
- 判断现有导航层级是否够用, 不够则读取 references/details.md 获取详细模式
- 用 Express/Fastify 搭建: 中间件、错误处理、认证、数据库集成
- 套用最佳实践清单: TypeScript、输入校验、日志、限流、连接池、健康检查等
- 按单元/集成/E2E 测试模式补测试, 测试细节引用 javascript-testing-patterns 技能

- 分层知识加载: skill.md 只放导航级概览, 深度实现细节存放在 references/details.md, 按需读取
- 工程约束机制: 强制 TypeScript 类型安全、自定义错误类、Zod/Joi 输入校验、环境变量管理密钥、结构化日志 (Pino/Winston)
- 外部依赖: Express/Fastify 框架, Zod/Joi 校验库, Pino/Winston 日志库; 测试方案不在本技能内, 委托给 javascript-testing-patterns 技能
