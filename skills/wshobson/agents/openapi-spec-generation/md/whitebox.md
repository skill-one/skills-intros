# openapi-spec-generation (`wshobson/agents/openapi-spec-generation`)

## whitebox

- 确认任务类型命中技能范围：建 API 文档、从代码生成 spec、design-first 契约设计、校验实现一致性、生成 SDK 或搭文档门户之一
- 按场景表选设计路径：新 API 走 design-first（先写 spec），已有代码走 code-first（从代码生成），演进中的 API 走 hybrid（代码注解+生成）
- 以 OpenAPI 3.1 YAML 骨架组织输出：openapi / info / servers / paths / components（schemas、securitySchemes）
- 需要具体模板或完整示例时，按需读取 references/details.md 模板库
- 过一遍最佳实践清单后交付：$ref 复用、真实示例、错误码、版本化、显式 nullable、server 变量

- 格式解析：一切产出锚定 OpenAPI 3.1 规范结构（paths → operations → components），按 design-first / code-first / hybrid 三条路线决定 spec 与代码的先后关系
- 约束校验：生成时内嵌一组 Do/Don't 规则作检查——$ref 复用 schema/参数/响应、安全方案齐全、null 显式声明、命名风格统一、URL 不硬编码（用 server 变量）、语义化版本号
- 外部依赖：技能本身不调用任何外部库或模型 API，唯一按需读取的资源是本地模板库 references/details.md（存放完整模板与详细示例）
