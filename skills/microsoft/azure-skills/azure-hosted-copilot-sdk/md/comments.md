# azure-hosted-copilot-sdk (`microsoft/azure-skills/azure-hosted-copilot-sdk`)

## comments

- user: 第一次用的新手, category: 坑, comment: 我没装 Docker 就直接让它部署，跑到一半报错重来。先跑 docker info 确认 Docker 在运行再开始，一次就过了。
- user: 后端老兵, category: 妙用, comment: 需求里只写「部署」，它发现项目已有 .azure/deployment-plan.md 就主动让位给 azure-deploy，不重复走准备流程，没做无用功。
- user: 全栈开发者, category: 坑, comment: 接自己的模型我先用了 API key 鉴权，直接不被支持。BYOM 只认 bearerToken：本地 DefaultAzureCredential，线上换 ManagedIdentityCredential。
- user: 转型全栈的前端, category: 注意, comment: 别自己搭骨架，azd init 官方模板里 API、React 前端、Bicep 基础设施、Dockerfile 全都齐。我手动重建了一半才发现，白费工夫。
- user: 接手遗留代码的工程师, category: 启发, comment: 它改代码前先读 AGENTS.md、沿用原有 SDK 接入方式，不按自己的习惯重写。给老项目加功能结构没乱，这点比工具本身更值。
- user: 外包接活的我, category: 妙用, comment: 需求里没提 Copilot，只说「给这应用加个功能」，它扫 package.json 认出 @github/copilot-sdk 就切对了路线，需求写得模糊也不怕。
