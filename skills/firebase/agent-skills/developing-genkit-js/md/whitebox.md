# developing-genkit-js (`firebase/agent-skills/developing-genkit-js`)

## whitebox

- 校验环境: 运行 `genkit --version` 确认 CLI ≥ 1.29.0, 不满足则全局安装/升级 genkit-cli
- 判定上下文: 未指定模型提供方时默认 Google AI; 读 package.json 识别框架 (Next.js / Firebase / Express)
- 查证后编码: 不凭记忆写代码, 先用 `genkit docs:read` / `docs:search` 查权威文档, 再按最佳实践写最小化实现
- 静态验证: 改动后跑 `npx tsc --noEmit` 做类型检查
- 报错走协议: 任何 Genkit 错误先查 common-errors.md, 命中已知模式则套用文档解法, 未命中才查其他文档

- 文档优先机制: 因 Genkit 经历过破坏性 API 变更, 内部知识一律不信任; 所有信息以 genkit CLI 的 docs:read / docs:search / docs:list 命令和内置 references (common-errors.md 等) 为准
- 错误匹配机制: 维护常见错误清单 (ValidationError / 类型错误 / 404 等), 报错时强制先比对清单、套用文档解法, 禁止凭旧版 (pre-1.0) 经验假设着修
- 代码生成栈: 基于 Node.js/TypeScript, 用 genkit 库 + Zod 定义输入输出 schema, 默认接入 @genkit-ai/google-genai 插件 (Gemini 模型), 并按 package.json 检测到的框架插件适配实现模式
