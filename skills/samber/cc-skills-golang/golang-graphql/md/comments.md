# golang-graphql (`samber/cc-skills-golang/golang-graphql`)

## comments

- user: 第一次用 gqlgen 的新手, category: 坑, comment: 手改 models_gen.go 加字段, 一跑 go generate 全被覆盖, 白干一下午。要加字段去 gqlgen.yml 配 autobind, 生成文件碰都别碰。
- user: 做技术选型的组长, category: 注意, comment: 名字相近的库容易混: graphql-go/graphql 是 code-first 写法, 冗长且没有 SDL, 直接排除。小 schema 图省构建选 graph-gophers, 大项目上 gqlgen。
- user: 后端老兵, category: 妙用, comment: 把业务报错放进 CreateUserPayload.errors 这类信封字段返回, 客户端能同时拿到部分数据和错误, 不用去解析 GraphQL 顶层 errors 数组, 前端处理干净多了。
- user: 运维老哥, category: 坑, comment: 上线没几天有人发超深嵌套查询把服务打挂。没配复杂度上限等于裸奔, gqlgen 加 FixedComplexityLimit, 生产环境顺手关掉 introspection。
- user: 从 REST 转过来的开发, category: 坑, comment: 列表页每个用户单独查一次 posts, 数据库被 N+1 拖垮。DataLoader 还必须每请求新建, 做成全局的会跨请求串缓存, 甚至漏别的用户数据。
- user: 写实时聊天的小团队主程, category: 启发, comment: 订阅接口客户端断线后 goroutine 不退出, 内存缓慢上涨才发现。现在写任何长连接 handler, 都先想清楚 ctx 取消时谁负责关 channel 和退订。
