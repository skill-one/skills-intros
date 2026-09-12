# expo-examples (`expo/skills/expo-examples`)

## whitebox

- 把用户需求映射到 with-<库> 示例名 (先查本地 catalog.md 快筛, 再用 gh api 拉取仓库实时目录确认, 并查 meta.json 排除已改名/废弃的示例)
- 一次性列出该示例的完整文件树, 按信噪比顺序读关键文件: README (安装) → package.json (依赖) → app.json (config 插件/权限) → 集成代码 → .env (所需密钥); 文件多时改用 degit/sparse-clone 拉进临时目录再读
- 已 有项目的用户走 Inspiration 模式: 把示例当参考, 手工把模式移植进用户代码, 绝不在其项目上脚手架; 全新项目走 Scaffold 模式: npx create-expo --example 直接起步
- 非破坏式适配: 只加示例引入而用户缺失的东西 — 用 npx expo install 补依赖 (解析 SDK 匹配版本), 合并 app.json 插件/权限而非替换, 移植集成代码, 按示例 .env 形状重建环境变量
- 完成标准: 集成代码移植完, 且它依赖的每个依赖/插件/权限/环境变量都已在用户项目中落位, 而非仅表面接通

- 数据源 = expo/examples 官方仓库 (GitHub), 默认分支是 master 不是 main; 通过 gh api 或 raw URL 读取, meta.json 是改名/废弃示例的唯一事实来源, 本地 catalog.md 只是可能漂移的快照
- 适配核心约束是非破坏式: 依赖不照抄示例的固定版本号 (示例跟随最新 SDK), 必须经 npx expo install 解析出与用户项目 SDK 匹配的版本; 配置只增量合并, 保留用户原有配置块
- 外部工具链: gh api (列目录/读文件), curl raw URL (无 gh 时的兜底), npx degit 或 git sparse-checkout (拉取示例到临时目录, 避免整仓 ~64MB 克隆, 用完即删), npx create-expo / bun create expo (脚手架模式), npx expo install (装 SDK 匹配依赖)
