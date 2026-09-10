# vercel-cli-with-tokens (`vercel-labs/agent-skills/vercel-cli-with-tokens`)

## comments

- user: 第一次部署的新手, category: 坑, comment: 部署完就喊客户验收, 结果人家看到的还是旧站——默认发的是 preview 预览版, 加 --prod 才正式上线.
- user: 后端老兵, category: 坑, comment: 老习惯把 --token 写进命令里, CI 日志和 shell history 留了一堆明文密钥, 被迫全部作废重发. 改成 export 环境变量才对.
- user: 管公司 CI 的运维老哥, category: 妙用, comment: 部署机 .env 里塞 VERCEL_TOKEN + ORG_ID + PROJECT_ID 三件套, 任何目录 vercel deploy -y 直接发, 不用 link, 换机器零配置.
- user: 接外包活的独立开发者, category: 注意, comment: 隔半年接手客户项目, 报 Authentication required. 先跑 vercel whoami 验 token, 过期去后台重新生成即可, 我却先怀疑了半天代码.
- user: 接手祖传项目的前端, category: 坑, comment: 本地文件夹名和线上项目不一致, 直接 vercel link 给我新建了个空项目. 改用 vercel link --project 项目名 才连上; 有 git remote 就 --repo 最稳.
- user: 刚带上 CI 值班的技术组长, category: 注意, comment: VERCEL_ORG_ID 和 VERCEL_PROJECT_ID 必须成对设置, 我只配了项目 ID 就报错. 两个值都能在项目设置页复制, 建议和 token 一起写进 .env.
