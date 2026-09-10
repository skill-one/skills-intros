# golang-samber-oops (`samber/cc-skills-golang/golang-samber-oops`)

## whitebox

- 触发条件: 任务涉及 samber/oops 的采用/使用, 或代码库已 import github.com/samber/oops (作用范围 **/*.go)
- 阅读现有 Go 代码, 定位标准 error 创建/返回点 (fmt.Errorf、errors.Wrap 等)
- 按分层规范重写为 oops 构建链: .In()/.Tags()/.Code()/.With() 收集结构化上下文, 终端方法 .Errorf()/.Wrapf()/.Recover() 生成错误
- 套用硬性规则: 变量数据放 .With() 属性而非消息串 (保证低基数), 每个包边界至少 Wrap 一次补充上下文, goroutine 边界必须用 .Recover()
- 用 go / golangci-lint / gopls 校验编译与调用点正确性, 交付

- 流式构建器 (fluent builder): .With/.In/.Tags/.Code/.User/.Tenant 等方法累积结构化属性, Errorf/Wrap/Wrapf/Join/Recover 为终端方法产出错误; Wrap 对 nil err 直接返回 nil, 无需判空
- 错误即结构化数据: OopsError 暴露 Code()/Domain()/Tags()/Context()/Stacktrace(), 自动捕获堆栈, 支持 JSON 序列化、slog 集成、%+v 输出; GetPublic 提供用户安全消息回退; 属性随错误穿透调用栈 (区别于 stdlib 在日志点手动补字段), 供 Datadog/Loki/Sentry 按 APM 分组
- 上下文传播: 中间件用 oops.WithBuilder 把构建器存入 Go context, 深层用 oops.FromContext 取出续建; 查 Go 包事实优先走 godig 技能 (pkg.go.dev), 代码导航用 gopls (LSP), 文档兜底用 Context7
