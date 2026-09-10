# using-git-worktrees (`obra/superpowers/using-git-worktrees`)

## comments

- user: 前端开发, category: 妙用, comment: 我常在改样式时突然要修线上 bug。现在开个隔离工作区, 原分支一动不动, 修完切回来接着写, 再不用 stash 来回倒腾。
- user: 第一次用的新手, category: 坑, comment: 我建了工作区目录没先确认被忽略, git add 时把整份代码副本提交进了仓库, 仓库直接膨胀。现在建目录前都先查 .gitignore。
- user: 用 submodule 的工程师, category: 注意, comment: 我们在子模块里开发, 目录检测会误判成'已在隔离区'。这技能会先排除子模块再下结论——遇到子模块别只看两个 git 目录是否不同。
- user: 后端老兵, category: 启发, comment: 以前直接在当前目录开写, 测试挂了说不清是我改坏的还是本来就坏。现在开工先跑基线测试, 挂了当场定责, 省了无数扯皮。
- user: 技术负责人, category: 注意, comment: 有队友图快手敲 git worktree add, 结果生成了工具面板看不见、也没法统一清理的目录。有平台自带的工作区命令就一定用自带的。
- user: 运维老哥, category: 妙用, comment: 服务器上沙箱不让建目录, 它不硬刚权限, 直接说明情况改在当前目录干活, 顺手装依赖跑通基线测试。被打断的需求当天也交付了。
