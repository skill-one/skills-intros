# developing-genkit-python (`firebase/agent-skills/developing-genkit-python`)

## whitebox

- 识别触发条件: 用户问题涉及 Genkit Python (AI 应用/agents/flows/tools, 或报错、导入、API 问题)
- 按工作流定位参考文档: 新项目查 Setup, 代码模式查 Examples, 遇到任何报错先读 Common Errors
- 生成代码: 固定模式 Genkit 框架 + GoogleAI 插件 + googleai/gemini-flash-latest 模型, 入口用 ai.run_main(main()) 而非 asyncio.run()
- 运行验证: 通过 genkit start 启动并打开 Dev UI (开发调试界面) 检查结果
- 若出错, 第一步永远是回到 Common Errors 排查, 修正后再交付

- 核心依赖链: Genkit Python SDK (AI 应用框架) → GoogleAI 插件 → Google Gemini 模型 API; 需环境变量 GEMINI_API_KEY, 模型 ID 必须带 googleai/ 前缀
- 运行环境约定: Python 3.14+, 依赖用 uv 管理; genkit CLI 通过 npm install -g genkit-cli 安装
- 防幻觉机制: SDK 迭代快, 内部知识不可信 — 所有 imports 和 API 写代码前一律对照 references 参考文档核验
