# expo-upgrade (`expo/skills/expo-upgrade`)

## comments

- user: 独立开发老哥, category: 坑, comment: 从 SDK 53 升级别停在 56, 官方要求直接跳 57 且用 expo@57.0.9 以上, 否则 reanimated 内存暴涨, 我在 56 上查泄漏查了两天。
- user: 外包项目维护者, category: 注意, comment: 动手前先看项目根目录有没有 ios/ 和 android/ 目录, 有就是 bare workflow, 直接跑 prebuild --clean 会把你手改的原生配置全抹掉。
- user: 第一次升级的新手, category: 坑, comment: 我只跑了 expo install expo@latest 就启动, 白屏报依赖版本冲突。必须再跑 expo install --fix 对齐依赖, 最后 expo-doctor 体检一遍。
- user: 全职 RN 开发, category: 妙用, comment: package.json 里 expo.install.exclude 锁的包多是绕旧 bug 的临时手段, 升级完挨个复查, 我删掉 reanimated 排除项后冲突全消。
- user: 音频 App 开发者, category: 注意, comment: expo-av 已废弃, 音频迁 expo-audio、视频迁 expo-video, API 全变了。务必先改完代码里的引用再卸载旧包, 反过来直接编译不过。
- user: 接手祖传项目的前端, category: 妙用, comment: babel.config.js 和 metro.config.js 若只剩 expo 默认内容, 可以直接删文件。升完项目干净一截, expo-doctor 也不再报这类噪音。
