# golang-context (`samber/cc-skills-golang/golang-context`)

## blackbox

**function**: 帮你找出并修好 Go 代码里 context 用错的地方——让取消信号、超时和请求数据能沿着调用链正确传递, 不再出现"请求都结束了、后台还在空转"或"超时了但查询停不下来"这类问题。

- input: 一个 Go 源文件路径 (例如 order_service.go, 里面某处 new 了自己的 context), output: 逐条指出问题所在行 + 改好的代码 (如改为透传上层传入的 ctx), 直接可替换使用
- input: 一段代码或一个问题: "HTTP handler 里开的审计日志 goroutine, 请求一结束就被取消, 怎么办?", output: 明确结论和对应的修改代码 (改用 context.WithoutCancel 让后台任务活过请求的生命周期)
- input: 一个选择类问题: "这个函数该用 context.Background() 还是 TODO()? 这个 struct 里存 ctx 行不行?", output: 一句话给结论 + 原因 + 建议的替代写法代码片段
