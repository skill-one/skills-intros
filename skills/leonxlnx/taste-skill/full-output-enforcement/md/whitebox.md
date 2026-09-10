# full-output-enforcement (`leonxlnx/taste-skill/full-output-enforcement`)

## whitebox

- 解析完整请求, 数清交付物数量 (文件/函数/章节/答案) 并锁定该数字
- 按锁定数量逐项全量生成, 不留占位符、不写骨架、不省略任何一段
- 输出前重读原始请求, 逐项比对交付物数量与完成度, 缺则当场补齐
- 扫描禁用模式 (占位注释、省略话术、缩水痕迹) 与代码可运行性, 全部通过后才输出

- 交付物计数锁定: 把请求拆成可数的交付物清单并锁定总数, 作为完整性的硬校验标准 (Cross-check 的比对依据)
- 禁用模式黑名单: 硬性封禁占位类输出 (`// ...`、`// TODO`、裸 `...`) 和省略话术 ('for brevity'、'and so on'、'similarly for the remaining' 等), 输出前逐一排查
- 长输出断点续写协议: 逼近 token 上限时不压缩、不跳到结论, 写到干净断点 (函数/文件/章节末尾) 即停, 输出 `[PAUSED — X of Y complete...]` 标记, 收到 'continue' 后从断点精确续写、不复述 | 全部机制均为纯输出约束协议, 不依赖任何外部工具、库或模型 API
