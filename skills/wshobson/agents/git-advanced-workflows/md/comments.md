# git-advanced-workflows (`wshobson/agents/git-advanced-workflows`)

## comments

- user: 开源库维护者, category: 妙用, comment: bugfix 要同时进 main 和 v2 旧分支，我以前手动改两遍。现在 main 上修完直接 cherry-pick 那个 commit 过去，比 merge 整条分支干净得多。
- user: 第一次用 rebase 的新手, category: 坑, comment: 第一次 rebase -i 改到一半直接关了终端，卡在中间态吓懵。其实 git rebase --abort 就能全退回去。现在我动手前必先开个 backup 分支。
- user: 运维老哥, category: 妙用, comment: 线上告警要热修，本地一堆改一半的代码没法切分支。用 worktree add 在另一个目录开 hotfix，互不干扰。修完记得 remove，不然白占磁盘。
- user: 测试工程师, category: 妙用, comment: 几百个提交里找引入 bug 的那个，我写了个复现脚本，bisect run 自动二分，几分钟定位。前提：工作区要先 commit 或 stash 干净。
- user: 后端组长, category: 坑, comment: 我用 --force 推 rebase 过的分支，把同事刚推的提交冲没了。从此一律 --force-with-lease：远端有别人的新提交时会直接拒绝。
- user: 独立开发者, category: 启发, comment: 以前攒一堆改动一次 commit，想拆都拆不动。现在每个逻辑点单独提交，squash、cherry-pick、回滚才真正顺手。提交习惯决定历史好不好用。
