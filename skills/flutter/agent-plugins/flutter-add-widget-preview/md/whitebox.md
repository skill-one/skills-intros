# flutter-add-widget-preview (`flutter/agent-plugins/flutter-add-widget-preview`)

## whitebox

- 定位可预览目标: 找无必需参数、返回 Widget/WidgetBuilder 的顶层函数、类静态方法或公开构造函数
- 加注解: 导入 package:flutter/widget_previews.dart, 给目标加 @Preview 并配置 name/group/size/theme/brightness 等参数
- 多组件复用同一配置时, 抽取为继承 Preview/MultiPreview 的自定义注解类
- 启动预览器: 受支持的 IDE 自动运行 'Flutter Widget Preview' 面板, 或命令行 flutter widget-preview start 打开 Chrome
- 热重载迭代: 改代码自动更新; 改了全局状态点全局热重启, 只动局部点单卡片热重启, 按控制台报错修复后重复

- 注解驱动的代码生成: 预览由 @Preview 注解标注并经代码生成实现, 因此注解里引用的回调必须公开且为常量, 否则生成不通过 (依赖 Flutter SDK 的 widget_previews.dart)
- Web 沙箱运行: 预览器跑在 Web 环境 (IDE 内嵌或 Chrome), 禁用 dart:io/dart:ffi 原生 API, 传递依赖需条件导入绕开; 资产须用包路径 packages/xxx/assets/...; 无约束组件默认压到约半视口, 需用 size 显式定尺寸
- 运行时 transform(): 自定义 Preview/MultiPreview 重写 transform() 可动态改写预览配置 (动态拼名称、动态选主题), 补足 const 注解做不到的事; 本技能元数据标注运行模型为 models/gemini-3.1-pro-preview
