# expo-upgrade (`expo/skills/expo-upgrade`)

## whitebox

- 升级主包: `npx expo install expo@latest`, 再 `npx expo install --fix` 把所有依赖对齐到与 SDK 兼容的版本
- 跑诊断: `npx expo-doctor` 检出问题 (如缺失 peer 依赖) 并修复
- 清缓存重装: `npx expo export -p ios --clear`, 删 node_modules 与 .expo, `watchman watch-del-all`
- 有原生变更时: 项目存在 ios/ 或 android/ 目录则 `npx expo prebuild --clean` 重新生成 (纯 CNG 项目跳过此步与缓存清理)
- 过破坏性变更清单: 按目标 SDK 版本查 references 修 API 变更、迁移废弃包、删冗余配置 (babel/metro/patches)

- 分版本参考文件: 破坏性变更按 SDK 版本内置在 references 里逐条套用 — react-19.md (SDK54), new-architecture.md (SDK53), expo-av 拆分为 expo-audio/expo-video 与 native-tabs (SDK55), react-navigation 迁移 expo-router (SDK56, 含 codemod)
- 外部工具链: expo CLI (install --fix / prebuild / export)、expo-doctor (诊断校验, 每次删依赖后必跑一次)、watchman、cocoapods 与 gradle (仅 bare workflow 清缓存)
- 特例短路规则: 存在 Hermes V1 内存回归时, SDK 55 及以下直接跳升到 SDK 57 且 expo@57.0.9+; 逐项复审 app.json 的 expo.install.exclude 和 patches/ 旧补丁是否仍必要; beta 版通过 versions API 检测 `-preview` 后用 `npx expo install expo@next --fix`
