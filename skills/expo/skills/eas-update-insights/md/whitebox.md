# eas-update-insights (`expo/skills/eas-update-insights`)

## whitebox

- 用 eas update:list --json --non-interactive 拿到最近发布组列表, jq 取 .currentPage[0].group 得到 group ID
- 对该 group 跑 eas update:insights <id> (可选 --days/--platform); 查频道级 embedded/OTA 用户分布则改用 eas channel:insights --channel <name> --runtime-version <v>
- 输出统一加 --json, 用 jq 提取 totals.crashRatePercent / installs / uniqueUsers / payload 等关键字段
- 跨平台、跨版本或跨频道对比指标, 识别异常 (如某平台 crashRate 骤升), 按阈值过滤即得健康门禁 (如 crashRatePercent > 1 的平台)

- 全部能力 = 调用 eas-cli 的子命令 (allowed-tools 限定 Bash(eas *)), 无自有业务逻辑; 前提: eas-cli 已安装、eas login 已登录, 且 channel:insights 必须在 Expo 项目目录运行 (从 app.json 解析 project ID)
- 解析/校验靠 jq + JSON 结构: update:list 返回 currentPage[] 数组 (同次发布的 iOS/Android 合并为一条); update:insights 返回 platforms[].totals 和 daily[] 时间序列, 其中 crashRatePercent = failedInstalls / (installs + failedInstalls) × 100, 无安装时为 0
- 数据是 EAS 服务端聚合指标 (与 expo.dev 更新详情页同源, 按发布量计费), 自带滞后性: installs 是下载而非确认启动, crash 靠下次 update check 自报 (最长约 24h); channel:insights 的 mostPopularUpdates 只返回 top-N, otaTotalUniqueUsers 是其求和, 活跃 update 超过 N 时会低估总覆盖
