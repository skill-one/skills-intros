# gh-cli (`github/awesome-copilot/gh-cli`)

## comments

- user: 后端老兵, category: 妙用, comment: 子命令没覆盖的接口我全用 gh api 打，比如 gh api repos/:owner/:repo/traffic/views，token 它自己带上，不用再配 curl 请求头。
- user: 第一次用的新手, category: 坑, comment: gh repo delete 一直报权限错，查了半天才知道默认登录没有 delete_repo 权限，先跑 gh auth refresh -s delete_repo 才能删。
- user: 运维老哥, category: 注意, comment: 脚本里别用交互登录，设 GH_TOKEN 环境变量就行；不在仓库目录里跑命令记得加 GH_REPO=owner/repo，否则报找不到仓库。
- user: 独立开发者, category: 妙用, comment: 收尾必用 gh pr merge 123 --squash --delete-branch，合并完本地远程分支一起删，再不用手动 git branch -D 了。
- user: 写脚本的数据工程师, category: 坑, comment: 输出默认进分页器，crontab 里直接卡死。我设 GH_PAGER=cat，且只用 --json --jq 取字段，别解析表格，格式一变就崩。
- user: 开源项目维护者, category: 启发, comment: review 别人 PR 不再只盯着 diff 看了，gh pr checkout 123 拉到本地跑一遍测试再评，误判少了一大半。
