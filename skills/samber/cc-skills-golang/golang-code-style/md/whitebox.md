# golang-code-style (`samber/cc-skills-golang/golang-code-style`)

## whitebox

- 触发匹配: 任务涉及 .go 文件的编写/风格审查时, skill 正文被注入上下文, 成为评判代码的规则来源
- 读取代码: 用 Read/Glob/Grep 定位并读取目标 Go 文件, 逐条对照风格规则 (语义断行、变量声明、早返回、函数设计等)
- 大型审查时分发: 最多 5 个并行子代理, 各管一个独立风格维度 (控制流/函数设计/变量声明等), 汇总各自发现
- 输出与修改: 报告问题或用 Edit/Write 直接改代码; 若违反某条规则是有意为之, 必须在代码里加注释说明
- 工具复核: 跑 gofmt/gofumpt/gocritic/revive/wsl_v5 等确认机械性问题; 命名/文档/设计模式等范围外议题转交兄弟 skill

- 规则即知识: 无训练无模型调用, 全靠 SKILL.md 中人工判断型规则 (早返回、≤4 参数、语义断行) + references/details.md 深化细节, 由 harness 中的 LLM 按文执行 — 专管 linter 覆盖不了的"清晰度"判断题
- 并行编排: 经 Agent 工具 fan-out 最多 5 个子代理, 各自扫描一个独立风格关注点后合并结果; Claude Code 上用 `ultracode` 显式开启多代理模式
- 外部工具依赖: 要求环境有 `go` 二进制; 机械格式化交给 golangci-lint 生态 (gofmt/gofumpt/goimports/gocritic/revive/wsl_v5), git 可用于核对改动 — 本 skill 只做规则判定, 格式化交给 linter
