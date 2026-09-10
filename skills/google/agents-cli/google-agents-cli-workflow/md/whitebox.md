# google-agents-cli-workflow (`google/agents-cli/google-agents-cli-workflow`)

## whitebox

- Phase 0 理解需求: 先读 .agents-cli-spec.md (无则与用户一次一问澄清), 设计定稿后写入 spec 文件并获用户批准
- Phase 1 查配方目录: 到 /google-agents-cli-adk-code 的 references/samples.md 索引, 把需求能力 (检索/沙箱/记忆等) 匹配到现成 recipe 并克隆研读
- Phase 2 脚手架: 先 agents-cli info 检查是否已有项目, 没有则 agents-cli scaffold create (已有代码则 scaffold enhance)
- Phase 3 构建 + 冒烟: 写 agent 代码, 每次改动用 agents-cli run "prompt" 快速验证行为
- Phase 4 评估迭代: agents-cli eval run (生成+打分), 从核心用例开始与用户对齐分数标准, 通过后才进入 deploy (需显式人工批准)

- 阶段化技能路由: 每个 Phase 开工前强制重读对应 skill (scaffold/eval/deploy/publish/observability 由 uvx google-agents-cli setup 安装), 防上下文压缩丢失关键内容
- CLI 工具链底座: 一切经由 agents-cli (~=1.5.0, 用 uv tool install 安装), 它内部封装 adk/pytest/ruff/uvicorn; 命令报错时读 --help 输出末尾 Source 行定位源码诊断; 选新模型用 google-genai SDK (vertexai=True) 列举可用 Gemini 列表, Python 命令一律 uv run
- 双层校验: pytest 只测代码正确性 (导入/类型/API 契约), 绝不用它断言 LLM 输出; agent 行为质量交给 agents-cli eval 的 LLM-as-judge 评分, 预期迭代 5-10+ 轮
