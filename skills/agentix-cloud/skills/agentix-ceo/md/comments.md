# agentix-ceo (`agentix-cloud/skills/agentix-ceo`)

## comments

- user: 独立开发者, category: 妙用, comment: 睡前切 autopilot 挂机跑活, 白天切回 supervised 把关。规矩提前写进 Custom Policies, 切模式不会丢。
- user: 第一次用的新手, category: 坑, comment: 注册完就急着派任务, worker 起不来——第 4 步得先把 Anthropic key 配到团队。确认链接 15 分钟就过期, 收到马上点。
- user: 自部署运维, category: 注意, comment: 内网自部署不用 key 不用注册, credentials 只写实例地址和 TEAM_ID 就能跑。但接口无鉴权, 千万别映射到公网。
- user: 带团队的技术负责人, category: 坑, comment: 把项目路线图写进 playbook, 切模式时被模板整个覆盖。它只保留 Custom Policies, 目标和活儿都该放任务列表。
- user: 产品经理, category: 注意, comment: supervised 模式它只推进进行中的活, 不主动排新任务, 会一直等你点头。想让它自己干, 得明确说切 autopilot。
- user: 后端老兵, category: 启发, comment: 以前派活爱写"接着上次继续", 但 worker 是一次性的, 干完就退。现在每个任务描述都写成独立可懂, 失败还能 resume 续跑。
