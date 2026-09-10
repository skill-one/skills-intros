# golang-dependency-injection (`samber/cc-skills-golang/golang-dependency-injection`)

## whitebox

- 评估代码库: 现有依赖关系图、生命周期需求 (健康检查/优雅停机)、服务数量
- 查决策表, 按规模和需求推荐手动构造注入或具体 DI 库 (google/wire / uber-go/dig+fx / samber/do)
- 生成装配代码: 构造函数 + main() 组装根处的手动接线, 或容器 Provider 注册代码
- 用 go 编译和 golangci-lint 验证生成代码, 并对照最佳实践清单复查 (禁全局变量/init(), 接口定义在消费方, 依赖图保持浅)

- 决策表路由: 以服务数量 (<10 手动 / 10-20 考虑引库 / 20+ 强烈建议库) 和生命周期需求为输入, 唯一输出一种方案; 内置防过度设计护栏 —— 小项目坚持手动注入, 不引库
- 重构模式的扇出编排: 拆出最多 3 个并行子代理, 分别扫描 ①全局变量与 init() 服务初始化 ②应改为接口的具体类型依赖 ③service-locator 反模式 (容器被到处传参), 结果汇总为一份迁移计划
- 外部工具链: 依赖 go 二进制 (必需); 分析用 Read/Glob/Grep, 写码用 Edit/Write, 编译与静态检查走 Bash(go / golangci-lint); 生成 DI 库代码前经 context7 MCP (resolve-library-id + query-docs) 查询官方文档确认当前 API 签名; google/wire 的 wire_gen.go 由 wire 本身生成, 本技能只负责指导
