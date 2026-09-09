# appinsights-instrumentation (`microsoft/azure-skills/appinsights-instrumentation`)

## comments

- user: 第一次用的新手, category: 注意, comment: 我张口就说"帮我加监控",结果被它转去 azure-prepare 了。后来才懂:要改代码装 SDK 的找 azure-prepare;想学怎么埋点、看示例和概念的才用这个。先想清楚你要哪种。
- user: .NET 后端老兵, category: 妙用, comment: ASP.NET Core 应用托在 Azure App Service,本以为要改一堆代码,结果它直接带我走自动埋点(AUTO 指南),代码一行没动。同组合的先问能不能自动,别急着动手。
- user: 云运维老哥, category: 妙用, comment: 工作区里已有 Bicep 模板,它让我把 examples 里的 appinsights.bicep 片段直接合进去,而不是另跑 CLI 脚本,资源定义跟着模板走,换环境重部署不会漏建。
- user: 刚上云的前端转全栈, category: 坑, comment: 我没说应用部署在哪,它就一直追问不肯往下走。后来发现本机跑、App Service、Container Apps 给的方案完全不同,容器还有单独指南。开口先讲清语言和托管位置,一步到位。
- user: Python 后端开发, category: 注意, comment: 前置条件只写了 ASP.NET Core 和 Node.js,我以为 Python 没戏,结果它有专门的 python 埋点指南和 OpenTelemetry Distro 参考。别被前置条件吓退,先问一句再下结论。
- user: 管账单的 SRE, category: 坑, comment: 我把 App Insights 资源随手建进了默认资源组,删环境时漏删它,账单上挂了个孤儿资源一个月才发现。听劝:跟应用建在同一个资源组,回收时一起带走。
