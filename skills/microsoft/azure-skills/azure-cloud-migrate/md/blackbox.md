# azure-cloud-migrate (`microsoft/azure-skills/azure-cloud-migrate`)

## blackbox

**function**: 帮你把跑在 AWS / Google 云上的应用整体"搬家"到 Azure：先出一份体检式迁移评估报告，再把代码和配置改写成 Azure 能直接运行的版本，最后还可以帮你部署上线。

- input: 一个 AWS Lambda 项目的代码文件夹, output: 一份迁移评估报告 + 改写成 Azure Functions 的可运行代码（放在新的 <项目名>-azure 文件夹里，原代码不动）
- input: 一个部署在 Heroku 或 AWS Beanstalk 上的应用源码, output: 改好配置、能在 Azure App Service 上跑的应用代码
- input: 一个跑在 Kubernetes / Google Cloud Run / AWS Fargate 上的容器化服务, output: 对应 Azure Container Apps 的迁移后代码和配置，确认后可直接部署到 Azure 云端
