# pnpm (`antfu/skills/pnpm`)

## comments

- user: 第一次用的新手, category: 坑, comment: 我把镜像和代理设置写进 .npmrc，升级后全不生效——新配置要写在 pnpm-workspace.yaml，键名用 camelCase，.npmrc 只留认证信息。
- user: 从 yarn 迁来的前端, category: 启发, comment: 迁完 pnpm 构建报找不到模块，一查是代码用了没写进 package.json 的隐形依赖。补上声明后，再没出现过「我本地能跑」的扯皮。
- user: 运维老哥, category: 注意, comment: CI 里没加 --frozen-lockfile，lockfile 被顺手更新，线上和测试版本对不上。现在统一用 pnpm ci 加 store 缓存，流水线又快又稳。
- user: 后端老兵, category: 妙用, comment: 传递依赖有 bug 上游不修，我没 fork，直接在 overrides 里把它钉到修复版，一行配置解决，等上游发了新版再删。
- user: 开源库维护者, category: 注意, comment: pnpm 10 起默认不执行依赖包的安装脚本，我装 sharp 一直报二进制缺失，还以为断网了。把包名加进 allowBuilds 才好，升级依赖时记得重查一遍。
- user: 全栈独立开发, category: 妙用, comment: 十几个项目共享同一个 store，相同包只占一份磁盘。再设 minimumReleaseAge 为 7 天，自动跳过刚发布可能被投毒的版本，零成本安全感。
