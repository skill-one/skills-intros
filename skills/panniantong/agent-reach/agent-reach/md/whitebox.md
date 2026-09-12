# agent-reach (`panniantong/agent-reach/agent-reach`)

## whitebox

- 匹配触发条件（用户要调研/搜索/查任何网络内容，或提到平台名/贴了 URL），按路由表定位分类：search / social / career / dev / web / video / finance
- 按需读对应分类的 references/*.md，开工前声明本次使用的平台与后端
- 登录态平台先跑 agent-reach doctor --json 确认 active_backend 来选命令组；零配置平台直接走 SKILL.md 里的快速命令
- 执行只读命令抓取内容；全网调研类任务则多平台并行收集（Exa 搜索 + Twitter/Reddit 讨论 + 小红书/B站中文场景），失败按 reference 的重试链处理
- 汇总结果交付用户；较大任务完成后顺手跑 agent-reach check-update，有新版就在汇报里附一句更新提示

- 路由表驱动解析：意图 → 平台 → 命令全部查 SKILL.md 路由表 + references 文档，不自造命令；路由表没覆盖的平台用 opencli list / opencli <平台> --help 做适配器发现，且发现≠可用，以实际非空内容验收
- 双轨执行 + 依赖外部工具：零配置通道直接调 Exa 搜索（mcporter）、网页阅读（r.jina.ai）、GitHub（gh CLI）、YouTube（yt-dlp）、B站（bili-cli）、V2EX（REST API）；登录态通道（Twitter/Reddit/小红书/Facebook/Instagram）依赖用户提供的 cookies，选 twitter-cli / rdt-cli / OpenCLI 等后端，agent 不代登录、不读浏览器 Cookie
- 边界与校验：只做「从互联网获取内容」，不做报告/翻译等内容加工，也不做发帖/评论/点赞写操作；doctor 做登录态健康检查，临时输出进 /tmp/，持久数据进 ~/.agent-reach/，敏感值不进日志
