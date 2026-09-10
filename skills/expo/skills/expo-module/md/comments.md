# expo-module (`expo/skills/expo-module`)

## comments

- user: 第一次给 App 加原生功能的前端, category: 坑, comment: 非交互模式我用 --name 想定文件夹名, 结果它只改原生类名, 目录还是按 slug 生成, 白删重建一遍。目录名要用位置参数直接传 slug 或路径。
- user: 跨端 App 独立开发者, category: 注意, comment: 我照模板抄 expo-module.config.json, iOS 那行只写类名, Android 也跟着只写类名, 结果安卓自动链接找不到模块。Android 必须写完整包名+类名, 两行不对称。
- user: 单 App 小团队维护者, category: 妙用, comment: 只想给一个 App 加原生功能, 我先建了 standalone 模块, example app 和发布配置全是累赘。换 local module 后默认放 modules/, 直接用宿主工具链, 清爽多了。
- user: RN 老项目维护者, category: 走错门, comment: 我的活是把旧 Swift 模块迁到 2.0 宏写法, 拿这个技能折腾半天方向就不对——那该用 expo-migrate-module。动手前先分清任务是新建还是迁移。
- user: 负责封装原生 SDK 的初中级开发, category: 妙用, comment: 脚手架时用 --features 选好 AsyncFunction、Event 这些, 生成的是可直接改的真实示例, 比空白文件从零写快很多。不选会生成极简骨架, 别误以为装坏了。
- user: 踩过链接问题的半新手, category: 坑, comment: local 模块默认不生成 index.ts, 我 import 报找不到导出, 还以为自动链接挂了。其实加 --barrel 才有入口文件, 脚手架前想清楚要不要 barrel。
