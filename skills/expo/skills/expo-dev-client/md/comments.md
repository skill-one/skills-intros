# expo-dev-client (`expo/skills/expo-dev-client`)

## comments

- user: 前端转 RN 的, category: 坑, comment: 在 Expo Go 里跑第三方原生模块直接白屏，白查两小时。文档写着 "not supported in Expo Go" 就别硬试，直接装 dev client，一次就通。
- user: 省钱的独立开发, category: 妙用, comment: 日常调试我全加 --local 本机打包，iOS 有 Xcode 就免费；云端构建分钟数（要花钱）留给队友要装的包。
- user: 带测试团队的后端老兵, category: 妙用, comment: 一条命令 build + --submit，包自动进 TestFlight 并邮件通知，测试自己装，我不再在群里挨个发安装包。
- user: 第一次发 TestFlight 的新手, category: 注意, comment: 分发到真机和 TestFlight 必须有付费 Apple 开发者账号（99 美元/年），免费账号只能跑本机模拟器，我卡了一下午。
- user: 准备发版的独立开发者, category: 注意, comment: 这只是开发调试包。正式发 TestFlight 给用户、上架商店是另一套流程（eas-app-stores 技能），别拿 development 包当正式版。
- user: RN 半年的半新手, category: 启发, comment: 之前拿 Expo Go 当 app 给客户演示，功能缺一半很尴尬。现在项目第一天就装 dev client，演示的才是真东西。
