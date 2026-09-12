# dart-collect-coverage (`dart-lang/skills/dart-collect-coverage`)

## comments

- user: 第一次配覆盖率的新手, category: 坑, comment: 我把 coverage 错加进了 dependencies, 发布包时多带出一堆生产依赖。要用 `dart pub add dev:coverage` 装到 dev_dependencies, 测试工具别混进生产依赖。
- user: Flutter 项目维护者, category: 妙用, comment: 自动生成的 .g.dart 一直把覆盖率拖得难看, 我在文件头加一行 `// coverage:ignore-file`, 报告立刻只反映手写代码的真实质量。
- user: monorepo 维护者, category: 注意, comment: workspace 里直接跑 `test_with_coverage` 只覆盖了根包, 两个子包全漏。要在命令后面跟上 `-- pkgs/a/test pkgs/b/test` 才收得全。
- user: CI 工程师, category: 妙用, comment: lcov.info 是通用格式, 我直接丢给 Codecov, PR 里就能行级标红未覆盖代码, 省得自己解析 coverage.json。
- user: 测试工程师, category: 注意, comment: ignore 注释一直不生效, 查了半天发现是手动流程的 format_coverage 没传 `--check-ignore`, 加上这个参数才会认 `// coverage:ignore-line`。
- user: 后端老兵, category: 坑, comment: 手动收集时我漏了 `--resume-isolates`, 测试跑完进程一直挂着不退出, 以为死锁重启了半天。加上这个参数才正常收尾。
