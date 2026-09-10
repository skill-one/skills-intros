# golang-graphql (`samber/cc-skills-golang/golang-graphql`)

## whitebox

- 命中判定: 任务涉及 Go 项目的 GraphQL 服务——设计 schema、写 resolver、订阅, 或代码 import 了 gqlgen / graphql-go。
- 选模式: 新建代码走 Build, 审查代码库或 PR 走 Review; Build 模式先派后台 agent 扫出项目里已有的 resolver 写法与命名惯例。
- 选库: 需要 Apollo Federation、大 schema (100+ 类型)、零反射开销选 gqlgen (代码生成); 小中型 schema、想免构建步骤选 graph-gophers (反射)。
- 写 SDL schema (.graphql) 并按规则设计: 能保证必有值的字段才标 `!`、列表用游标分页 (Connection/PageInfo)、mutation 结果包 Payload 信封; 再写薄 resolver, 只做转换, 业务委托给 service 层。
- 接上安全件后验证: 每请求 DataLoader 中间件、鉴权中间件 + 指令鉴权、ErrorPresenter、复杂度上限; 改 schema 后重跑 go generate, 用 gopls / golangci-lint 收尾。

- Schema-first + 绑定: 两库都以 SDL 为源。gqlgen 走代码生成——go generate 产出 models_gen.go (禁止手改, 用 gqlgen.yml 的 autobind 映射, 否则下次生成被覆盖), 编译期类型安全; graphql-go 走 ParseSchema 时反射绑定, 注意 Int 字段须用 int32。
- N+1 防治与性能护栏: 子字段批量加载用 DataLoader, 且必须在 HTTP 中间件里按请求新建——全局实例会跨请求缓存导致脏数据/跨用户泄漏; 生产 handler 必须挂 FixedComplexityLimit (gqlgen) 或 MaxDepth/MaxParallelism (graphql-go), 并按 ENV 门控关闭 introspection。
- 事实来源与外部工具: Go 包的版本/符号/已知漏洞查 pkg.go.dev 用 godig (优先于 Context7), 代码定义/调用点/诊断用 gopls, 文档兜底 Context7; 对外错误经 ErrorPresenter / ResolverError 包一层, 剥离 SQL 等内部细节, 只给安全消息 + extension code。
