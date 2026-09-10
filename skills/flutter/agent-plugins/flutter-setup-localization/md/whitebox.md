# flutter-setup-localization (`flutter/agent-plugins/flutter-setup-localization`)

## whitebox

- 1. 依赖注入: 执行 flutter pub add 引入 flutter_localizations 与 intl, 写入 pubspec.yaml
- 2. 开启生成开关: 在 pubspec.yaml 的 flutter 段设置 generate: true
- 3. 建 l10n.yaml: 在项目根目录声明 .arb 目录、模板文件 (app_en.arb) 与输出文件名
- 4. 触发生成: 编写各语言 .arb 文件后运行 flutter pub get, 自动产出 AppLocalizations 类
- 5. 接线使用: MaterialApp 注入 localizationsDelegates 与 supportedLocales, 界面里用 AppLocalizations.of(context) 取字符串

- ARB 单一事实源: 以 app_en.arb 为模板 (@key 元数据携带 description/placeholders), 其他语言文件按同名 key 补齐译文
- 代码生成 + 校验闭环: generate: true 使 flutter pub get 触发编译, 生成类型安全的 AppLocalizations; 出错则按终端报错修 ARB 语法 (缺逗号/占位符不匹配) 后重跑
- ICU 风格高级格式: 在 ARB 内用 {} 占位符、{count, plural, ...} 复数、{gender, select, ...} 条件选择, 由生成器转为强类型方法调用; 外部依赖: flutter_localizations 与 intl 包、Flutter CLI
