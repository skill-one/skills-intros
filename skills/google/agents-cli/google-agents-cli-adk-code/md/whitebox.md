# google-agents-cli-adk-code (`google/agents-cli/google-agents-cli-adk-code`)

## whitebox

- 接到“写 ADK 代码 / 定义 agent / 加工具 / 加回调”类任务后, 先激活配套的 workflow 技能, 确认开发阶段与脚手架要求
- 校验项目就绪: 跑 `agents-cli info` 确认有配置; 新项目跑 `agents-cli scaffold create <name>`, 已有代码跑 `agents-cli scaffold enhance .` —— 没有脚手架就不写任何代码
- 读 `references/samples.md` 主题索引, 把需求能力映射到现成的参考配方, 克隆配方并先读其 AGENTS.md 再动手
- 按 cheatsheet (adk-python.md / adk-workflows.md) 写代码; 超出 cheatsheet 的细节, 先 `curl https://adk.dev/llms.txt` 拿文档索引, 再 WebFetch 对应页面, 或直接翻已安装的 ADK 包源码核实精确签名
- 产出 Python ADK 代码: Agent(name, model, instruction, tools=[...]) 的标准结构
- 本技能不负责脚手架与部署, 越界需求转交 google-agents-cli-scaffold / google-agents-cli-deploy

- 配方优先、禁造轮子: samples.md 只给能力→配方名的映射, 命中已有能力(沙箱代码执行、跨会话记忆、审批门、工具护栏、按用户凭据、定时/事件驱动运行)时, 必须克隆配方实现; 手写 Docker/E2B 沙箱包装、skill 加载器、审核回调、memory store 视为未完成
- 三层知识兜底: 本地 cheatsheet → 在线文档索引 (curl adk.dev/llms.txt + WebFetch 具体页) → 已安装 ADK 包源码, 逐层查到 API 的精确签名和符号
- 外部依赖: 二进制 `agents-cli` (经 `uv tool install google-agents-cli` 安装), Python ADK SDK (其他语言暂不支持), Gemini 模型 (示例为 gemini-3.7-flash), 在线文档源 adk.dev
