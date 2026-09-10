# self-hosted-funnel-launch (`autonnel/autonnel-skills/self-hosted-funnel-launch`)

## whitebox

- 选运行方式: 默认 Cloudflare Workers (静态资源免费不限量), 本地快速评估用 Docker, 改产品本身才用源码 checkout
- 部署并初始化: wrangler 建 KV namespace + Hyperdrive (连接自己的 Postgres)、写入 secrets 后 deploy:cf (或 docker compose up), 应用 schema 后走 /setup 向导建管理员账号
- 按固定顺序在 admin UI Settings 里配置: catalog (商店) → payments → storage → email → 广告平台, 顺序错了会返工
- 先建 checkout 再建 landing; 创建 funnel 并按角色 (LANDING/CHECKOUT/UPSELL/THANKYOU/ERROR) 挂页面; publish 是显式操作, 页面和 funnel 各自独立版本
- 上量前验证: 走一遍真实端到端购买 (含接受/拒绝 upsell、退款、服务端转化回传), 之后即可通过 /api/mcp 让 agent 持续构建和修改

- 静态/动态分流计费 (Cloudflare 路径): funnel 流量绝大多数是对页面/图片/脚本的静态资源请求, 在 Workers 上免费不限量; 只有 Worker 调用 (订单表单、upsell 接受、postback 队列) 计入 10 万次/天额度; 真正先撞的天花板是 KV 写入 1,000/天 (每次发布失效并刷新缓存, 烧的是写额度不是请求额度); Postgres 经 Hyperdrive 池化, 需自备数据库 (唯一非免费项)
- 草稿/发布双版本 + draftData 不做结构校验: 所有写入落在 draftData, publish:true 才提升并失效渲染缓存, 所以流程是写 → get_page 验证 → 二次调用发布; draftData 不校验 root/content/zones/组件名, 组件类型必须从 get_template({key}) 实时拉取 (记旧名单会存成功但渲染空白); 内容必须匹配 editorType (create_page 默认 PUCK 且事后不可改, PUCK 用 draftData、HTML/GRAPESJS 用 htmlContent, 写错列直接被拒)
- MCP 工具面与错误形态: 实例把 admin API 暴露为 /api/mcp 的 MCP 工具 (Streamable HTTP + SSE 帧), 必须带 Accept: application/json, text/event-stream 否则 406; 大多数失败 (缺 writeAccess、校验失败、冲突等) 返回 HTTP 200 + result.isError=true, 只有未知工具名/传输层/auth 是不同形态; funnel step 仅 {stepSlug, pageId} 两字段且 schema 为 .strict() (多传字段即拒); API 层无 delete_page, 页面一经创建只能进 admin UI 删, 所以 slug 要一次起对
