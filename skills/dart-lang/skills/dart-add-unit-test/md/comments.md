# dart-add-unit-test (`dart-lang/skills/dart-add-unit-test`)

## comments

- user: 第一次写 Dart 测试的前端, category: 坑, comment: 文件名忘了加 _test.dart 后缀, 跑 dart test 显示 0 个测试, 我还以为全绿了。改成 utils_test.dart 才被识别, 新文件务必检查后缀。
- user: 被 CI 坑过的移动端开发, category: 注意, comment: 放 integration_test/ 里的测试默认不会被执行, 必须 dart test integration_test 显式指定路径。我之前一直显示通过, 其实压根没跑。
- user: 后端转 Flutter 的工程师, category: 坑, comment: 改了 @GenerateNiceMocks 注解后直接跑测试, 报错找不到新方法。要先执行 dart run build_runner build 重新生成 mocks 文件。
- user: 写过十年后端的老兵, category: 妙用, comment: verify(...).called(1) 不只看返回值, 还能验证调用次数和参数, 抓到一个接口被重复请求的 bug, 比只 assert 结果更狠。
- user: 从 Java 转 Dart 的新手, category: 妙用, comment: test 里直接 async/await 就行, runner 会自动等 Future 完成再判定结果, 不用额外包装, 异步用例写起来和同步一样短。
- user: 小团队技术负责人, category: 启发, comment: 照指南让 test/ 目录镜像 lib/ 结构后, 改哪个文件立刻知道去哪补测试, 团队新人也照这个约定放文件, review 少了很多来回。
