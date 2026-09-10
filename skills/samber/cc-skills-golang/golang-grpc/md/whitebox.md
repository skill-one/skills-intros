# golang-grpc (`samber/cc-skills-golang/golang-grpc`)

## whitebox

- 任务进入: 用户在 Go 项目里实现/审查/调试 gRPC (匹配 **/*.go 或 gRPC 相关请求), 技能加载内嵌的 gRPC 最佳实践指南。
- 判定模式: 从零实现 server/client → Build mode; 审计已有代码的正确性/安全性/可运维性 → Review mode。
- 按指南产出代码: 写 .proto → protoc 生成 Go 桩代码 → 实现 server/client (错误码、deadline、拦截器、优雅停机、健康检查)。
- 查证外部事实: 包文档/版本/漏洞走 godig (pkg.go.dev), 定义跳转/调用点/诊断走 gopls (LSP), Context7 兜底。
- 验证收尾: bufconn 内存集成测试校验错误返回与状态码, golangci-lint 静态检查。

- Proto 代码生成依赖外部工具链: protoc (brew install protobuf) + protoc-gen-go / protoc-gen-go-grpc (go install); .proto 按域+版本目录组织 (proto/user/v1/), 强制 Request/Response 包装消息以便向后兼容演进。
- 纯知识驱动, 无独立运行时: 转换与校验靠内嵌规则/反模式清单执行 — 裸 error 必须改 status.Errorf + 具体 code (否则客户端拿到 Unknown 无法决定重试), 每个 client 调用设 context deadline, 横切关注点走 ChainUnaryInterceptor, 生产环境强制 TLS、关闭 reflection、注册 health 服务。
- 事实查询链分层: godig 查 Go 包的文档/符号/版本/已知漏洞 (优先于 Context7), gopls 做 LSP 级代码导航与诊断; 运行时依赖 google.golang.org/grpc 官方库生态 (status/codes、credentials、test/bufconn、go-grpc-middleware)。
