# fastify-best-practices (`mcollina/skills/fastify-best-practices`)

## whitebox

- 识别任务是否属于 Fastify 范畴 (构建/配置/调试 Fastify 应用: 路由、插件、校验、认证、部署等)
- 按 skill.md 的 Recommended Reading Order, 将场景映射为需读取的规则文件顺序 (如认证 → plugins → hooks → authentication)
- 读取 rules/ 下对应规则文件, 取得详细说明与代码示例
- 依据 Core Principles (封装、schema 优先、async/await、最少依赖) 结合规则文件生成代码
- 输出可直接运行的 Fastify 代码 (参照 Quick Start 模式: 实例 + logger + async handler + listen)

- 场景→规则路由: skill.md 内置查找表, 将常见场景 (入门/认证/性能/测试/生产) 映射为规则文件阅读顺序, 按需加载而非全量读取
- 知识来源为 rules/ 下 18 个 markdown 规则文件 (含解释+代码示例), 所有输出可回溯到这些文件, 不引入额外知识
- 代码生成锚定 Quick Start 模板与五条 Core Principles; 技术栈依赖: Fastify、Node.js、TypeScript (strip types)、Pino 日志、JSON Schema
