# dart-add-unit-test (`dart-lang/skills/dart-add-unit-test`)

## blackbox

**function**: 给你的 Dart/Flutter 代码补写单元测试, 交付开箱即跑、能防止以后改坏功能的测试文件。

- input: 一个 Dart 源文件路径 (如 lib/utils.dart, 里面是普通函数或类), output: 配套的测试文件 (如 test/utils_test.dart), 覆盖正常值、边界值和异常情况, 你运行 dart test 就能看到全部通过 ✅
- input: 一段依赖网络请求或数据库的 Dart/Flutter 代码, output: 带假数据替身 (mock) 的测试, 不联网、不连真数据库也能跑, 并确认代码确实调用了该调的接口
- input: 一段有 bug 的代码 + 一句 bug 描述 (如「金额相加结果不对」), output: 能复现这个 bug 的回归测试: 修复前运行必失败, 你改好后运行变绿, 以后这个 bug 不会再悄悄回来
