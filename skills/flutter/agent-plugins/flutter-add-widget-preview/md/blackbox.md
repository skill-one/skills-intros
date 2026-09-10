# flutter-add-widget-preview (`flutter/agent-plugins/flutter-add-widget-preview`)

## blackbox

**function**: 给 Flutter 项目的 UI 组件加上「实时预览」能力——不用启动整个 App，在 IDE 侧边栏里就能直接看到每个按钮、卡片、页面的真实长相，还能点按交互。 📱

- input: 一个 Flutter 组件文件，如 lib/widgets/login_form.dart, output: 同一个文件被修改：新增了带 @Preview 标记的预览函数，打开 IDE 的 "Flutter Widget Preview" 面板即可看到登录表单的实时画面，改代码即时刷新
- input: 一句需求："帮我新建一个商品卡片组件", output: 可直接使用的 Dart 组件代码 + 自带预览标记，保存后预览面板自动出现浅色 / 深色两种模式各一张卡片
- input: 一段加预览后报错的 Dart 代码（如用到了 dart:io 这类浏览器环境跑不了的接口）, output: 修复后的代码：预览里跑不了的部分被绕开，预览面板恢复正常显示，并在注释里说明改了哪里
