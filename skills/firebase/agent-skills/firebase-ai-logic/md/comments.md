# firebase-ai-logic (`firebase/agent-skills/firebase-ai-logic`)

## comments

- user: 第一次用的新手, category: 坑, comment: 抄了篇旧教程，写死 gemini-1.5-flash 一直报错；换 gemini-flash-latest 就通了。另外 API 用 init 命令开通就行，别在控制台瞎点半天。
- user: 独立开发者, category: 坑, comment: 把 20 多 MB 的 PDF 直接塞 inline data，稳吃 HTTP 413；传到 Cloud Storage 再把 URL 传给模型才正常，小文件没事。
- user: 前端接单佬, category: 妙用, comment: 模型名写死在客户端，一过期就得重新发版；用 Remote Config 远程改模型名，线上 App 不发新版就切到新模型，省了一次发版审核。
- user: 周末side-project选手, category: 注意, comment: 文字对话在 Developer API 免费档随便玩，但生图（Nano Banana）必须升级 Blaze 按量付费，做图像功能前先确认账单方案，别写完代码才发现跑不了。
- user: 后端老兵, category: 启发, comment: 以前接 AI 功能必搭一层代理后端藏 key，这次客户端 SDK 直连加 App Check 就够了，配额不会被恶意刷。小项目可以真的不写后端了。
- user: 跨端App开发, category: 妙用, comment: 多轮对话不用自己维护 history，startChat 自动记上下文；再换成 generateContentStream，回答像打字一样逐字出，体验立马上一个档次。
