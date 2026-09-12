# dart-generate-test-mocks (`dart-lang/skills/dart-generate-test-mocks`)

## blackbox

**function**: 为依赖网络接口、数据库等外部服务的 Dart 代码编写单元测试——把真实服务换成假替身, 让测试不联网也能跑、瞬间出结果。

- input: 一个依赖网络请求的 Dart 类的代码 (如调用 API 取数据的服务类), output: 对应的单元测试文件: 用例覆盖成功、失败等场景, 不需要真实网络即可运行并通过
- input: 一段跑不过的测试代码 + 报错信息 (如 mock 抛空指针、参数对不上), output: 修好的测试代码, dart test 全部通过
- input: 一句描述: 「想验证 404 时我的类会抛异常」, output: 一条可直接运行的测试用例, 模拟 404 响应并断言异常被抛出
