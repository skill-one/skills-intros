# developing-genkit-go (`firebase/agent-skills/developing-genkit-go`)

## whitebox

- 判断任务是否命中技能范围: 用 Go + Genkit 构建 AI 功能/Agent/流程/工具
- 按 'Core Features' 表按需加载对应 reference 文档 (如 generation.md, tools.md, providers.md)
- 编写代码: genkit.Init 创建 *Genkit 实例, 用 DefineFlow 包裹 AI 逻辑, 通过插件调用模型
- 用 Genkit CLI 验证: `genkit start -- go run .` 起 Developer UI 测试, 或 `genkit flow:run` 直接跑流程

- 中央注册模式: genkit.Init 返回 *Genkit 实例并显式传给所有函数; 由插件 (googlegenai 等) 对接模型 API, 支持 Google AI / Vertex AI / Anthropic / OpenAI 兼容 / Ollama
- 结构化输出与工具调用由标签和描述驱动: 输出类型写 jsonschema:"description=..." 标签教模型填字段; 模型依据工具的 description 字符串决定是否调用
- 提示词与代码分离: 复杂提示写 .prompt 文件 (Handlebars 模板), 改提示无需重编译; 横切需求优先用内置中间件 (Retry/Fallback 等) 通过 ai.WithUse 组合
