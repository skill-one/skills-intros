# dart-resolve-package-conflicts (`dart-lang/skills/dart-resolve-package-conflicts`)

## comments

- user: 第一次用 Dart 的新手, category: 坑, comment: 报版本冲突时我直接删了 pubspec.lock 重装,结果整个依赖树乱升,报错铺满屏幕。其实只删冲突包那一小段,再 pub get 就好了。
- user: CI 运维老哥, category: 妙用, comment: 在流水线里加 --enforce-lockfile,线上跑的版本和本地测试完全一致,再没出过「我这能跑」的扯皮。
- user: 维护祖传项目的老 Flutter, category: 妙用, comment: 撞上被官方撤回的包版本,降约束没用。lockfile 里只删那个包的条目,pub get 自动拉到最新可用版。
- user: 后端老兵, category: 注意, comment: pub outdated 里 Upgradable 和 Resolvable 是两回事:前者不用改 yaml,后者要手动改版本号,先分清再动手。
- user: 独立开发者, category: 启发, comment: 养成每月跑一次 pub outdated 的习惯,小步升级比半年攒一次大升好修多了,breaking change 一个个过。
- user: 带三个人的技术组长, category: 注意, comment: pub upgrade 完别急着提交,先跑 analyze 和 test,新版包常换 API 名,直接提交上线才炸。
