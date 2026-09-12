# dart-build-cli-app (`dart-lang/skills/dart-build-cli-app`)

## blackbox

**function**: 把你的一个想法变成能在终端里敲命令运行的小工具, 最后交付成单个可执行文件, 拷到别的电脑不用装任何东西就能跑。

- input: 一句话需求, 如「做个统计文件夹里各类文件数量的命令」, output: 一个终端命令, 如 `filecount ~/Downloads`, 敲下即出统计结果; 参数敲错时显示清晰的用法提示, 而不是一屏报错
- input: 一个已有的命令行工具项目 + 「加一个 export 子命令」, output: 更新后的项目: 新命令可用, `help export` 有清楚说明, 且附带自动化测试, 跑一遍即可证明各项功能正常
- input: 一个开发完成的命令行工具项目, output: 编译好的独立可执行文件 (如 `mytool.exe`、`mytool-linux`), 双击或在命令行直接运行; 也可按需交付 Linux、ARM 等不同系统的版本
