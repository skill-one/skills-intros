# golang-security (`samber/cc-skills-golang/golang-security`)

## whitebox

- 判定模式 (PR 审查 / 全库审计 / 写码修漏), 用三问建立威胁模型: 信任边界在哪、攻击者可控哪些输入、失守的爆炸半径多大
- 按五大漏洞域逐一分析: 注入、加密与密钥、Web 安全、认证授权、并发与依赖 (审计模式派最多 5 个并行子代理, 各管一域)
- 报告前先溯源: 追踪数据从入口到敏感操作的完整流向, 检查上游是否已有校验——据实调低严重级别而非漏报, 降级结论留内联注释备查
- 按分类参考文档实施修复, 防御映射到标准库方案 (参数化查询、html/template、os.Root、Argon2id 等); 审计模式下每个修复放独立 worktree, 一个修复 = 一个可独立回滚的 PR
- 工具验证: gosec 静态扫描 + govulncheck 查依赖已知 CVE + go test -race 测竞态 + fuzz 测试

- 威胁建模: 对每条跨信任边界的数据流套 STRIDE 六类威胁 (仿冒/篡改/抵赖/信息泄露/拒绝服务/提权), 再用 DREAD 打分 (1-10) 映射到 Critical→Low 四级, 决定修复优先级
- 防御映射而非自造: 内置速查表 + 十余份分类参考 + 代码审查清单, 每类漏洞绑定标准库正解 (database/sql 占位符、crypto/subtle 恒时比较、crypto/rand、AES-GCM), 明确反模式清单拦截 math/rand 做令牌、== 比密钥、自造加密等常见错
- 外部工具链 (无模型 API 依赖): gosec 做 SAST 静态安全扫描, govulncheck 扫依赖已知 CVE (必装依赖, go install 安装), go test -race / -fuzz 做动态验证; golangci-lint 安全相关 linter (bodyclose、errcheck 等) 辅助
