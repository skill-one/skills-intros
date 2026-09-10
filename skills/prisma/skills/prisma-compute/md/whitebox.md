# prisma-compute (`prisma/skills/prisma-compute`)

## whitebox

- 检查项目现状: 包管理器、框架、package.json 脚本、prisma.compute.ts、已有 compute:deploy 脚本
- 核对命令语法与登录态: 先看 CLI --help 输出, 再跑 auth whoami / auth workspace list 确认认证上下文
- 按任务分流: 已有应用用生成的 compute:deploy 或 app deploy; 新项目用 create-prisma 脚手架; 自动化场景用 compute-sdk 或 Management API
- 检查部署就绪条件: 框架在支持列表内、绑定 0.0.0.0、监听 PORT、60 秒内可响应; 可行时先本地构建/ app build
- 执行部署 (自动化时加 --json --no-interactive), 部署后请求公网 URL 验证, 汇报 app/部署/项目/workspace 各项 id 及后续步骤

- 证据优先级链: 项目生成配置 (prisma.compute.ts / compute:deploy) > CLI help 输出 > 本地安装的包代码与类型定义 > 官方文档, 一切编辑和命令都按此顺序取事实, 不凭记忆猜命令
- 双认证源切换: 非空 PRISMA_SERVICE_TOKEN 即为生效凭证且无视本地 OAuth 工作区; 否则由'活动工作区指针'选取本地存储的 OAuth 会话, 换区必须显式 auth workspace use, 不静默降级到其他缓存会话
- 类型化部署配置: prisma.compute.ts 用 defineComputeConfig 声明单 app 或 monorepo 的 apps 目标 (framework/entry/httpPort/env 文件等), CLI 显式 flags 覆盖配置值; 依赖外部工具 @prisma/cli (部署/日志/auth)、create-prisma (脚手架)、@prisma/compute-sdk (编程式部署), 最终对接 Prisma Compute 平台
