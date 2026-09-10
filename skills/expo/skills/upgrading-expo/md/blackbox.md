# upgrading-expo (`expo/skills/upgrading-expo`)

## blackbox

**function**: 帮你把 Expo 项目升级到最新 SDK 版本, 并修好升级后所有跑不起来的报错和过期写法。

- input: 一个 Expo 项目 (告诉我项目路径 + 目标 SDK 版本, 如 '升级到 SDK 54'), output: 升级完成的项目: 依赖版本对齐、能正常构建运行, 附一份本次改了什么的清单
- input: 升级后的报错信息或代码片段 (如 'expo-av 已弃用'、'useContext 用法报错'), output: 改好的代码文件, 用新 API 替换了旧写法, 直接可用
- input: 项目的 package.json 或 app.json, output: 一份诊断报告: 哪些包已弃用及替代方案、哪些配置冗余可删、哪些补丁可移除, 以及对应的修改后文件
