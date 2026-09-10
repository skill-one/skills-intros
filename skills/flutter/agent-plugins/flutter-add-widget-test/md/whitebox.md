# flutter-add-widget-test (`flutter/agent-plugins/flutter-add-widget-test`)

## whitebox

- 前置配置: 确认 pubspec.yaml 的 dev_dependencies 含 flutter_test, 测试文件放 test/ 目录且以 _test.dart 结尾
- 定义并渲染: 用 testWidgets() 写测试, pumpWidget() 构建目标 widget (需要主题/方向数据时包一层 MaterialApp)
- 定位与断言: 用 expect(finder, matcher) 校验初始渲染, 再用 tap / enterText / drag 模拟用户交互
- 重建与复检: 普通交互后 pump() 重建一帧, 动画/异步场景用 pumpAndSettle() 等动画走完, 再 expect 校验更新后的 UI
- 运行闭环: 执行 flutter test test/xxx_test.dart, 按失败输出调整断言或 widget 逻辑, 重跑直到通过

- 定位-断言机制: Finder (find.text / find.byType / find.byKey) 在 widget 树中查找元素; Matcher (findsOneWidget / findsNothing / findsNWidgets / matchesGoldenFile) 校验其存在性与数量
- 帧泵机制: 静态渲染只 pumpWidget 一次即可断言; 状态变化靠 pump() 触发单帧重建; 动画/异步 UI 靠 pumpAndSettle() 循环泵帧直到没有待调度的帧
- 外部依赖: 全部能力来自 Flutter SDK 自带的 flutter_test 库与 flutter test 命令行, 不引第三方测试框架; 本技能运行在 models/gemini-3.1-pro-preview 上 (见 metadata)
