# cloud-run-basics (`google/skills/cloud-run-basics`)

## whitebox

- 根据需求归类到三种资源之一：service (HTTP 服务) / job (定时或一次性任务) / worker pool (常驻后台消费)
- 前置检查：启用 Cloud Run Admin 与 Cloud Build API，确认所需 IAM 角色已绑定
- 按 SKILL.md 中的命令模板生成 gcloud 命令，填入服务名、镜像地址、区域等参数
- 部署时分流：给镜像则直接从 Artifact Registry / Docker Hub 导入；给源码则交给 Cloud Build + buildpacks 云端自动构建
- 等待部署成功输出；若失败按错误类型走排障分支（读日志 / 查 references 文档）

- 命令模板替换 + 硬校验：SKILL.md 内置各资源类型的标准 gcloud 命令模板，按占位符 (SERVICE_NAME, IMAGE_URL, REGION...) 填参；附带一条关键校验规则——用户代码必须监听 0.0.0.0 并读取注入的 $PORT，否则启动即崩
- 构建路径分流：有 Dockerfile → Cloud Build 直接执行它；无 Dockerfile → Google Cloud buildpacks 自动构建；已编译产物可 --no-build 跳过构建快速部署，但遇原生依赖编译错误需回退 --source 走 buildpacks 重新编译
- 失败处理路由：部署失败时按症状查表——IAM/权限错误查 iam-security.md，启动崩溃用 gcloud logging read 拉日志定位，知识盲区用 Developer Knowledge MCP 的 search_documents 补齐
