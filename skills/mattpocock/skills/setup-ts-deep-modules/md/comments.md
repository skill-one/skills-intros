# setup-ts-deep-modules (`mattpocock/skills/setup-ts-deep-modules`)

## comments

- user: 前端组长, category: 妙用, comment: 最值钱的是测试规则:tests 只许走入口点,连自己包的 lib/ 都不能 import。后来重构内部实现,测试零改动,那种跟着内部函数挂的脆测试绝迹了。
- user: 刚接手老仓库的新手, category: 坑, comment: 别跳过第 6 步:我装完没见到 fail 就收工,过俩月才发现 PACKAGES_ROOT 填错,检查根本没扫到我的包目录。必须亲眼看到 fail→还原→pass 才算装好。
- user: 后端老兵, category: 注意, comment: 它只管谁能 import 谁,不管分层:哪些包准依赖哪些包,配置里只留了注释占位让你自己填。想上 layer 规则的团队别指望开箱即得,接入后得自己补。
- user: monorepo 维护者, category: 妙用, comment: 公私按路径深度判定,不维护文件夹名单:新加 utils/、hooks/ 子目录自动就是私有的,加新包只是建个文件夹。我们 3 个包扩到 8 个,配置一行没改。
- user: 用 type:module 的独立开发者, category: 坑, comment: 我先自己手写 .dependency-cruiser.js,repo 是 type: module,一跑就报 module.exports 报错。换 .cjs 才好。别手写,直接用它给的模板。
- user: 三年前端, category: 启发, comment: 以前所有导出塞一个 index.ts,越滚越大没人敢动。它的思路是根目录每个文件都是入口,我拆成 index/client/server 三个小入口后清爽多了,新人一眼看懂门面。
