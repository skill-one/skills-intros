# golang-uber-fx (`samber/cc-skills-golang/golang-uber-fx`)

## whitebox

- 触发条件: 项目是 Go 且 import 了 go.uber.org/fx, 或任务要求用 fx.New 接线服务
- 读代码: 用 Glob/Grep/Read 扫描 *.go, 定位 main (composition root) 和现有构造函数
- 需要时查证: 包事实优先用 godig (pkg.go.dev 数据), 文档缺了退回 Context7, 代码跳转用 gopls
- 设计并写入: 在 main 用 fx.New + fx.Provide/Invoke/Module/Annotate 组装依赖图, 阻塞工作放进 OnStart hook 的 goroutine 而非 init()
- 验证: go build + golangci-lint 检查; 按 fx.New(...).Err() 提前暴露缺失 provider 和循环依赖

- 依赖注入机制: 底层是 uber-go/dig 的反射容器 — 用 fx.In/fx.Out 结构体 + fx.Annotate (name/group/As 标签) 声明依赖, 值分组 (group:"routes") 聚合; 没有 Invoke 引用到某个类型, 它的构造函数就不会执行 (惰性)
- 生命周期与模块机制: OnStart/OnStop 钩子按依赖图拓扑顺序触发 (OnStop 反序), 默认 15 秒超时, 钩子必须尊重 ctx 取消; fx.Module 把 fx.Decorate 的作用域限定在自己及子模块内, 不会泄漏给兄弟模块
- 外部依赖: 需要本机安装 go 工具链; 文档源按优先级为 godig (pkg.go.dev) → Context7 (后备) → gopls LSP (代码导航); 验证工具为 go build / golangci-lint / git
