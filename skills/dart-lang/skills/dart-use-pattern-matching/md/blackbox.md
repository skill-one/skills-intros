# dart-use-pattern-matching (`dart-lang/skills/dart-use-pattern-matching`)

## blackbox

**function**: 把你手里写法过时或繁琐的 Dart 代码, 改写成用 switch 表达式和模式匹配的简洁版本。

- input: 一段用 if / else if 层层嵌套判断类型和取值的 Dart 代码, output: 改写后的 Dart 代码: 嵌套判断换成一条清晰的 switch 表达式, 缩短且语义更直白
- input: 一段解析 JSON 的 Dart 代码 (先手动检查字段存在, 再逐个取出), output: 改写后的 Dart 代码: 用一条模式同时校验结构和提取数据, 结构不符自动走失败分支
- input: 一段 switch 漏掉了某个子类型、编译报「未穷尽匹配」错误的 Dart 代码, output: 修复后的 Dart 代码: 补全所有缺失分支, `dart analyze` 不再报错
