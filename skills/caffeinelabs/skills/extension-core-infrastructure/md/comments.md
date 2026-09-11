# extension-core-infrastructure (`caffeinelabs/skills/extension-core-infrastructure`)

## comments

- user: 前端新手, category: 坑, comment: 把 login() 写进表单 onSubmit, 弹窗直接报 'Signer window should not be opened outside of click handler'. 必须在按钮 onClick 里直接调.
- user: 做过 SaaS 的独立开发者, category: 妙用, comment: 接 Google 登录居然不用申请 key 也不用配 OAuth 客户端, login({provider:'google'}) 一行就通, 我以前自己接 OAuth 得折腾一整天.
- user: React 老手, category: 坑, comment: 我拿 isLoginSuccess 做登录门槛, 用户刷新页面后有会话却回到登录页. 它只在弹窗登录后为 true, 界面判断必须用 isAuthenticated.
- user: 企业内部工具开发, category: 注意, comment: 本地调试时前端校验拦下了 localhost:3000, SSO 死活登不上. 域名校验要放行 localhost/127.0.0.1 带端口, II 本身是认的.
- user: 后端老兵, category: 注意, comment: object-storage 是 peer dependency, 我只装了 core-infrastructure, 构建直接缺包报错. 记得把它也写进项目 package.json.
- user: 全栈独立开发, category: 妙用, comment: 登录后不用手动刷数据——useActor 随身份变化自动重建 actor 并把依赖查询失效重发, 我自己写的那套 refetch 逻辑全删了.
