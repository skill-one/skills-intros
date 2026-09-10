# expo-deployment (`expo/skills/expo-deployment`)

## blackbox

**function**: 帮你把用 Expo 做的手机应用和网页应用发布上线：云端打包、提交到苹果 App Store 和 Google Play 商店、发测试版给用户试装。

- input: 一个 Expo 项目的文件夹（写好的 App 代码）, output: 云端打包好的 iOS 和 Android 安装包文件（.ipa / .aab），可直接拿去提交商店
- input: 打包好的 iOS 应用 + 你的苹果开发者账号, output: 应用已提交到 App Store Connect / TestFlight，测试人员手机上能收到并安装
- input: 一句指令，如「把网页版发布到正式环境」, output: 一个可以访问的线上网址（正式域名或临时预览链接）
