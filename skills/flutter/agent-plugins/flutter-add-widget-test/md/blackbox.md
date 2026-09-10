# flutter-add-widget-test (`flutter/agent-plugins/flutter-add-widget-test`)

## blackbox

**function**: 给 Flutter 手机应用的界面组件写自动化测试: 模拟用户点击、输入文字、滑动等操作, 自动核对界面显示是否正确, 跑一遍就能告诉你这个界面好没好。

- input: 一个 Flutter 界面组件的代码文件 (如 lib/todo_list.dart 待办清单页面), output: 配套的测试文件 (如 test/todo_list_test.dart), 在项目里运行测试命令后能看到通过 ✅ 或指出具体哪里不对 ❌
- input: 一句话需求, 如: 「测试在输入框输入商品名、点加号后, 列表要出现这条商品」, output: 完整可运行的测试代码, 打开后自动模拟输入和点击, 并核对列表里是否真的出现了那条商品
- input: 一个运行报错/跑不过的测试文件, output: 修正后的测试文件, 重新运行即可通过, 并说明之前为什么断言失败
