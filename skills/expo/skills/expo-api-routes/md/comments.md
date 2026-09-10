# expo-api-routes (`expo/skills/expo-api-routes`)

## comments

- user: 独立开发者, category: 妙用, comment: 不用单独搭后端了, App 和接口放一个仓库, eas deploy 一条命令全上线。第三方 key 藏在服务端, 反编译也扒不走。
- user: 前端转全栈新手, category: 坑, comment: 在 Expo Go 里 fetch('/api/hello') 一直 404。API 路由必须 npx expo serve 起本地服务才生效, 别在 Go 里白折腾半天。
- user: 后端老兵, category: 坑, comment: 顺手用 fs 读配置文件, 一部署就崩——底层是 Cloudflare Workers, 没有文件系统。配置改走环境变量, 数据走云数据库。
- user: 全栈接单党, category: 注意, comment: 本地 .env 配的 key 线上全是 undefined。生产环境要单独用 eas env:create 创建, 两边不互通, 上线前记得建好。
- user: 也维护 Web 端的, category: 注意, comment: 网页端调接口被浏览器跨域拦截, 手机端却正常。要自己加 OPTIONS 预检和 CORS 响应头, 不加网页端全挂。
- user: 玩过 Workers 的运维, category: 注意, comment: 在路由里跑视频转码, 本地没事, 线上 30 秒必超时。Workers 有 CPU 时间上限, 重活拆成多次请求或挪去别的服务。
