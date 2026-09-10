# caveman-discover (`juliusbrussee/caveman/caveman-discover`)

## whitebox

- 盘点: 从入口点遍历仓库 (HTTP/RPC handler、cron/队列/worker、CLI 脚本、eval 脚本、各 agent/chain), 找出所有调用 LLM 的 job, 不按 import 关系遍历
- 命名: 每个 workflow 按网关 slug 规则命名 (小写 [a-z0-9_-], 1-96 字符), 命名 job 而非技术; 代码看不出用途的从文件名推导并标记 review
- 提案: 输出标注表 (workflow/job/位置/标注方式), 明确等用户确认后才改代码
- 接线: 在每个调用点用最轻量的机制打标 (SDK 的 workflow 选项 / default_headers 加 x-cave-workflow / caveman wrap --workflow / 纯 HTTP 加 header), 标在调用方而非共享 helper
- 验证+报告: 用仓库现有的测试/脚本/真实调用跑通一条已标注路径, 确认网关不报 400, 输出报告 (已标注清单、看板落地位置、未接线清单、review 清单)

- 入口驱动盘点 + 调用方打标: 一个 workflow = 一个人能说清的 job——同一 handler 里 10 个调用点算 1 个, 共享 llm.ts 被 3 个 job 用算 3 个; 标签只打在调用方, 共享 helper 永不打标
- 标签随网关流量传播: 依赖 Caveman Cloud 网关——caveman_cloud SDK 用 per-trace workflow / defaultWorkflow 选项; 裸 provider SDK (OpenAI/Anthropic/LangChain/LiteLLM/Vercel) 往已带 x-cave-api-key 的同一 default_headers 块里加 x-cave-workflow; caveman wrap 的产物用 --workflow 参数或 CAVE_WORKFLOW 环境变量; 不经网关的调用点不打标, 列入 not wired
- 两道防护 + 校验回路: 改码前强制人工审批 (遥测/评审类观察不构成编辑授权, 需独立盘点); 幂等——重复运行已标注仓库零改动; 合法性靠网关校验——非法 slug 被拒并返回 400 cave_invalid_request_header, 据此修 slug
