# extension-oql (`caffeinelabs/skills/extension-oql`)

## comments

- user: 前端转 Motoko 的新手, category: 坑, comment: 编译报 field payload does not exist 别换包版本,是文件顶部缺 import Entity "mo:caffeineai-oql/Entity",补上就好,跟包版本无关。
- user: 接手遗留项目的自由职业者, category: 坑, comment: 上线后 schema 一直返回 fields: [],查半天是集合还没数据、又没人调 .sample。给每个 entity 补上假数据模板,schema 才正常出来。
- user: 独立 SaaS 开发者, category: 妙用, comment: orders 和 products 各建一个 entity、.edge 连上后,直接问 agent「上月销量前十」就能出结果,一行 join 代码没写,报表后台都省了。
- user: 十年后端老兵, category: 妙用, comment: .ownedByWith 的闭包能读 actor 状态,「管理员看全部、普通用户只看自己的」一个函数搞定,不用在每条查询路径里重复权限过滤。
- user: 安全工程师, category: 注意, comment: .edge 指向别的 canister 的实体不会报错,但那列会从 schema 里静默消失,前端再也发现不了它。跨服务外键就老老实实当普通字段存。
- user: 社交 App 全栈创始人, category: 注意, comment: 私信表一开始用 .scopedPerUser,结果 agent 连我自己的跨用户问题都答不了——它也被挡。要能汇总又保护隐私,得换 .controllerOrScoped。
