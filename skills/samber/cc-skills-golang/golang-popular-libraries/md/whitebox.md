# golang-popular-libraries (`samber/cc-skills-golang/golang-popular-libraries`)

## whitebox

- 理解需求：明确使用场景、性能要求和约束条件
- 标准库优先：先查 references/stdlib.md，判断标准库是否已覆盖需求
- 目录筛选：按 web/database/testing/logging/messaging 等类目，从 references/libraries.md 的已审核清单中取候选
- 尽调验证：逐个候选查 pkg.go.dev 的维护状态、license、imported-by 数量和已知漏洞（通过 godig）
- 输出推荐：给出最简单且生产可用的选项；若标准库已够用，直接告诉开发者不用引库

- 知识底座是三份静态参考目录（stdlib.md / libraries.md / tools.md），按类目给出已审核候选，兜底指向 awesome-go
- 成熟度量化：以 pkg.go.dev 的 importer 数、license、漏洞记录为证据，经 godig（golang-pkg-go-dev skill）查询；gopls 读依赖解析后的真实源码做横向对比；Context7 仅作文档兜底
- 决策过滤器：标准库优先 + 简单优先 + 依赖足迹最小化；废弃库不直接推荐（先询问开发者），包装 stdlib 却无增值的库会被拦截
