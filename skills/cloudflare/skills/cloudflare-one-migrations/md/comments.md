# cloudflare-one-migrations (`cloudflare/skills/cloudflare-one-migrations`)

## comments

- user: 网络安全工程师（ZIA+ZPA 混合迁移）, category: 坑, comment: 混合迁移时我直接启用 ZIA 迁来的 L4 拦截规则，Access 私有应用流量被 Gateway 先拦死了。要先建那条私有应用放行规则，优先级还必须排在宽拦截之前。
- user: 第一次带迁移项目的新手, category: 坑, comment: 我最初只交规则截图，结果映射出一堆「无法迁移」；补交结构化导出才发现对象引用散在别的文件里，很多规则其实能映射上。
- user: ZPA 重度用户, category: 坑, comment: 我以为 API 建完 Tunnel 就完事，连接器其实没部署：cloudflared 要单独安装认证，副本数还得对上原 connector 实例数，否则拓扑变了。
- user: 安全合规审计员, category: 妙用, comment: 最值钱的是逐条核算表：每条源规则对应迁移/部分/未迁移加原因和安全影响。审计时我直接当交付物，没人再追问漏迁了哪条。
- user: 运维老哥, category: 注意, comment: 大 app segment 建 Access app 会被默认 5 个 hostname 上限卡住。先找 Cloudflare 账户团队申请提到 50 再动手，别学我先拆出一堆策略相同的重复 app。
- user: 老网工, category: 注意, comment: Zscaler 的 CAUTION/warn 在 Gateway 没有等价行为，别默默改成放行或拦截了事；逐条找业务方拍板并记录，我漏记一条被回滚追问过。
