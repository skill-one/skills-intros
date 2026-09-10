# flutter-implement-json-serialization (`flutter/agent-plugins/flutter-implement-json-serialization`)

## whitebox

- 用 http 包发出网络请求, 拿到响应。
- 校验状态码: 200/201 通过, 否则直接抛 Exception (绝不返回 null)。
- 用 dart:convert 的 jsonDecode 解码响应体, 并强制转换为 Map<String, dynamic> 或 List<dynamic>。
- 按数据量选解析策略: 小数据在主线程同步解析, 大数据 (>16ms) 用 compute() 丢到后台 isolate 解析。
- 把解码结果喂给模型的 fromJson 完成映射; 反向序列化走 toJson, 最后跑单元测试验证。

- 类型安全靠显式转换: jsonDecode 返回 dynamic, 必须强转为具体类型才交给模型, 保证类型安全、自动补全和编译期异常。
- fromJson 用 Dart 模式匹配 (switch pattern) 解构字段, 结构不符即抛 FormatException('Failed to load User.'); 失败一律抛异常而非返回 null。
- 依赖项: dart:convert (标准库, 负责编解码)、package:http (网络请求)、flutter/foundation 的 compute() (后台 isolate 解析大数据防 UI 卡顿), 外部模型 API 一律不用。
