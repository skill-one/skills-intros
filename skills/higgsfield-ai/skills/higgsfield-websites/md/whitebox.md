# higgsfield-websites (`higgsfield-ai/skills/higgsfield-websites`)

## whitebox

- 解析需求: 按 SKILL.md 的 quick tells 把请求映射到 --type (website/app/game); 不明确就先问用户一个问题 (同时问最终是否发布到社区 feed), website 类型还必问 Animated (滚动驱动影片) 还是 Non-animated。
- 读取对应 flow 文档 (references/website-flow.md / app-flow.md / game-flow.md), 严格按该流程走完各自的阶段、编辑地图与部署/发布门禁。
- higgsfield website create --type … --subdomain … 生成 React 19 + TanStack Start SSR 项目到 app/; 用 git + bun 一次性写完每个文件; 需要素材时提交 higgsfield generate / higgsfield model 渲染任务, 页面构建与渲染并行推进。
- 生成品牌封面并填写 app/src/app-meta.json (og_title、og_image_url 等) — 这是构建必经步骤, 缺封面或缺标题视为未完成。
- higgsfield website deploy 直接上线公开站点 (无预览阶段), 从 higgsfield website status 取 URL 回给用户; 只有用户先前明确同意才追加 publish 到社区 feed。

- 路由分发机制: SKILL.md 用 quick tells 判定产品类型 — '无 AI 生成、独立品牌' → website; '要生成图像/视频/音频或用 Higgsfield 模型/credits' → app (永远不提供自带生成 API 的选项); '游戏' → game; 每种 type 路由到独立 reference 文档, 各自携带专属规则与门禁 (如 website 禁用 Quanta、app 必须用 Quanta 和 fnf SDK 登录)。
- 运行时架构: 每个 site 是部署在单个 Cloudflare Worker 上的 React 19 + TanStack Start SSR 应用 (基础设施 D1/R2/KV/DO/Containers); 生命周期全由 Higgsfield CLI 驱动 (create/repo/deploy/publish/status/db/secrets), 本地代码编辑靠 git + bun, 所有 bun/构建命令都在 app/ 目录下执行。
- Turn 经济机制: 面向有回合上限的 agent 运行时 — 每个文件只写一次且写完整 (禁止先写后补、禁止重读刚写的文件), 能并发的渲染任务 (如影片+封面) 同时提交、只在其输出是下一步输入时等待一次; 转译规则: 对用户只说产品语言 ('更新站点中…'), 不暴露 git/分支/部署等内部机制。
