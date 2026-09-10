# email-sequence (`coreyhaines31/marketingskills/email-sequence`)

## whitebox

- 先读取 .agents/product-marketing-context.md（旧版 .claude/）获取产品上下文，只对仍缺失的信息提问：序列类型、受众、目标。
- 将需求匹配到内置序列类型（welcome / nurture / re-engagement / onboarding 等），按策略表确定长度与间隔（如 welcome = 5-7 封、12-14 天、欢迎信即时发送）。
- 按该类型的固定邮件骨架逐封套写（如 welcome: 交付价值→速赢→故事→社会证明→处理异议→转化）。
- 每封邮件按文案规范写作：单封单一职责 + 单一 CTA、先价值后推销、短段落、50-125 / 150-300 / 300-500 字三档。
- 以固定输出格式交付：Sequence Overview + 每封邮件块（Subject/Preview/Body/CTA）+ Metrics Plan。

- 上下文文件优先：条件式读取 `.agents/product-marketing-context.md`，已覆盖的问题不再向用户重复问，只补缺口——本质是提问前的静默前置解析。
- 查表式生成，非自由发挥：邮件数量、发送间隔、邮件顺序全部来自 SKILL 内置的类型策略表与骨架；细粒度内容惰性加载 references/ 下的 sequence-templates.md、email-types.md、copy-guidelines.md。
- 落地对接经 tools/REGISTRY.md 路由到具体邮件平台指南（Mailchimp、Nitrosend、Resend 支持 MCP 接入；Customer.io、SendGrid、Kit 仅提供集成文档）；除此之外无外部库或模型 API 依赖。
