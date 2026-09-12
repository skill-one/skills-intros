# dart-run-static-analysis (`dart-lang/skills/dart-run-static-analysis`)

## comments

- user: 第一次写Flutter的新手, category: 坑, comment: 没在 exclude 排除生成文件，analyze 被 *.g.dart 的警告刷屏，自己代码的问题全淹了。加上 **/*.g.dart 后一屏干净。
- user: 后端老兵, category: 妙用, comment: dart fix 先跑 --dry-run 预览再 apply：有次它要把弃用 API 全换新写法，和我的架构冲突，预览时直接拦下。
- user: CI流水线维护者, category: 注意, comment: 本地全过 CI 却挂，因为流水线加了 --fatal-infos 把 info 当错误。现在本地用同一条命令再提交，不再两面挨打。
- user: 团队Flutter组长, category: 启发, comment: 打开 strict-casts / strict-inference / strict-raw-types 后，以前上线才炸的 dynamic 隐患，analyze 一跑全提前冒头。
- user: 懒得清警告的开发, category: 坑, comment: 图省事写 ignore_for_file: type=lint 整文件静音，真 bug 也被埋了。改行级 // ignore: 只压确认无害的那条。
- user: 接手祖传项目的人, category: 妙用, comment: 祖传代码几百条警告别手动修：先 dart fix --apply 清掉机械问题，剩下的才值得逐条看，一下午能清完。
