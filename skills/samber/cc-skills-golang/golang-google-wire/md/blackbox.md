# golang-google-wire (`samber/cc-skills-golang/golang-google-wire`)

## blackbox

**function**: 帮你给 Go 项目做"依赖接线":把程序里对象之间的创建与连接关系交给 wire (Google 的编译期依赖注入工具) 管理, 缺依赖、重复依赖在编译前就被发现, 并自动生成接线代码。

- input: 一个 Go 项目, main.go 里手工 new 了一堆数据库、缓存、服务对象, 想改用 wire, output: 改造后的 provider 与 injector 代码 + 生成的 wire_gen.go, `wire ./...` 与 `go build` 均通过
- input: 一段 wire 报错, 如 `multiple providers for *sql.DB` 或 `no provider found for UserStore`, output: 修复好的代码 (如用命名类型区分两个连接、补上 wire.Bind 接口绑定), 重新跑 `wire ./...` 不再报错
- input: 一句话需求: "给应用加一个 Redis 客户端依赖, 关闭时自动释放", output: 新增的 provider (含 cleanup 函数) + 重新生成的 wire_gen.go, 新依赖已接入应用且退出时自动清理
