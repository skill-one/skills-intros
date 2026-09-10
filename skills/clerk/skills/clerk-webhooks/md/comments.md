# clerk-webhooks (`clerk/skills/clerk-webhooks`)

## comments

- user: 第一次接 Clerk 的新手, category: 坑, comment: 本地验证一直 401, 查了半天签名, 其实是 middleware 把 /api/webhooks 拦了。在 clerkMiddleware 里把它设成公开路由就好。
- user: Express 老兵, category: 坑, comment: 全局挂 express.json() 后验签永远失败。webhook 那条路由必须单独用 express.raw({ type: 'application/json' }), 别让它碰解析过的 body。
- user: 独立开发全栈, category: 妙用, comment: Svix 失败会按计划重试, 我把请求头里的 svix-id 当幂等键, 先查库再写入, 重复事件直接返回 200, 用户表再没出过重复行。
- user: 刚上线的 SaaS 后端, category: 注意, comment: webhook 是异步最终送达, 不是即时的。『注册完马上从库里读这个新用户』这种同步流程会翻车, 刚建的数据请走 session token 或 Backend API。
- user: 自学转码的个人开发者, category: 坑, comment: 我只接了 user.created, 用户后来改邮箱, 库里还是旧地址, 邮件全发丢。created/updated/deleted 要一起处理, 改名换头像同理。
- user: 运维老哥, category: 注意, comment: clerk webhooks listen 打出的 relay URL 还得手动加进 Dashboard 当 endpoint, 不加事件一个都不来, 我空等了半小时才想明白。
