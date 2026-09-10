# replicas-agent (`replicas-group/skill/replicas-agent`)

## comments

- user: 第一次用的新手, category: 坑, comment: 上来就 docker ps,报连不上 daemon——它预装了但不会自启。先按 DOCKER.md 把 daemon 拉起来,再跑 compose 就一路顺畅。
- user: 后端老兵, category: 妙用, comment: 修完 bug 起个服务,用 Preview 生成公开链接直接丢进 Slack 群,同事手机点开就能验收,省掉内网穿透那套折腾。
- user: 运维老哥, category: 注意, comment: 我让它读我已有的 Google 表格,读不了——它只能操作自己创建的文件。旧内容得先复制进新文件,或直接贴给它。
- user: 独立开发者, category: 妙用, comment: 把 Linear 链接直接甩给它:拉 issue、改代码、开 PR、回评论关单一条龙。我只看 PR 里的 diff,验收快很多。
- user: 前端工程师, category: 注意, comment: 录屏嵌进消息里又糊又变形,就是没按 MEDIA.md 的推荐宽高比和帧率来。动手前先翻对应参考文件,省得重录。
- user: 带团队的技术经理, category: 启发, comment: 以前连「怎么配环境变量」也丢给它,现在这类怎么用的问题先查 docs.replicas.dev,agent 只留给要它真正动手的活,又快又准。
