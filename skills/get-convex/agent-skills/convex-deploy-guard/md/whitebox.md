# convex-deploy-guard (`get-convex/agent-skills/convex-deploy-guard`)

## whitebox

- 作为任何部署相关操作 (ship / env / migrate / seed) 的第 0 步被调用，本身不是部署工具
- 识别：读 .env.local 的 CONVEX_DEPLOYMENT、convex.json、CONVEX_DEPLOY_KEY，或调用官方 Convex MCP 的 status，分类为 local-anonymous | dev | preview | prod
- 宣告：在执行任何部署相关命令前，单独一行输出目标，如 `target: dev (joyful-capybara-123, personal dev)`；识别与行动是两个独立步骤
- 放行门：目标是 prod 时，先说明改哪个部署、改什么，拿到本会话内新的明确 yes 才执行；非 prod 直接执行
- 异常分支也走主流程第 2 步：部署'没生效'时不重试部署，而是重新识别——几乎肯定是打到了另一个部署

- 多源交叉校验：配置文件/环境变量 (.env.local、convex.json、CONVEX_DEPLOY_KEY) 与 MCP status 互相印证，两源不一致必须先解决；无法判定时用 `npx convex env list` 指纹比对——永不猜测。依赖：官方 Convex MCP (status 工具)、Convex CLI (npx convex)，无模型依赖
- 风险分级开关：MCP 的两个 prod 标志严格拆开——`--cautiously-allow-production-pii` 只授予只读审计 (读数据/日志/insights)；`--dangerously-enable-production-deployments` (解锁变更类工具) 默认永远 OFF，仅当用户本会话明确要求改 prod 才开；MCP 启动默认只挂非 prod 选择器 (--deployment dev)
- 会话级状态锁：用户一旦说'只读'，整个会话绝对只读——MCP 以 `--disable-tools run,envSet,envRemove` 启动，连'无害'的变更也拒绝；prod 同意是按动作×目标×会话生效的，之前给过的 yes 不携带
