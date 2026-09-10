# eas-update-insights (`expo/skills/eas-update-insights`)

## blackbox

**function**: 查询你们 App 已发布的 OTA 更新 (不重新发版、手机上直接热更的更新) 健康状况: 装了多少人、崩溃率高不高、包体多大、还有多少用户停在旧版本上。

- input: "生产环境刚发的那个更新现在怎么样?", output: 该更新的健康报告: iOS / Android 各自的安装人数、崩溃率 (%)、平均包体大小, 附最近 7 天每日启动与失败次数的走势
- input: 一个更新组 ID + 时间范围 (如「只看过去 24 小时」), output: 该时段各平台的启动数、失败数、崩溃率数据 (表格或 JSON), 用来判断新版是否比上一版崩得更多
- input: 渠道名 + 版本号 (如 production / 1.0.6), output: 该渠道上有多少用户还在用装机内置的旧版本、多少用户已收到在线更新, 以及当前最受欢迎的更新排行
