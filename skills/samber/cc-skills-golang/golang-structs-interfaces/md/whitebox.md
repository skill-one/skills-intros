# golang-structs-interfaces (`samber/cc-skills-golang/golang-structs-interfaces`)

## whitebox

- 匹配触发: 任务落在 **/*.go, 涉及 struct/interface 设计 (定义接口、嵌入、类型断言、field tag、receiver 选择等)
- 以 "Go 类型系统设计师" persona 载入, 把 skill.md 的设计原则当作审查清单而非自由发挥
- 用 Read/Grep/Glob 读取用户现有 Go 代码, 或按需求从零设计类型
- 逐条套用规则修正: 小接口 (1-3 方法)、接口定义在消费方、comma-ok 断言、编译期接口检查、receiver 一致性、序列化字段必带 tag, 对照"常见错误表"排查
- 用 Edit/Write 落盘修改, 运行 go vet 等验证; 深入主题 (断言细节、struct tag 全表) 时按需加载 references/ 参考文档

- 规则驱动: 核心是一份 "设计原则 + 标准库接口签名表 + 常见错误对照表" 的检查清单, 模型按清单审查/生成代码, 无自定义脚本
- 渐进式披露: skill.md 只含主干; 细节存于 references/ (type-assertions.md, struct-fields.md), 并交叉引用兄弟 skill (golang-naming、golang-design-patterns、golang-dependency-injection 等) 按需加载
- 外部工具校验: 依赖 go 工具链 (requires bins: go), 用 go vet ./... (如 copylocks 检测 noCopy 违例) 及可选 golangci-lint 验证; 文件操作走 Read/Edit/Write/Grep/Glob
