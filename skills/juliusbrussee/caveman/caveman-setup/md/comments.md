# caveman-setup (`juliusbrussee/caveman/caveman-setup`)

## comments

- user: 第一次接网关的新手, category: 坑, comment: slug 写成大写 SupportBot,验证直接 404。改全小写 support-bot 一次就通,命名规则真的会卡人。
- user: 全栈独立开发者, category: 注意, comment: 开工前把 GATEWAY、CAVE_API_KEY、PROVIDER_KEYS 模式、DASHBOARD 四个值备齐,缺一个它就停下来问你,绝不瞎猜 URL。
- user: 后端老兵, category: 妙用, comment: 我按业务拆 slug:客服机器人 support-bot、报表任务 digest-job 分开命名,后台按应用分组,哪条业务烧钱一眼见。
- user: 管密钥的运维老哥, category: 妙用, comment: stored 模式下供应商密钥加密存网关侧,我全程没碰 key 本体,.env 只多 CAVE 两个变量,密钥盘点省一大截。
- user: 内部工具维护者, category: 坑, comment: 对只有 coding agent、不直接调 LLM 的仓库跑,它如实回「无可接入调用点」并停手,不硬造集成——那类仓库要用 caveman wrap。
- user: 带团队的架构师, category: 启发, comment: 报告只准写实测状态码和 token 数,没验证必须报「未验证」,不许装成功。这条纪律我直接抄进了团队的上线路径。
