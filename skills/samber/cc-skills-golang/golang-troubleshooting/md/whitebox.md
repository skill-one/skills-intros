# golang-troubleshooting (`samber/cc-skills-golang/golang-troubleshooting`)

## whitebox

- 读全错误信息, 按 Quick Decision Tree 把症状归类 (编译失败/崩溃/挂起/内存增长/慢...)
- 先复现: 写一个确定性的失败测试, 不凭猜测动手修
- 按症状路由到对应 reference 文档 (common-go-bugs / concurrency-debug / pprof 等), 一次只验证一个假设
- 诊断工具逐步升级: fmt.Println → 日志 → pprof → Delve → GODEBUG
- 确认根因后才写修复并验证 (讲不清为什么, 就继续查, 不打补丁)

- 症状→文档路由: 内置决策树把每类症状映射到 references/ 下具体文档 (methodology、common-go-bugs、pprof、production-debug 等), 分流后按 10 步方法论执行
- 测量优先于直觉: pprof (curl localhost:6060/debug/pprof 的 CPU/heap/goroutine/mutex/block profile)、go test -race 竞态检测、GOTRACEBACK/GODEBUG、go build -gcflags="-m" 逃逸分析; 外部依赖: go 二进制 + Delve 调试器 (go install github.com/go-delve/delve/cmd/dlv@latest)
- 双模式编排: 单一问题默认串行调查 (不开子 agent); 用户明确要求全库审计时, 按五类 bug (nil/interface、资源泄漏、错误处理、竞态、context/slice/map) 启动最多 5 个并行子 agent; 根因纪律贯穿两种模式: 向后追数据流、连问 5 个 why、核查上游调用方是否已保证条件
