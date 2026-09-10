# deploy-to-vercel (`vercel-labs/agent-skills/deploy-to-vercel`)

## comments

- user: 前端新手, category: 坑, comment: 我只说了句"帮我部署上线", 拿到的是随机 xxx.vercel.app 预览链接, 以为域名配坏了. 想发到正式域名必须明说"部署到生产".
- user: 独立开发者, category: 妙用, comment: 在 claude.ai 里没登录 Vercel 也能发: 走兜底脚本部署, 先拿 Preview URL 发朋友试用, 满意再用 Claim URL 一键转到自己账号接管.
- user: 运维老哥, category: 注意, comment: 兜底脚本打包只排除 node_modules、.git 和 .env. 密钥写在 .env.local 或 config.js 的, 上传前先挪进 .env, 别裸奔.
- user: 多团队自由职业者, category: 注意, comment: 我名下有两个团队, 首次部署它会列出来让我选一个, 选完直接跑到底不再二次确认. 选错就得重新 link 换组织, 开局那步要想清楚.
- user: 后端老兵, category: 妙用, comment: 本地文件夹名和 Vercel 项目不同名时 link 老对不上, 让它按 git 远程仓库匹配 (--repo) 一次就中, 之后 push 即自动部署, 一劳永逸.
- user: 远程团队产品经理, category: 注意, comment: 它给链接时构建可能还在后台跑, 直接转发群里可能打不开. 先让它 inspect 查下状态, 确认部署成功再发客户, 免得白解释一轮.
