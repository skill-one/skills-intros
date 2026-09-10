# golang-uber-fx (`samber/cc-skills-golang/golang-uber-fx`)

## blackbox

**function**: 帮你的 Go 长期运行服务 (如 HTTP 服务、后台任务) 用 uber-go/fx 框架搭好组件装配、启动/优雅退出逻辑，或修复、重构已有的 fx 代码。

- input: 你有一个能跑但 main() 里到处是手动 new、手工 defer 关闭的 Go 项目路径, output: 改写后的代码：组件改由 fx 统一装配，启动、优雅退出按依赖顺序自动处理，main() 只剩几行
- input: 一段报错或现象，如「服务启动时数据库还没连上」「Ctrl+C 后请求被硬切断」「fx 报 missing type for *sql.DB」, output: 定位到的问题代码 + 修好的代码片段，并说明改了哪里、为什么
- input: 一句需求描述，如「写一个带数据库和健康检查接口的 HTTP 服务骨架」, output: 可直接 go run 的完整 fx 项目代码，含模块划分和配置注入
- input: 一份已有的 fx 代码，问「这样写对吗」, output: 逐条指出隐患（如 OnStart 里做阻塞操作、误用 Provide/Supply）并给出修改后的版本
