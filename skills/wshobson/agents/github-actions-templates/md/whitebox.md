# github-actions-templates (`wshobson/agents/github-actions-templates`)

## whitebox

- 识别任务: 用户需求是 CI/CD 自动化 (自动测试 / 构建 Docker 镜像 / 部署 K8s / 安全扫描), 命中技能适用范围
- 匹配模式: 从内置模式库中选最接近的一条 — 测试 / 构建推送镜像 / K8s 部署 / 矩阵构建 / 安全扫描 / 可复用 workflow
- 填充模板: 按用户技术栈改写该模式 (语言版本、镜像仓库、密钥名、分支名), 生成 .github/workflows/*.yaml
- 套用最佳实践清单: 逐项检查 — 固定 Action 版本、缓存依赖、最小权限、secrets 存敏感信息、生产部署加审批门
- 交付完整可运行的 workflow YAML

- 本质是模式复用 + 参数替换, 而非从零生成 YAML: 直接基于预写好的生产级模板改写, 保证输出开箱即用
- 编排 GitHub Actions 生态的官方/第三方 Action (actions/checkout、setup-node、docker/build-push-action、codecov-action、trivy-action、slack-github-action 等), 并强制钉住具体版本 (@v4, 不用 @latest) 防止上游变更破坏流水线
- 安全与性能内建在模板里: 敏感值一律走 ${{ secrets.* }} 引用, job 配置最小 permissions, 依赖用 npm cache / GitHub cache 加速; 模板引用的外部设施包括 ghcr.io 镜像仓库、Trivy/Snyk 扫描器、AWS EKS + kubectl、Slack Webhook
