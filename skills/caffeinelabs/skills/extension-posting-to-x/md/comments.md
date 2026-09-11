# extension-posting-to-x (`caffeinelabs/skills/extension-posting-to-x`)

## comments

- user: 第一次接 Caffeine 的新手, category: 坑, comment: 我没先接登录就部署发推, 所有请求都被匿名身份拒掉, 查了一晚上才发现令牌只能挂在已登录用户名下。先把登录流程跑通, 再接发推, 顺序不能反。
- user: 做过第三方登录的全栈, category: 注意, comment: 四个授权 scope 少一个也能走完授权页, 静默不报错, 直到真发推那一刻才失败。我漏了 tweet.write, 白排查一下午。上线前照清单逐项核对。
- user: 运维老哥, category: 坑, comment: 我漏配 is_replicated, 每条推文被复制成全节点并发请求, 用户限额当天烧光, 账单翻了十几倍。这个开关必须显式关掉, 别赌默认值。
- user: 修过线上掉线的独立开发者, category: 坑, comment: 刷新令牌每次刷新都会换新, 我只更新了访问令牌, 旧刷新令牌立刻作废, 用户约两小时集体掉线。刷新后必须把新的一对一起写回存储。
- user: 多租户 SaaS 后端, category: 妙用, comment: 默认所有用户共享管理员应用的发推限额, 高峰互相挤兑。我改成 fallback 模式: 管理员设默认值兜底, 重度用户填自己的 Client ID, 限额互不抢占。
- user: 安全评审工程师, category: 启发, comment: 这套令牌全程不出后端, 前端只能查到「是否已连接」。我以前把第三方令牌存在浏览器里, 这个边界设计值得照搬到其他平台集成。
