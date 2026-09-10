# golang-structs-interfaces (`samber/cc-skills-golang/golang-structs-interfaces`)

## blackbox

**function**: 🧩 审查和修改 Go 语言代码里的 struct (数据结构) 与 interface (接口), 让类型设计更简洁、更易测试, 直接给出改好的代码。

- input: 一段 Go 代码, 里面定义了一个 8 个方法的大接口, output: 拆成几个 1-3 个方法的小接口组合后的代码, 每处改动附一句原因说明
- input: 一个要转成 JSON 或存数据库的 struct 定义, output: 补好 json/db 字段标签、隐藏内部字段的完整 struct 代码
- input: 提问: 「这个结构体的方法该用 *T 还是指针接收者还是值接收者?」, output: 明确的结论 + 按结论改写的代码示例
