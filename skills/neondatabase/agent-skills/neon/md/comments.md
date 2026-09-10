# neon (`neondatabase/agent-skills/neon`)

## comments

- user: 第一次用的新手, category: 坑, comment: 对象存储、Functions、AI 网关都是公测,只在 us-east-2、eu-central-1 两个区可用。我先建了别的区的项目,只能删掉重建。用这些功能前先确认区域。
- user: 后端老兵, category: 坑, comment: 在 neon.ts 里写 process.env.KEY ?? "" 自以为兜底,结果空串传上去,线上这个 key 被覆盖删掉了。缺值就删掉这行,或确认 .env 里真有值再 deploy。
- user: 独立接活的前端, category: 妙用, comment: 给客户做 demo 不想注册账号,直接领了个免登录的临时 Postgres。注意认领码 15 分钟过期、项目 72 小时删——想留就用 neon claim 转正,数据不丢。
- user: 前端转全栈, category: 妙用, comment: 聊天室的 WebSocket 在 Vercel 函数上几十秒被掐,迁到 Neon Functions 最长能跑 24 小时,还挨着数据库。纯前端 SPA 可以直接当 REST 后端,开头记得自己验 JWT。
- user: 运维老哥, category: 注意, comment: 切分支时 checkout 会顺手把该分支的连接串写进本地 .env.local。同事合用环境、或脚本写死了连接串的话,切完分支连的库就变了,先知道这回事。
- user: 五人小队技术负责人, category: 启发, comment: 以前一个功能要克隆一套 staging 库,现在开分支测完就删,数据库第一次像 git 一样轻。顺手给 dev 前缀分支设了 7 天自动过期,忘删也不烧钱。
