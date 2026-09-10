# expo-dev-client (`expo/skills/expo-dev-client`)

## blackbox

**function**: 给你的 Expo 项目打一个专属的测试版 App（自定义版 Expo Go 壳子），装到手机上就能实时运行调试，还能发给团队内测。

- input: 一个 Expo 项目文件夹 + 一句「帮我打个 iOS 测试包」, output: 一个可安装的测试 App 安装包（.ipa 文件），装上手机就能跑你的项目
- input: 「我的项目用了 Expo Go 里没有的第三方库，打不开了」, output: 一个专属测试 App：手机装好后启动 Metro，改代码保存立刻在真机上看到效果
- input: 「让同事在他们 iPhone 上试试我的半成品」, output: 同事手机的 TestFlight（苹果官方内测平台）里出现你的测试 App，点一下就装好，构建完成还会收到邮件提醒
- input: 一段打包失败的报错信息（如签名错误）, output: 修好的打包配置 + 一条重新打包成功、可正常安装的 App
