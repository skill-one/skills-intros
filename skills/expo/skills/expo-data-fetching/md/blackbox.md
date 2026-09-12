# expo-data-fetching (`expo/skills/expo-data-fetching`)

## blackbox

**function**: 帮你的手机 App (Expo/React Native) 干好一切联网相关的活——从服务器取数据、缓存、断网也能用、登录凭证安全保存, 也能修联网引发的 bug。

- input: 一个取数据的页面代码 + 描述「加载时一直转圈/白屏」, 或者一张报错截图, output: 修好的页面代码: 分清加载中、出错 (带重试按钮)、空列表三种界面, 刷新失败时旧数据也保留
- input: 一句话需求: 「断网时 App 也要能看之前刷过的内容」, output: 可直接运行的代码: 自动识别网络状态, 断网时展示缓存数据并提示离线
- input: 「登录后的 token 存哪才安全? 怎么自动续期?」, output: 完整代码: 凭证存入加密存储 (不是普通本地存储), 过期自动刷新, 每次请求自动携带
