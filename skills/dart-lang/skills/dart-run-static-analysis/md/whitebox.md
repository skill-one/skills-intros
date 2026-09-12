# dart-run-static-analysis (`dart-lang/skills/dart-run-static-analysis`)

## whitebox

- 确认项目根目录存在 analysis_options.yaml, 作为全部分析行为的配置入口。
- 调用 analyze_files MCP 工具 (无则用 CLI `dart analyze <目录>`) 执行静态分析。
- 审阅诊断输出 (错误/警告/lint); 若 info 级也须视为失败, 追加 `--fatal-infos` 重跑。
- 错误人工修; 机械性 lint 转入自动修复: `dart fix --dry-run` 预览并确认, 再 `--apply` 落地。
- `dart format .` 格式化改动过的代码, 最后重跑分析验证诊断清零。

- 配置驱动: 分析行为完全由 analysis_options.yaml 决定 — include: 引入规则集 (如 package:flutter_lints/recommended.yaml), analyzer.language 开启 strict-casts/strict-inference/strict-raw-types 严格类型检查, linter.rules 逐条开关 lint 规则, formatter 节点控制 page_width 与 trailing_commas。
- 分层豁免: 误报或生成代码 (如 **/*.g.dart) 用 analyzer.exclude 的 glob 整体排除; 局部用行级 `// ignore:`、文件级 `// ignore_for_file:`、pubspec 内 `# ignore:` 抑制指定诊断, 插件诊断须带插件名前缀 (如 plugin/code)。
- 外部依赖: Dart SDK 自带 CLI 三件套 dart analyze / dart fix / dart format; 有 MCP 环境时对应 analyze_files / dart_fix / dart_format 工具; 承载模型为 models/gemini-3.1-pro-preview。
