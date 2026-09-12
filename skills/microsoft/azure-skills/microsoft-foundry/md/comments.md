# microsoft-foundry (`microsoft/azure-skills/microsoft-foundry`)

## comments

- user: 后端老兵, category: 妙用, comment: 线上 agent 半夜挂了,我只说一句「排查并修复」,它自己走完调用→查日志→定位→改代码→重部署→再验证的闭环,我全程只看结论。
- user: 第一次用的新手, category: 坑, comment: 上来就说「部署我的 agent」,结果项目里没 azure.yaml 也没 .foundry 目录,直接被反问卡住。先把工程文件建好再来,一次就通。
- user: 运维老哥, category: 注意, comment: 它只管 Foundry,App Service、Functions 这类普通 Azure 部署要找别的技能。另外模型部署报错多半是配额不够,先让它查配额再动手。
- user: 算法工程师, category: 妙用, comment: 最惊喜的是把线上 trace 直接沉淀成评测集,还带全链路溯源;改 prompt 前先跑一遍回归,心里有底,不怕改崩线上。
- user: AI 产品经理, category: 启发, comment: 持续评测能挂进 CI/CD 后,每次部署自动跑评测当质量门禁,倒逼我们先写评测集再改 agent。顺序反过来了,返工反而更少。
- user: 独立开发者, category: 注意, comment: 一个目录只放一个 agent,它能自动认出项目和环境;我图省事把两个 agent 塞一个仓库,每次都停下来让我选,烦。
