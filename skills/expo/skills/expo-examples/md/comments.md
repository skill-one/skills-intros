# expo-examples (`expo/skills/expo-examples`)

## comments

- user: 接活的 RN 自由职业者, category: 妙用, comment: 不直接往项目里抄:先 npx degit 把整个例子拉到 /tmp 通读,缺的依赖用 npx expo install 装,版本自动对齐我的 SDK,一次没踩版本坑。
- user: 第一次接 RN 需求的前端, category: 坑, comment: 直接复制示例 package.json 里的版本号,我的项目 SDK 偏旧,一跑就崩;换成 npx expo install 装依赖才对齐,别抄它的固定版本。
- user: 维护三年老 app 的, category: 注意, comment: 示例全是最新 SDK 的 managed 项目,没有 ios/android 目录。维护 bare 老项目的话别指望整体搬进去,只取接线代码和插件配置自己合。
- user: 独立开发者, category: 坑, comment: 记忆里的例子名在仓库搜不到,白翻半天;查 meta.json 才发现标了 deprecated 并写了去向。找不到就先查它,别硬按旧目录名找。
- user: 带新人做选型的 tech lead, category: 妙用, comment: 评估要不要用某库时,不开本地环境,直接点例子自带的 launch.expo.dev 链接,手机扫码就跑通完整流程,比读 README 直观得多。
- user: Web 转 RN 的新手, category: 坑, comment: 用 raw 链接拉示例文件一直 404,查了半天是分支名:这仓库默认分支是 master 不是 main,链接里写 main 全部失败。
