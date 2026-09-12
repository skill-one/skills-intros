# dart-build-cli-app (`dart-lang/skills/dart-build-cli-app`)

## whitebox

- 初始化: 用 `dart create -t cli` 脚手架项目, 入口 main() 放 bin/, 实现逻辑放 lib/src/
- 解析参数: 引入 args 包, 简单脚本用 ArgParser 定义 flag/option, 多命令 (类似 git) 用 CommandRunner + Command 子类路由
- 执行逻辑: 用 stack_trace 的 Chain.capture() 包裹运行, 失败时向 stderr 输出可读错误并返回非零退出码 (io 包的 ExitCode 枚举)
- 测试验证: 用 test_process 起真实子进程跑 CLI, test_descriptor 构造/校验文件系统状态, StreamQueue 断言 stdout/stderr 和退出码, 并跑 `dart run bin/cli.dart help <cmd>` 核对帮助文本
- 编译分发: 开发期 `dart run` 快速迭代, 发布期 `dart compile exe` 打成单文件原生可执行 (需要时加 --target-os/--target-arch 交叉编译 Linux)

- 参数解析与路由: 全靠 args 包 (ArgParser / CommandRunner), 非法参数捕获 UsageException 后展示自动生成的帮助文本并以退出码 64 结束
- 错误处理: stack_trace 的 Chain.capture 追踪异步调用链, Chain.terse 剥离核心库噪音帧; 底层异常不吞、向上冒泡, 保证失败 = 明确错误信息 + 非零退出码
- 质量门禁: 发布前跑 `dart format . --set-exit-if-changed` (格式违规即退出码 1) → `dart analyze` → `dart test`; 命令级功能强制集成测试, 依赖 Dart SDK 及 args / io / stack_trace / test_process / test_descriptor 这些库
