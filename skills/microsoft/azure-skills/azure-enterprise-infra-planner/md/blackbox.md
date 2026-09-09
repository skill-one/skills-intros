# azure-enterprise-infra-planner (`microsoft/azure-skills/azure-enterprise-infra-planner`)

## blackbox

**function**: 你用一段话描述业务需求, 我直接产出可在 Azure (微软云) 上真实创建出来的整套基础设施: 先给你方案确认, 再给你能落地的部署代码, 最后帮你部署到云端。

- input: 一段需求描述, 如: 「我要在 Azure 上跑一个对外网站加后台数据库, 要求高可用、数据不能泄露」, output: 一份基础设施方案: 要建哪些网络、防火墙、数据库等资源, 用什么规格, 存在哪些安全与成本取舍, 标注清楚等你确认
- input: 你回复「批准」这份方案, output: 一套可直接使用的部署代码 (infra 目录下的 main.bicep 或 main.tf 文件), 已通过语法校验和安全检查, 拿到任何环境都能跑
- input: 一个已有资源的 Azure 订阅 + 新需求, 如: 「在我现有网络里加一套测试环境, 别动线上系统」, output: 只做增量添加的部署: 新资源接进你现有的网络, 线上已有的东西一律不碰, 部署前先给你看改动预览
