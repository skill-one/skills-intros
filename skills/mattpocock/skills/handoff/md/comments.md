# handoff (`mattpocock/skills/handoff`)

## comments

- user: 第一次用的新手, category: 坑, comment: 我以为它会在对话快满时自动存档,结果直接关窗口,上下文全丢。它不会自己触发,离开前要自己敲 /handoff。
- user: 独立开发者, category: 妙用, comment: 先 git commit 再跑 handoff,文档只引用提交号、不复述改动,交接文件短到一屏,新会话照样接得上。
- user: 后端老兵, category: 妙用, comment: 命令后面跟一句"下个会话要干嘛",文档立刻聚焦。我写"继续修登录超时",新会话开场直奔正题,不绕路。
- user: 运维老哥, category: 注意, comment: 文档存在系统临时目录,不在项目文件夹里,重启可能被清。要留档就拷走,或把路径原样贴给下次会话。
- user: 带远程协作的组长, category: 坑, comment: 直接把文档发给同事,里面路径全是我本机的,他打不开。后来先 push 再跑,保证引用的文件仓库里都有。
- user: 多线程的产品经理, category: 启发, comment: 我把它当"游戏存档点":切任务前跑一次,回来新会话读文档就能续上,连下一步该调用哪些技能都替下家列好了。
