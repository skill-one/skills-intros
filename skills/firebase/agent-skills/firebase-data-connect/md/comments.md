# firebase-data-connect (`firebase/agent-skills/firebase-data-connect`)

## comments

- user: 第一次用的新手, category: 注意, comment: 产品改叫 SQL Connect 了, 但命令行还叫 dataconnect (init dataconnect、dataconnect:compile)。搜报错和教程用旧名才搜得到。
- user: 前端出身的全栈, category: 坑, comment: 改了表结构忘跑 sdk:generate, 前端拿着旧类型开发, 上线才发现字段对不上。现在 schema 一动就重新生成。
- user: 后端老兵, category: 妙用, comment: 不起模拟器也能自检: 跑一遍 dataconnect:compile, 查询和表对不上的地方直接报出来, 部署前全部过一遍。
- user: 做社交 App 的移动端开发, category: 注意, comment: 客户端查不到数据先别怀疑代码: 查询没写 @auth 等级就是默认拒绝。这里安全默认, 权限必须显式给。
- user: 独立开发者, category: 坑, comment: seed_data.gql 只在本地模拟器生效, 我以为部署后线上也有测试数据, 对着空表排查半天。线上灌数据用 Admin SDK。
- user: DBA 转型的, category: 启发, comment: 我本能想上裸 SQL, 但自动生成的查询自带类型检查; 只有 PostGIS、窗口函数这类真需求, 才值得退回裸 SQL。
