# api-and-interface-design (`addyosmani/agent-skills/api-and-interface-design`)

## whitebox

- 识别任务类型: 新端点、模块边界、组件 props、公共接口变更之一 (对应 When to Use 清单)
- 契约先行: 用 TypeScript interface 先写出输入/输出类型, 类型即文档, 实现跟随契约
- 套核心规则: 统一错误体 (HTTP 状态码 + code/message/details)、只在系统边界校验、只加可选字段不改旧字段、按命名约定表取名
- 状态变更端点补幂等设计: 客户端生成 key、唯一约束原子抢占、requestHash 拒绝同 key 异载荷
- 逐项过 Verification 检查单, 全部通过后交付设计

- 类型驱动: 判别联合 (discriminated union) 表达状态变体、branded type 防止 TaskId/UserId 串用、输入输出类型分离; 全程靠 TypeScript 类型系统, 不依赖外部模型或工具调用
- 边界校验: 校验只发生在系统边缘 (API 路由、表单提交、第三方响应、环境变量), 内部代码直接信任类型; 第三方 API 响应一律视为不可信数据; 用 schema.safeParse 风格的校验库 (示例依赖 Zod 类库)
- 幂等即实现: 拒绝 check-then-act (先查后写是竞态), 用数据库唯一约束一次操作定胜负; 处理中的重复请求按策略返回 409/阻塞等待/202; key 保留期必须长于最长重试链 (含死信队列重放)
