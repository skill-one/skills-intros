# upgrading-expo (`expo/skills/upgrading-expo`)

## whitebox

- 运行 `npx expo install expo@latest` 升级 Expo 本体, 紧接 `npx expo install --fix` 自动把依赖对齐到目标 SDK 的兼容版本
- 运行 `npx expo-doctor` 诊断, 定位剩余配置问题
- 按 Breaking Changes Checklist 手工修复: 替换弃用包 (如 expo-av → expo-audio/expo-video)、更新 import 路径、复查 expo.install.exclude 和 patches/ 旧补丁
- 若涉及原生变更: 无 ios/android 目录 (CNG 项目) 则跳过; 有则 `npx expo prebuild --clean` 重建, bare workflow 另清 CocoaPods/Xcode/Gradle 缓存
- 清缓存重装: 删 node_modules/.expo、`watchman watch-del-all`、`npx expo export --clear`

- 依赖对齐与校验: 核心靠 Expo 官方 CLI —— `expo install --fix` 按官方版本矩阵改写 package.json, `expo-doctor` 做一致性检查; 二者均为 npm 外部工具
- 版本探测: 通过 https://exp.host/--/api/v2/versions API 查最新版本, 依 `-preview` 后缀识别 beta (经 `expo@next` tag 安装)
- 迁移知识库: 内置 references/ 目录按 SDK 版本组织迁移指南 (React 19、New Architecture、expo-av→expo-audio/expo-video、react-navigation→expo-router 等), 加上弃用包映射表, 指导手工代码改写
