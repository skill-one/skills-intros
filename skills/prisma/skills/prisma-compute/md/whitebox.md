# prisma-compute (`prisma/skills/prisma-compute`)

## whitebox

- 按决策树给任务分类 (已有应用部署 / 配置 / 框架适配 / 排障等), 只加载对应的 reference 文件
- 侦查项目现状: 包管理器、框架、package.json 脚本、prisma.compute.ts、已生成的 compute:deploy 脚本
- 用 CLI help 输出确认命令语法, 并核实认证上下文 (auth whoami --json; 存在多会话时用 auth workspace list --json)
- 可行时先本地构建, 再执行 @prisma/cli app deploy (自动化场景用 --json --no-interactive, 生产部署需 --prod --yes)
- 部署后请求公开部署 URL 验证 (不信本地就绪检查), 汇报 app URL 与各 ID 及后续步骤

- 分级规则约束系统: 8 类带前缀快速规则按优先级生效 (verify- > auth- > framework- > runtime- > config- > env- > deploy- > sdk-), 例如『命令必须先用 help 验证』『永不打印 token/密钥』『部署必须绑定 0.0.0.0 并读取 PORT』
- 证据优先级仲裁: 遇到歧义按 固定顺序取证 — 项目生成配置 (prisma.compute.ts / compute:deploy) > CLI help > 本地安装包代码 > 官方文档; 认证来源则是 PRISMA_SERVICE_TOKEN 优先, 有值时忽略本地 OAuth workspace
- 依赖的外部工具: bunx 调 @prisma/cli (部署/构建日志/认证/域名), create-prisma 仅用于新项目脚手架, @prisma/compute-sdk 与 Management API 用于程序化部署, GitHub check run 和 build logs 用于排查 CI 构建失败
