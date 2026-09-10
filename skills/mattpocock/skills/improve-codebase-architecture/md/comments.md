# improve-codebase-architecture (`mattpocock/skills/improve-codebase-architecture`)

## comments

- user: 创业小厂 CTO, category: 妙用, comment: 开场直接点名最头疼的模块或痛点, 它会跳过全库扫描直奔目标; 不指定方向时它靠 git log 找热点, 提交信息写得乱, 热点就会猜偏。
- user: 第一次用的新手, category: 坑, comment: 我以为看完报告它就动手改, 其实候选只给方向不给设计, 干货在后面一轮轮追问里。跳过追问照抄方案去改, 结果漏了要迁移的旧测试。
- user: 内网开发的前端, category: 注意, comment: 报告的样式和图表走 CDN 加载, 公司内网打开只剩干巴巴的文字甚至空白。看报告前先确认浏览器能出公网, 不然会以为它坏了。
- user: 带 ADR 流程的后端老兵, category: 妙用, comment: 否掉候选时给出硬理由, 它会提议记成 ADR, 我当免费决策存档用。亲测: 没写 docs/adr 之前, 它真把半年前否掉的方案又端上来过一次。
- user: 接手祖传代码的维护者, category: 启发, comment: 它问『删掉这个模块, 复杂度是集中还是只是搬家』, 还说『两个调用方才算真接缝』。这两问我现在 review 都先问一遍, 判断该不该抽层快多了。
- user: 开源项目维护者, category: 注意, comment: 项目没有 CONTEXT.md 它也能跑, 会在追问时现场帮你建一个。但想让报告用你们的业务词而不是满屏 Handler, 开工前先自己写一版领域词表。
