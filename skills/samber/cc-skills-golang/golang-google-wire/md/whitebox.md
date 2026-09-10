# golang-google-wire (`samber/cc-skills-golang/golang-google-wire`)

## whitebox

- 读代码: 扫描项目 .go 文件, 定位带 //go:build wireinject 标签的注入器文件及其中的 wire.Build(...) 声明
- 解析依赖图: 以各 provider 函数的返回类型为节点, 按参数类型拼接出完整构造链, 接口到实现的对应关系由 wire.Bind 显式声明
- 校验: 每个类型必须有且仅有一个 provider, 缺失或重复立即报错——问题在编译期暴露, 不留到运行时
- 生成代码: 运行 wire ./..., 把注入器函数体替换成一串普通 Go 构造调用, 写入 wire_gen.go 并提交进仓库
- 收尾验证: 用 wire check ./... 或 go build 确认图完整; 构造函数签名每次变更后重新生成

- 核心是代码生成而非运行时注入: wire 在编译期解析依赖图, 产出的 wire_gen.go 只是一串普通构造函数调用——无反射、无运行时容器, 错误在跑 wire ./... 时出现, 而非服务首次请求时 (注: google/wire 已于 2025 年 8 月归档, 功能完备, 仅接受 bug 修复)
- 图一致性靠 Go 类型系统强制: 隐式接口满足被禁止 (必须显式 wire.Bind), 同类型双 provider 被禁止 (用命名类型如 PrimaryDSN/ReplicaDSN 区分); cleanup 函数按 (T, func(), error) 形式声明, 生成的代码负责逆序执行并在中途失败时只运行已建部分的清理
- 桩与生成物靠 build tag 隔离: //go:build wireinject 使注入器桩不参与编译, 只有 wire_gen.go 进二进制, 杜绝重复定义; 外部依赖: Go 工具链 + wire CLI (go install github.com/google/wire/cmd/wire@latest), 辅以 golangci-lint 做静态检查、gopls 做代码导航
