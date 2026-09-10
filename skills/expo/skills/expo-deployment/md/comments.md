# expo-deployment (`expo/skills/expo-deployment`)

## comments

- user: 第一次发 iOS 的新手, category: 坑, comment: 以为 eas build 得本地装 Xcode——它是云构建. iOS 提交还必须先买 99 美元/年开发者账号, 免费账号 build 成功也交不上去.
- user: 后端转来的全栈, category: 注意, comment: 安卓自动提交前要先去 Play Console 建 service account、下载 JSON 密钥填进 eas.json. 我漏了这步, build 都成功, submit 一直报错卡了一晚.
- user: 独立开发者, category: 妙用, comment: 睡前跑 build --submit, 云端构建完自动交商店, 早上直接收 TestFlight 邮件. 再也不用守着 Mac 盯几小时打包, 命令挂后台就行.
- user: 吃过版本冲突亏的团队老手, category: 坑, comment: 开了 appVersionSource remote 后我本地改 buildNumber 没生效——版本号只认云端, 要用 eas build:version:set 改. 别再翻 Info.plist 白忙了.
- user: 前端第一次发应用, category: 注意, comment: 第一版直冲 App Store 审核被拒两次. 后来学会先 npx testflight 提 TestFlight 给真人测一轮再上, 通过率高很多, 也省得来回等审核.
- user: 出海 App 运营, category: 妙用, comment: 商店标题、副标题、关键词全放进 metadata 文件跟代码走, 改文案发个 PR 就同步商店页, 不用再登 App Store Connect 一格格手动填.
