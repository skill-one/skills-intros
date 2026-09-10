# turborepo (`vercel/turborepo/turborepo`)

## blackbox

**function**: 当你把多个项目放在同一个仓库里开发时, 我帮你配置 Turborepo (让各项目自动按依赖顺序构建、结果可缓存复用的编排工具), 给出可直接粘贴的配置和命令, 并排查缓存不生效、构建太慢等问题。

- input: "我的 turbo 缓存一直不命中, 改一行代码所有包都重新构建" + 你的 turbo.json 内容, output: 一段排查结论 + 修好的 turbo.json (补上 outputs / env / inputs 的正确写法), 替换后缓存即可正常命中
- input: "仓库里有 apps/web 和 packages/ui, web 引用了 ui, build 该怎么配?", output: 三段可直接粘贴的配置: 各包 package.json 的 scripts、根目录 turbo.json、根 package.json —— 跑一条命令即可让 ui 先构建、web 后构建
- input: "CI 每次都全量构建太慢, 想只构建这次改动涉及的包", output: 一条命令 `turbo run build --affected` + 对应的 CI 配置片段, 只重建改动的包及其下游
