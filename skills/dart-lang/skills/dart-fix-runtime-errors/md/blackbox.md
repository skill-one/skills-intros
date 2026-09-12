# dart-fix-runtime-errors (`dart-lang/skills/dart-fix-runtime-errors`)

## blackbox

**function**: 修复 Dart 代码里的类型、空值安全等编译报错，让代码通过检查、能正常运行。

- input: 一个报错的 Dart 项目目录（运行 dart analyze 一堆红色错误）, output: 改好的代码，再跑 dart analyze 不再报错
- input: 贴出一段报错信息，如「List<dynamic> can't be assigned to List<int>」, output: 修正后的代码片段 + 一句话说明改了哪里
- input: 一段空值报错的 Dart 代码，如「Non-nullable field must be initialized」, output: 补上空值处理后的完整代码，能通过编译和测试
