# entra-app-registration (`microsoft/azure-skills/entra-app-registration`)

## blackbox

**function**: 帮你让应用安全地接入 Microsoft 账号登录和微软云服务授权——从在 Entra ID (微软的账号管理中心, 原 Azure AD) 注册应用、配置权限, 到给你能直接跑通的登录代码。

- input: 「我想让我的 Node.js 网站支持『用 Microsoft 账号登录』」, output: 一份从零开始的操作清单: 注册应用要填什么、回调地址怎么配、需要哪些权限; 外加能直接运行的登录代码, 以及注册完成后要记下的 Client ID / Tenant ID 说明
- input: 一段报错信息, 如「AADSTS7000218: client secret 已过期」, output: 用大白话解释报错原因 + 修复步骤: 在哪里生成新密钥、在应用里更新哪里, 避免下次再过期
- input: 「我有个后台定时任务要读 Microsoft 365 数据, 没有人守着它登录」, output: 一套无需人工登录的方案: 该申请什么权限、用密钥还是证书, 以及对应的设置命令和调用示例代码
