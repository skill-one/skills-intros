# azure-reliability (`microsoft/azure-skills/azure-reliability`)

## comments

- user: 运维老哥, category: 坑, comment: 先用 CLI 改完线上, 隔天 azd up 一跑全打回原形。项目里有 azure.yaml 的话直接选 B 路径改 Bicep, 一次到位, 不再被部署覆盖。
- user: 接手老项目的后端, category: 坑, comment: 我的 Function App 是 Flex Consumption, 以为健康检查改配置就行, 其实得自己在代码里写个 /api/health 函数。好在这技能动我源码前会先问, 没乱来。
- user: SRE, category: 妙用, comment: 输出按功能四行汇总、不打分, 截图直接当架构评审的现状基线, 省了我写巡检报告; 而且纯只读, 只给 Reader 权限就能跑, 不怕误操作。
- user: 独立开发者, category: 注意, comment: LRS→ZRS 存储迁移真要跑几小时到几天, 我差点在发版前夜点确认。建议安排在没有部署计划的时段, 等迁移完再补第二次部署。
- user: 第一次用的新手, category: 注意, comment: 先备齐三样: az login、resource-graph 扩展、改配置要 Contributor 权限。我只给了 Reader, 评估能跑但让它改配置就全失败, 折腾半小时。
- user: Container Apps 用户, category: 注意, comment: Container Apps 目前不在此技能范围内, 表格里会标 not assessed (planned), 只覆盖 Functions 和 App Service。用前先核对服务类型, 别白跑一趟。
