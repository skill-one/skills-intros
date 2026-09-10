# google-agents-cli-deploy (`google/agents-cli/google-agents-cli-deploy`)

## blackbox

**function**: 把你写好的 AI agent 项目部署到 Google Cloud 上线, 拿到可直接调用的服务地址, 并搞定选型、密钥配置和自动化发布 🚀

- input: 一个已完成的 agent 项目文件夹 + 一句「帮我部署上线」, output: 部署完成的线上服务地址 (URL), 附一条测试命令, 直接验证 agent 能正常回答
- input: 「我的 agent 该部署到 Agent Runtime、Cloud Run 还是 GKE?」, output: 一份针对你需求的选型对比 (运维负担、自动扩缩容、成本、上手难度) + 明确推荐
- input: 一段部署报错信息, 如 403 Permission denied、部署卡住不动, output: 定位到出错原因 (如缺哪个权限/配置), 附上可直接复制执行的修复命令
