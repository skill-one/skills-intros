# github-actions-templates (`wshobson/agents/github-actions-templates`)

## comments

- user: 第一次配CI的新手, category: 坑, comment: 抄 Docker 模板一直报 403,查了半天是仓库 Settings→Secrets 没配凭证,且 job 要加 packages: write,少一样都推不上去。
- user: 前端开发, category: 坑, comment: 模板用 npm ci,它严格按 lock 文件装依赖。我本地装了新包没提交 lock,CI 直接报不同步失败——记得连 lock 一起提交。
- user: 运维老哥, category: 注意, comment: 模板里 environment 写 production 不等于有审批,要先在 Settings→Environments 建同名环境并加审批人,否则打 tag 就直发线上。
- user: 管预算的技术负责人, category: 注意, comment: matrix 是系统×版本相乘:3 系统×4 Python 就是 12 个并行任务,macOS runner 计费是 Linux 的 10 倍,只测真支持的组合。
- user: 开源库维护者, category: 妙用, comment: 把测试流程抽成 reusable workflow,5 个仓库都来调用,上次 Node 升级只改一处,不用挨个仓库改。
- user: 安全工程师, category: 妙用, comment: Trivy 结果传成 SARIF 后,漏洞直接出现在仓库 Security 标签页,每条带修复版本号,评审时一眼看到新增风险。
