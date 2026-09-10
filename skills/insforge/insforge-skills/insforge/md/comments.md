# insforge (`insforge/insforge-skills/insforge`)

## comments

- user: 前端转后端的新手, category: 坑, comment: insert({...}) 单对象直接报错, 排查半天, 原来必须传数组 insert([{...}])。新手必记。
- user: 独立开发者, category: 坑, comment: 首页用 setInterval 每 3 秒全量 select, 当月流量额度烧光。改成 realtime 订阅 + 只查需要的列 + limit 才止血。
- user: Next.js 全栈, category: 注意, comment: 差点把 admin 的 apiKey 塞进 NEXT_PUBLIC_ 变量——那是全库最高权限, 会暴露在浏览器里。admin 客户端只放服务端代码。
- user: 接私活的自由开发者, category: 坑, comment: 上传图片只把 url 存进了表, 要做删除才发现 delete 认的是 key。落库时 url 和 key 两个字段都要存, 别学我。
- user: 运维老哥, category: 妙用, comment: 服务器上原有的 aws cli 备份脚本一行没改, 把 endpoint 指到 InsForge 的 S3 兼容网关就跑通了。版本需 ≥2.0.9。
- user: 三人小团队技术负责人, category: 妙用, comment: 改表结构前先 branch create 开个分支随便折腾, 合并前 --dry-run 先审 SQL 再合。切分支后记得改 .env 并重启 dev server。
