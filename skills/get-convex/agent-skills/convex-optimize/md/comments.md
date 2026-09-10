# convex-optimize (`get-convex/agent-skills/convex-optimize`)

## comments

- user: 独立开发者, category: 妙用, comment: 改完后它会重跑评估并展示前后分数差, 我拿这组前后截图给合作方证明整改到位, 省去自己写审计总结.
- user: 第一次接手外包项目的前端, category: 坑, comment: 以为和 lint 一样会自动改完, 我放着去开会, 回来发现卡在等确认, 一个文件没动. 必须看着计划逐项点头它才动手.
- user: 刚转后端的新手, category: 注意, comment: 只对 Convex 项目生效, 项目里得有 convex/ 目录和 schema. 我拿普通 Next.js 项目去跑, 第一步检测应用就过不去.
- user: 后端老兵, category: 妙用, comment: 妙在它把过期组件检查并进同一份审计报告, 按优先级一次给全, 不用我再手动逐个比对 @convex-dev 各包版本.
- user: 创业公司 CTO, category: 启发, comment: 报告把安全和数据丢失风险排在代码风格前面, 反衬出我们 review 老在纠结写法, 高危项却一直没排期, 该改流程了.
- user: 运维老哥, category: 注意, comment: 它扫完会主动问要不要装 sentinel 补生产报错捕获, 别跳过, 我们线上挂了半天才发现, 就是因为当初没接报错监控.
