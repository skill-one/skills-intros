# ci-cd-and-automation (`addyosmani/agent-skills/ci-cd-and-automation`)

## whitebox

- 识别任务类型: 新建 CI / 增改自动检查 / 配置部署管线 / 排查 CI 失败
- 按『左移』原则排序质量门禁: lint → 类型检查 → 单测 → build → 集成测试 → E2E → 安全审计 → 包体积
- 生成 .github/workflows/ci.yml 等 GitHub Actions 配置, 触发条件设为 PR 和 push 到 main
- 配置分支保护 (门禁必须通过 + 至少 1 人审批才可合并), 密钥只存 GitHub Secrets
- 按 Verification 清单验收: 门禁齐全、管线 <10 分钟、部署有回滚机制

- 顺序门禁 + 零跳过: 检查按成本从低到高排列 (静态分析最先), 任何一步失败整条管线即失败; 禁止通过禁用规则、跳过测试的方式让管线变绿
- 依赖 GitHub Actions 生态: actions/checkout + actions/setup-node (npm 缓存), PostgreSQL service 容器跑集成测试, Playwright/Cypress 跑 E2E, npm audit 做安全审计; 管线超 10 分钟时用缓存、并行作业、路径过滤优化
- 失败反馈闭环 + 可回滚部署: CI 失败输出直接喂回 agent 本地修复 (如 lint --fix) 后重推重跑; 部署走 staging 验证 → 生产 → 15 分钟监控窗口, 出错即触发回滚
