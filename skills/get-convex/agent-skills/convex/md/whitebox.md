# convex (`get-convex/agent-skills/convex`)

## whitebox

- 按任务类型分类请求：新建应用 / 给现有 Convex 应用加能力 / 在 convex/ 下写改代码 / 审查加固 / 运维线上应用
- 路由到对应的打包子技能：quickstart / add / expert / reviewer·authz·verify / monitor·migrate·cost 等
- 若是「加能力」：拉取在线能力目录 capabilities.json，匹配到具体 capability，再按其在线文档 /capability/<id>.md 执行
- 在线目录不可达时回退到打包技能自带的流程，不硬性失败
- 执行中叠加护栏：在线流程优先于打包版本；花钱类操作（tier>0，如买域名）必须先获用户明确确认

- 静态路由表而非猜测：「How to route」固定规则把任务类型映射到约 30 个打包的 convex-* 技能；每个子技能是独立操作手册（scaffolding、审查清单、演练流程等），本技能只做分发
- 在线目录保鲜机制：运行时从 https://basic-anteater-667.convex.site/capabilities.json?src=agent-skills 拉取最新能力清单，命中后按 /capability/<id>.md 的文档执行——在线文本视为「流程指令」而非可盲执行的 shell；项目缺指引或指引过期时建议先跑 `npx convex ai-files install` 装最新官方 guideline（docs.convex.dev/ai）
- 下游校验依赖：写码路径交给 convex-expert（含 tsc --noEmit 提前抓类型错误）、审查走 convex-reviewer / convex-authz、验证走 convex-verify（种子数据 + 多用户驱动 + 反向授权断言）；部署影响类命令前由 convex-deploy-guard 先分类并宣告目标环境
