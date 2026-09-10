# firebase-auth-basics (`firebase/agent-skills/firebase-auth-basics`)

## comments

- user: 第一次用的新手, category: 坑, comment: Google 弹窗一闪就没,报 unauthorized-domain。原因是我把 http://localhost:9090 填进了授权域名,只留 localhost 就好,不能带协议和端口。
- user: 独立前端开发, category: 注意, comment: 改完 firebase.json 的 auth 配置以为就生效了,还是登不上——必须再跑一次 deploy --only auth 部署到后端,这步千万别省。
- user: 赶demo的全栈, category: 妙用, comment: 先让用户匿名登录逛 App,要下单时再绑定邮箱转正式账号,购物车一点不丢。试用门槛直接降到零,转化率肉眼可见地涨。
- user: 后端老兵, category: 注意, comment: ID Token 只有 1 小时寿命,别在服务端长期缓存,过期就用 Refresh Token 换新,不然用户登录一小时后集体请求被拒。
- user: 运维老哥, category: 妙用, comment: CLI 不用全局装,npx -y firebase-tools@latest 用完即走,CI 机器和同事环境零污染,还永远跑最新版。
- user: 刚接手老项目的前端, category: 启发, comment: 以前以为开了登录数据就安全,其实还得在规则里用 request.auth 限定只能读写自己的数据,不然绕过客户端照样裸奔。
