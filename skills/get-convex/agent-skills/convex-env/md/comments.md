# convex-env (`get-convex/agent-skills/convex-env`)

## comments

- user: 后端老兵, category: 坑, comment: 我在 query 里写 process.env 读 key,线上一律 undefined。查了才知道只有 action 能读,查询/变更函数拿不到。
- user: 第一次用的新手, category: 坑, comment: 只在 dev 环境 set 了密钥,上线 prod 直接报 key 缺失。原来每个部署环境要各自 env set 一遍。
- user: 独立接单开发者, category: 妙用, comment: 换 API key 时只跑 npx convex env set,代码一行不动、不用重新部署,几分钟完成密钥轮换。
- user: 运维老哥, category: 注意, comment: 设完别急着走,用 npx convex env list 核对。key 名大小写打错它不报错,读的时候才 undefined。
- user: 开源项目维护者, category: 注意, comment: .env.local 只管本地,云端部署必须用 convex env set,别指望它跟着代码一起发布上去。
- user: 前端转全栈, category: 注意, comment: action 里要读环境变量且用 Node 内置库时,记得文件头加 'use node',默认 V8 环境会报错。
