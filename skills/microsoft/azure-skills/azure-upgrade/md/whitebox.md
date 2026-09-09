# azure-upgrade (`microsoft/azure-skills/azure-upgrade`)

## whitebox

- Identify: 确定源→目标的 plan/SKU (如 Functions Consumption→Flex), 向用户确认后才开始
- Assess: 分析现有应用的升级就绪度, 并按场景加载对应参考文档 (scenario reference)
- Pre-migrate: 收集旧应用的设置、身份、配置, 备好迁移素材
- Upgrade: 执行自动化升级 (新建资源、迁移设置、部署代码), 脚本保证幂等可续跑, 进度记入 upgrade-status.md
- Validate: 访问 function app 默认 URL 确认可达、校验端点与监控, 然后询问用户是否验证性能/清理旧应用/更新 IaC, 按需交接给 azure-validate 或 azure-deploy

- 场景路由: 按源→目标映射表选参考文档 (consumption-to-flex.md / redis-to-amr.md / java README); Java SDK 升级走独立的源码现代化流程, 不套用通用升级 Steps; Redis 场景再转交 GitHub 上的专用 skill (amr-migration-skill / acre-to-amr-migration-skill); 无匹配场景时改用文档工具自行研究升级路径
- Azure MCP 工具链 (外部依赖): mcp_azure_mcp_get_azure_bestpractices 取最佳实践、mcp_azure_mcp_documentation 查升级文档、mcp_azure_mcp_appservice 查 plan/应用详情、mcp_azure_mcp_applicationinsights 验证监控配置
- 安全护栏: 评估必须先于任何升级操作; 目标 plan/SKU 和破坏性动作 (删除/停止原应用) 均需用户显式确认, 违者用 ask_user 拦下
