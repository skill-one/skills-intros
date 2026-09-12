# dart-migrate-to-checks-package (`dart-lang/skills/dart-migrate-to-checks-package`)

## blackbox

**function**: 把 Dart 测试中旧的 expect 断言写法整体迁移到 package:checks 的新 check 写法,迁移后测试可正常编译和运行。

- input: 一个测试文件路径,如 test/api_test.dart(里面写满 expect(value, isTrue) 这类旧写法), output: 同一个文件被就地改写:断言全部换成 check(value).isTrue() 新写法,文件开头的 import 也一并更新,直接能跑
- input: 整个项目目录 + 一句「把测试迁到 package:checks」, output: pubspec.yaml 中加入 checks 依赖,项目下所有测试文件完成迁移,并跑过 dart analyze 和 dart test 确认通过;若有测试真的失败,会附上失败原因说明
- input: 一段旧断言代码,如 expect(items, [1, 2, 3]);, output: 对应的新写法 check(items).deepEquals([1, 2, 3]); ——特别注意会自动用 deepEquals 而不是 equals,避免列表/字典比较直接报错这个最常见的坑
- input: 一个旧写法的异步/报错断言,如 expect(failingCall(), throwsA(isA<StateError>()));, output: 改写为 await check(failingCall()).throws<StateError>(); 同步函数和异步 Future 各自用正确的对应写法,不会出现编译不过或假通过
