# golang-safety (`samber/cc-skills-golang/golang-safety`)

## whitebox

- 触发匹配: 任务涉及 Go 代码 (*.go), 且属于空值安全 / 数值转换溢出 / 资源生命周期审查, 或设计零值安全的类型; 并发、可利用漏洞、调试已故障程序不在范围
- 读取目标代码, 对照固定陷阱清单逐项扫描: typed-nil 接口、nil map 写入、append 共享底层数组、int64→int32 静默截断、float == 比较、循环内 defer、导出的可变内部状态、零值可用性
- 按 ✓ 修复模式直接修改代码: comma-ok 断言、make 初始化或懒初始化、全切片表达式 s[:len(s):len(s)]、转换前范围检查、epsilon 比较、抽出循环体让 defer 按次执行、返回防御性副本、sync.Once 懒初始化
- 用 go 和 golangci-lint 验证修复, 落实 errcheck / forcetypeassert / nilerr / govet / staticcheck 等静态检查
- 遇范围外问题不硬修, 按交叉引用转介给兄弟技能: 并发 → golang-concurrency, 漏洞 → golang-security, 排障 → golang-troubleshooting

- 清单驱动审查: 内核是 ✗危险 → ✓修复 的固定对照表 (11 条最佳实践 + 常见错误表 + nil/slice/channel 行为矩阵), 无外部模型依赖; 深层细节按需加载 references/nil-safety.md 与 references/slice-map-safety.md
- 机器验证兜底: 依赖 go 工具链 (必需二进制) 与 golangci-lint, 经 Bash 执行; 允许工具面: Read / Edit / Write / Glob / Grep / Bash(go:*) / Bash(golangci-lint:*) / Bash(git:*) / Agent, 作用域限定 **/*.go
- 范围守卫: 定位是防『自己写出的 bug』(panic 与静默数据损坏), 明确不防攻击者、不管并发同步、不做故障调试; 篇幅全用于审查规则与修复模式, 越界即转介
