# workers-best-practices (`cloudflare/skills/workers-best-practices`)

## comments

- user: 后端老兵, category: 妙用, comment: 当上线前 checklist 用：把整段 Worker 代码丢给它 review，抓出模块级变量存请求状态的隐患——单测全绿、并发下才炸的那种，值。
- user: 第一次用的新手, category: 坑, comment: 直接让它凭空写 Worker，AI 按记忆用了旧 API，部署才报错。先让它跑 wrangler types、看项目实际版本再动手，一次就过。
- user: 安全工程师, category: 注意, comment: token 别用 === 直接比，有计时差异，按 Web Crypto 的比较写法来；随机 ID 用 crypto.randomUUID()，别用 Math.random()。
- user: 前端转全栈, category: 坑, comment: 在 handler 里发统计没 await，本地偶尔成、线上全丢——请求一结束后台活就没了。要么 await，要么挂 ctx.waitUntil()。
- user: 独立开发者, category: 妙用, comment: 原本脚本调 Cloudflare REST API 读写 KV，让它改成 binding 后少一层鉴权和网络开销，直接 env.KV 操作，代码短了一半。
- user: SRE 值班, category: 注意, comment: 以为 observability.enabled 一个开关就够，排障时发现 traces 是空的——traces.enabled 要单独设 true，上线前两项一起查。
