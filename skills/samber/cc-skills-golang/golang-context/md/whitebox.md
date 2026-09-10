# golang-context (`samber/cc-skills-golang/golang-context`)

## whitebox

- 触发匹配：任务落在 **/*.go 路径，且涉及 context 传播设计、泄漏/未超时排查、Background/TODO/WithoutCancel 选型或 context 存值等场景才激活（仅把 ctx 当首参传递的普通代码不在范围内）
- 加载规则：读取本 SKILL.md 的 10 条最佳实践与构造函数选型表，按主题追加读 references/ 深度文档（cancellation / values-tracing / http-services）
- 定位代码：用 Glob/Grep/Read 找到调用链中破坏传播或漏 cancel 的具体位置
- 改写代码：用 Edit/Write 按规则修补——同一 ctx 贯穿调用链、ctx 首参命名、nil 换 TODO、WithCancel/WithTimeout 补 cancel()、Background 只留在 main/init/test 入口、后台任务用 WithoutCancel
- 验证：用 Bash(go:*) 编译检查，跑 golangci-lint（govet/staticcheck）捕获上下文陷阱，或经 Agent 拆分子任务

- 规则即文档、按需展开：核心原则是『同一 context 贯穿整条调用链』，配一张『什么场景用哪个构造函数』的决策表；深层细节（取消传播与 AfterFunc、未导出键类型防冲突、HTTP/DB 场景模式）拆在 3 个 references 文档里，命中对应主题才读取，避免一次性灌入
- 工具链验证闭环：依赖 go 工具链（元数据声明 requires bins: go），并可用 Read/Edit/Write/Glob/Grep/Bash(go:*)/Bash(golangci-lint:*)/Agent；机械可查的坑（未调用的 cancel()、nil context 等）交给 golangci-lint 的 govet/staticcheck 自动兜底
- 优先级与联动：定位为社区默认规则，被公司显式声明覆盖的同名规则优先；通过交叉引用挂接 golang-concurrency / golang-database / golang-observability / golang-lint 兄弟技能，主题越界时移交
