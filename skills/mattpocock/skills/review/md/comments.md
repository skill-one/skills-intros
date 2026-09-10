# review (`mattpocock/skills/review`)

## comments

- user: 前端新人, category: 坑, comment: 改完没 commit 就喊它 review，diff 是空的——它只比 HEAD 和基准点，未提交的改动看不见。先 commit 再跑。
- user: 后端老兵, category: 妙用, comment: 接手的老仓库一行规范文档都没有，本以为 Standards 轴没得查，它内置的坏味道基线照样出活；有文档的仓库则文档优先，不误报。
- user: 团队 Tech Lead, category: 注意, comment: 坏味道结论是判断题不是硬违规，别照单全收逼人改；lint 能查的它主动跳过。拿它当评审初筛，别当终审。
- user: 独立开发者, category: 启发, comment: 它靠 commit 里的 issue 号找需求来源，找不到就明说跳过。被治好了不写 issue 号的毛病，现在每条 commit 都带 Closes #xx。
- user: 常审同事 PR 的组员, category: 妙用, comment: 用 main 当基准点审功能分支，修 bug 时混进来的顺手重构被 Spec 轴单独列为「没被要求的行为」，scope creep 当场现形。
- user: DevOps 小哥, category: 注意, comment: docs/agents/issue-tracker.md 不存在就先跑 /setup-matt-pocock-skills，否则 commit 里的 issue 号拉不到内容，Spec 轴直接空手而归。
