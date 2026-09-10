# firebase-hosting-basics (`firebase/agent-skills/firebase-hosting-basics`)

## comments

- user: 第一次部署网站的新手, category: 坑, comment: 我拿 Next.js 项目部署,线上一直白屏,后来才明白 Hosting 只管静态和 SPA,要服务端渲染得用 App Hosting。
- user: 接私活的独立开发者, category: 妙用, comment: 给客户演示前先 `hosting:channel:deploy staging` 开个临时预览链接,改稿不碰正式站,定稿再正式发布,省心。
- user: React 初学者, category: 坑, comment: 部署后刷新子页面就 404,在 firebase.json 的 rewrites 里把所有路径指回 /index.html 后就好了,SPA 必配。
- user: 运维老哥, category: 注意, comment: 上线前先跑 emulators:start 在 localhost:5000 本地验证,firebase.json 写错当场能发现,不浪费一次线上发布去试。
- user: 前端转全栈, category: 注意, comment: init 默认发布目录是 public/,我的打包产物在 dist/,没改字段就部署,线上全 404,发之前一定核对 public 路径。
- user: 个人博客站长, category: 启发, comment: 以前攒一堆改动怕传错不敢发,现在有预览通道和版本回滚兜底,我改成小步快发,改完几分钟就能让读者看到。
