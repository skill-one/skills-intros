# golang-error-handling (`samber/cc-skills-golang/golang-error-handling`)

## whitebox

- 触发: 任务涉及 Go 错误处理 (创建/包装/检查/记录错误) 且路径匹配 **/*.go
- 判定模式: 写新代码→Coding, 审 PR diff→Review, 查整个代码库→Audit
- Coding 主流程: 按技能内 15 条最佳实践顺序执行 (必须检查返回错误、%w 包装、errors.Is/As、单一处理规则、slog 等), 用 Read/Edit/Write 改代码
- 可选并行: 后台启动一个子代理, grep 相邻代码的违规点 (吞错误、log+return 成对) 不阻塞主流程
- 产出代码修改, 可用 Bash(go:*) 或 golangci-lint 验证

- 规则清单驱动: 15 条硬规则作检查表 — 错误要么处理要么返回 (log/return 二选一)、小写错误串、fmt.Errorf("{context}: %w", err) 保留错误链、errors.Is/As (Go 1.26+ AsType)、errors.Join 合并独立错误、sentinel error vs 自定义类型的选择表
- 三模式编排: Audit 模式最多拆 5 个并行子代理 (创建/包装/单一处理/panic-recover/结构化日志) 后汇总; Claude Code 上需 ultracode 显式开启多代理; Coding 用后台子代理不阻塞
- 外部依赖: 需 go 二进制; 运行时调用宿主 harness 的工具 (Read/Edit/Write/Glob/Grep/Bash(git,go,golangci-lint)/Agent); 推荐库为 log/slog + samber/oops 及 samber/slog-* 系列 (slog-http/slog-sentry/slog-multi 等); 无自有模型 API, 推理由宿主 harness (Claude Code/Codex) 的 LLM 完成
