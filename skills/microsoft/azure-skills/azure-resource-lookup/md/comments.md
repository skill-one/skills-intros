# azure-resource-lookup (`microsoft/azure-skills/azure-resource-lookup`)

## comments

- user: 运维老哥, category: 妙用, comment: 每季度大扫除,我都让它扫全部订阅的孤儿资源:没挂的磁盘、闲置IP、删VM留下的网卡。上次清出40多个没人认领的,一次查完不用挨个点门户。
- user: 第一次用的新手, category: 坑, comment: 上来就说"帮我把测试环境删了",结果它只读不改,白等半天。这工具是查资源的,要动资源得换部署类的工具,开口前先分清。
- user: 接手祖传项目的后端, category: 启发, comment: 接手零文档的老项目,第一句就问"我订阅里都有啥",全量清单一次到手。现在动任何架构前先查一遍,知道影响面再改,踏实多了。
- user: 云上成本负责人, category: 注意, comment: 刚建完的VM立刻查居然没有——它有几分钟延迟,不是实时的。我一度以为权限坏了折腾半天。查新建或刚改的东西,等几分钟再查。
- user: 多订阅企业的IT管理员, category: 坑, comment: 它只查我有权限的订阅,我以为出了全公司清单,结果漏了没权限的那几个,差点漏报。后来统一加了Reader只读角色再查,数据才齐。
- user: 小团队兼管网站的, category: 妙用, comment: 官网后台全是App Service,一直没工具能列出所有网站,这个一句话列全,还能按资源组筛。资源多时让它限量或限定范围,不然几千条刷屏。
