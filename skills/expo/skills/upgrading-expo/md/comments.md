# upgrading-expo (`expo/skills/upgrading-expo`)

## comments

- user: 从 Web 转来的新手, category: 坑, comment: 直接用 npm 装 expo, 依赖版本全乱了。后来才明白要 npx expo install expo@latest 再跟 --fix, 版本让 Expo 说了算。
- user: 音视频 App 开发者, category: 坑, comment: 升 SDK 55 没先迁代码, 录音直接挂——expo-av 弃用了。先把 Audio.Sound 换成 useAudioPlayer 再删旧包, 顺序别反。
- user: 自维护 ios/ 目录的独立开发者, category: 注意, comment: 升完要跑 npx expo prebuild --clean 才吃到原生改动, 但它会把 ios/ 整个重新生成, 我手工改过的原生代码是先备份再跑的。
- user: CNG 项目的全栈, category: 妙用, comment: 升级前后各跑一次 npx expo-doctor, 对比输出就知道问题出在哪个依赖; 我们仓库没 ios/android 目录, 整个升级就两条命令的事。
- user: 动画重度用户, category: 坑, comment: 升到 SDK 54 动画全崩, 查半天是缺 react-native-worklets——它是 reanimated 的前置依赖, 单独装上就好。
- user: 接手祖传代码的前端, category: 启发, comment: 借升级把 expo.install.exclude 和 patches/ 全审了一遍, 俩老 workaround 直接删了, 只剩默认配置的 babel.config.js 也一并清掉。
