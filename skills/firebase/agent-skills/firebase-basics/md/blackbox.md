# firebase-basics (`firebase/agent-skills/firebase-basics`)

## blackbox

**function**: 帮你完成 Firebase (谷歌的应用云服务) 的基础配置：登录账号、创建或切换项目、给你的 App 下载连接 Firebase 所需的配置文件。

- input: 「帮我登录我的 Firebase 账号」（或「看看现在登录的是谁」）, output: 当前登录的账号邮箱被确认显示，之后所有操作都有权限执行
- input: 「新建一个项目，ID 叫 my-cool-app-123」, output: Firebase 上出现这个新项目，并已设为当前正在使用的项目
- input: 「把我现有的项目切到 abc-todo-app」, output: 当前项目切换成功，后续操作都作用在这个项目上
- input: 一个 Android/iOS 应用的 ID（如 1:123456789:android:abcd1234）, output: 对应的配置文件（Android 的 google-services.json 或 iOS 的 GoogleService-Info.plist）直接放进你的 App 工程目录里，App 即可连上 Firebase
