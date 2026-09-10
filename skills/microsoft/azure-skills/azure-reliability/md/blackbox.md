# azure-reliability (`microsoft/azure-skills/azure-reliability`)

## blackbox

**function**: 给你的 Azure 云上应用 (Functions、App Service) 做一次「抗故障体检」, 标出哪里会单点挂掉, 并在你确认后直接帮你修好。

- input: 一个 Azure 资源组或应用名称 (如 rg-myapp), 或一句「帮我查下这个应用可靠性怎么样」, output: 一张红绿灯体检表: 区域冗余、存储副本、健康检查、多地区容灾四项, 每项标明 🟢 已开启 / 🔴 缺失, 以及具体涉及哪些资源
- input: 「把红的那几项修一下」/「让我的应用支持区域冗余」, output: 在你逐项确认后, 直接在线上资源完成的修改 + 修完后的复检对比表 (哪些从红变绿了)
- input: 一个含 Bicep 或 Terraform 文件的项目文件夹 (如 azd 项目), output: 已写入可靠配置的 IaC 文件 (下次部署不会丢), 并替你执行部署直到生效
