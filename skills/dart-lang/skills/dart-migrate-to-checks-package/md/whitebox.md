# dart-migrate-to-checks-package (`dart-lang/skills/dart-migrate-to-checks-package`)

## whitebox

- 依赖准备: `dart pub add dev:checks`, 移除显式列出的 `package:matcher`。
- 用 grep 扫描 test/ 目录, 定位所有含 `expect`/`expectLater` 的测试文件并规划迁移范围。
- 改导入: `import 'package:test/test.dart'` 换成 `test/scaffolding.dart` + `checks/checks.dart`。
- 按映射表逐条改写断言: `expect(x, m)` → `check(x).m()`, 并套用防错规则 (集合用 deepEquals、reason→because 等)。
- 验证: `dart analyze` 查静态问题, `dart test` 跑测试确认通过。

- 映射表 + 坑位规则驱动的改写: 集合相等必须 `.deepEquals` (因 `.equals` 是严格 `==`); `reason:`→`because:`; `matches`→`matchesPattern(RegExp(...))`; `isA().having()`→`.isA().has()` 链; 同步 `.throws<E>()` 直接链式、异步必须 await + 回调。
- 编译器兜底验证: 增量迁移时临时保留 `import 'package:test/expect.dart'`, 全量迁完后删掉它, 残留 `expect` 会立刻变成编译错误, 便于逐个修完。
- 外部依赖: Dart 工具链 (`dart pub` / `dart analyze` / `dart test`)、shell grep; 库为 `package:checks` (自定义断言用 `package:checks/context.dart` 的 context.expect/nest 写成 Subject 扩展) 与 `package:test/scaffolding`; 执行模型为 models/gemini-3.1-pro-preview。
