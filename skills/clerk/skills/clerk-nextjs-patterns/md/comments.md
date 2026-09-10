# clerk-nextjs-patterns (`clerk/skills/clerk-nextjs-patterns`)

## comments

- user: 第一次接 Next.js 的新手, category: 坑, comment: 写 `const { userId } = auth()` 后 userId 一直是 undefined，页面全显示未登录。排查半天，原来服务端必须 `await auth()`，漏了 await 还不报错。
- user: 全栈工程师, category: 坑, comment: 页面被 middleware 挡住了，API 路由却全裸奔——matcher 里漏了 `'/(api|trpc)(.*)'`，而且不报错，全靠自查才发现。
- user: 后端老兵, category: 注意, comment: 一开始鉴权失败我全返回 401，前端没法区分「去登录」和「找管理员」：未登录是 401，已登录无权限是 403，别混。
- user: 重度用缓存的全栈, category: 注意, comment: unstable_cache 的 key 里没放 userId，结果 A 用户刷出了 B 的数据。用户级缓存必须把 userId 拼进 key，这不是优化项是安全项。
- user: B2B SaaS 独立开发者, category: 妙用, comment: 用 `<Show when={{ feature: 'analytics' }}>` 做功能门禁，后来把该功能从 Pro 挪去 Team 套餐，后台改一下就行，代码一行没动、不用重新部署。
- user: 从 Core 2 升级的维护者, category: 启发, comment: 把 `!!userId` 换成 `isAuthenticated`、角色判断换成 `has({ permission })` 后，权限逻辑一眼能读懂，还顺手把散在各处的角色检查收敛了。
