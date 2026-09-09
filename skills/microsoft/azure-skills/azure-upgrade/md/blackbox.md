# azure-upgrade (`microsoft/azure-skills/azure-upgrade`)

## blackbox

**function**: 帮你把现有的 Azure 应用升级到更好的套餐/新服务 (如函数应用计划、Redis 缓存), 或把老 Java 代码里过时的 Azure 写法换成新写法——先给评估结论, 确认后完成迁移并验证可用, 旧资源原样保留。

- input: 一句话指令: 「把我的 Function App 从 Consumption 计划升级到 Flex Consumption」, output: 一份升级可行性评估报告 (哪里兼容、哪里要注意) → 你确认后, 得到一个在新计划上跑起来的同款函数应用: 配置、身份都已搬好, 默认网址打开正常; 旧应用原样保留, 等你决定是否清理
- input: 一个用旧版 Azure SDK (com.microsoft.azure.*) 的 Java 项目代码, output: 改用新版 SDK (com.azure.*) 的源码文件, 附一份改动清单: 哪些类换成了什么新写法
- input: 一句话指令: 「我的 Premium P2 Redis 缓存想迁到 Azure Managed Redis, 帮我选个规格」, output: 推荐的目标规格 (SKU) 及理由 + 迁移完成的新缓存实例和配置; 旧缓存保留, 你确认无误后再清理
