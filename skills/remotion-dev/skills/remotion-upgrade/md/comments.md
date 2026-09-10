# remotion-upgrade (`remotion-dev/skills/remotion-upgrade`)

## comments

- user: 独立开发者, category: 坑, comment: 只升了 remotion 主包，漏了 @remotion/player，运行直接报版本不一致。所有 @remotion/* 包必须升到同一个精确版本，一个不能漏。
- user: 第一次升级的新手, category: 注意, comment: 项目里有 @remotion/cli 就直接 npx remotion upgrade，一条命令连本地 remotion 技能包也一起更了。我先手动改 package.json，白折腾。
- user: 全栈老兵, category: 注意, comment: zod、mediabunny 这类辅助包别随手更到最新，先用 npm view @remotion/studio@目标版本 dependencies 查清单再对齐，否则会依赖冲突。
- user: CI 运维老哥, category: 坑, comment: 手动改完 package.json 忘跑包管理器刷 lockfile，CI 装的还是旧版。改完必须让 npm/pnpm 重新算锁文件，再对着 diff 核一遍。
- user: 视频工作室技术负责人, category: 妙用, comment: 升完顺手跑 npx remotion versions，一眼揪出一个停在旧版的包；再去 GitHub releases 页抄 changelog，给团队写升级说明很省事。
- user: monorepo 维护者, category: 妙用, comment: pnpm workspace 里 remotion 包散在三个子包，这流程先扫全仓库 manifest 和 lockfile 再动手，我无关的依赖一个没动，diff 很干净。
