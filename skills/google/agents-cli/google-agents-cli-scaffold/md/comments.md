# google-agents-cli-scaffold (`google/agents-cli/google-agents-cli-scaffold`)

## comments

- user: 第一次用的新手, category: 坑, comment: 我先手动建了空文件夹再跑 create，结果它按 enhance 模式处理，生成的文件不对。删掉空目录重跑才正常——别提前 mkdir。
- user: 运维老哥, category: 坑, comment: 部署 agent_runtime 后会话行为一直怪，排查半天发现是代码里留了 session_type 被 Runtime 覆盖。部署前删掉这行就好。
- user: 独立全栈开发者, category: 妙用, comment: 老项目结构太乱没法 enhance，我在 /tmp 临时 scaffold 一个，把 Dockerfile 和 CI 配置抄过来就用，用完即删，比手写省事。
- user: 照旧教程入坑的后端, category: 注意, comment: 照旧博客敲 --datastore 直接报 UsageError，agentic_rag 模板也移除了。RAG 这类能力现在去官方 recipes 克隆现成代码。
- user: 自动化测试工程师, category: 启发, comment: 我以前用 pytest 断言模型回复，今天过明天挂。改成 agents-cli run 做冒烟、eval run 做验证才明白：LLM 行为该评测，不该单测。
- user: 定团队规范的技术负责人, category: 注意, comment: 我们 agent 代码不在 app/ 目录，第一次 enhance 静默漏了文件。加 --agent-directory 指对路径才补齐，用前先确认代码位置。
