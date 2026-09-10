# expo-deployment (`expo/skills/expo-deployment`)

## whitebox

- 初始化: 安装 eas-cli、eas login 后执行 npx eas-cli init, 项目接入 EAS 并生成 eas.json。
- 写配置: 在 eas.json 中填好 production 构建档案 (autoIncrement 等) 和 submit 档案 (Apple/Google 商店凭据)。
- 云端构建: eas build -p ios|android --profile production, 二进制包在 EAS 云服务器上产出, 版本号随 appVersionSource remote 自动递增。
- 提交商店: 同一命令追加 --submit (iOS 也可 npx testflight), 包送入 App Store Connect / Google Play Console 内部轨道。
- 核验状态: 用 eas build:list、eas build:view、eas submit:list 追踪构建与提交进度。

- 唯一入口是 EAS CLI (外部依赖: npm 包 eas-cli): 所有动作都是发往 Expo 云端服务的命令, 构建在 EAS Build 云服务器完成 (iOS 默认 m-medium 规格), 本地无需 Xcode/Gradle 工具链。
- eas.json 是声明式配置中枢, 被解析后驱动全流程: build 档案控制 autoIncrement 与资源规格; submit 档案存商店凭据 (iOS: appleId/ascAppId; Android: serviceAccountKeyPath + track); iOS 签名凭据经 eas credentials 管理; 版本号托管用 appVersionSource: remote。
- Web 是独立的导出+托管路径: expo export -p web 产出静态 bundle (API 路由随包一起), 再由 eas deploy [--prod] 推到 EAS Hosting, 每个 PR 可得预览 URL; 各平台细节按需查阅 references/ (testflight、play-store、ios-app-store、app-store-metadata、workflows)。
