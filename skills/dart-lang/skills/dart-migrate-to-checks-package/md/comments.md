# dart-migrate-to-checks-package (`dart-lang/skills/dart-migrate-to-checks-package`)

## comments

- user: 刚从 Java 转 Dart 的新手, category: 坑, comment: 把 expect(list, [1,2,3]) 直译成 .equals, 全挂。Dart 集合不重写 ==, 集合断言必须换 .deepEquals, 这是迁移第一大坑。
- user: 十年后端老兵, category: 妙用, comment: 先加 import 'package:test/expect.dart' 保旧测试能跑, 迁完一个文件就删这行, 没改的 expect 全变编译错误, 编译器就是我的迁移清单。
- user: 写异步流测试的工程师, category: 注意, comment: 同步闭包 throws 后面直接链断言, 异步必须 await check(f).throws<E>((it) => ...) 传回调, 异步后面接 .equals 编译不过, 白耗我半小时。
- user: 专职测试工程师, category: 坑, comment: matches(r'\d+') 直译成 .matchesPattern(r'\d+') 会把字符串当字面量, 永远匹配不上, 必须显式包一层 RegExp() 才行。
- user: 接手祖传代码的维护者, category: 启发, comment: 动手前先 grep having(、matches(、expect(.*, [ 统计数量, 工作量心里有数, 还能按重灾区排迁移顺序, 不用瞎摸。
- user: Flutter 独立开发者, category: 注意, comment: bool? 字段上调 .isTrue() 直接编译报错, 换成 .equals(true) 最省事, 或先 .isNotNull() 再链 isTrue()。
