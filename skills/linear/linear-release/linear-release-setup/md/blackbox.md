# linear-release-setup (`linear/linear-release/linear-release-setup`)

## blackbox

**function**: 帮你在 CI (自动构建发布的工具) 里接入 Linear 发布追踪: 你告诉我你的项目怎么发布, 我给你能直接粘贴使用的 CI 配置文件和设置说明。

- input: "我们用 GitHub Actions, 每次合并到 main 就自动发布网页版", output: 一份可直接放进 .github/workflows/ 的 yml 文件, 附带要在仓库设置里添加密钥 (access key) 的位置说明
- input: 一个已有的 .gitlab-ci.yml 文件, output: 在原文件基础上补好 linear-release 任务的新配置, 并标出需要调整的地方 (如克隆深度设置)
- input: "iOS 上 TestFlight、网页版直接上线, 两条线分开追踪, 用 CircleCI", output: 两份相互独立的 CI 配置片段, 每条发布线一份, 各配一个对应的密钥
