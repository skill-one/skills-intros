# golang-concurrency (`samber/cc-skills-golang/golang-concurrency`)

## whitebox

- 任务进入 (.go 文件), 先判定三种模式之一: Write (实现并发代码) / Review (只看 PR diff) / Audit (全库审计)
- 用 Read/Grep/Glob 读代码与 diff, 需要示例时加载 references/ 下的 channels-and-select、sync-primitives、pipelines 文档
- 套用核心原则与并发清单做设计/修正: 每个 goroutine 有退出路径、select 带 ctx.Done()、发送方关 channel、按场景表选 channel / Mutex / atomic / errgroup
- Audit 模式额外派 5 个并行子代理分别扫一个维度, 汇总成一份报告
- 验证: 跑 go test -race ./..., 需要时加 goleak 检查泄漏、golangci-lint 过一遍

- 规则驱动而非猜: 核心原则清单 + 常见错误表 + 决策表直接给出结论 — 比如热循环里 time.After 换 NewTimer+Reset、channel 只由发送方 close、共享 map 读多写少选 sync.Map, 全部来自 SKILL.md 的固定规则
- 依赖外部工具: go 工具链 (含 -race、pprof 的 goroutineleak 检测)、golangci-lint、go.uber.org/goleak、golang.org/x/sync 的 errgroup 与 singleflight; 允许的工具是 Read/Edit/Write/Glob/Grep/Bash(go|golangci-lint|git)/Agent
- 审计的并行化: 把并发问题拆成 5 个互不重叠的扫描维度 (goroutine 启动无退出机制、未加锁的共享状态、channel 用法、select 缺 ctx 或循环内 time.After、锁与原子操作), 每个一个子代理, 最后合并成单一报告; Claude Code 上用 ultracode 显式开启
