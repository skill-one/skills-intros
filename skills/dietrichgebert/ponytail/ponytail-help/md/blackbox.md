# ponytail-help (`dietrichgebert/ponytail/ponytail-help`)

## blackbox

**function**: 给写代码的我装上一个「反过度设计」开关: 你要什么我就造什么, 但永远给你最简单能用的方案, 并主动指出哪里的代码是多余的、该删。

- input: 输入 /ponytail, 再说一句需求, 比如「帮我写个配置读取模块」, output: 一段能直接跑的最简代码, 结尾附一句偷懒建议, 如「其实 Python 自带的 configparser 就够, 以上 40 行可以全删」
- input: 输入 /ponytail-review + 一个代码文件路径, output: 逐条列出过度设计的位置和改法, 如「第 42 行: 工厂模式却只有一个产品, 直接内联成一行函数调用」
- input: 输入 /ponytail-audit + 项目文件夹路径, output: 一份按优先级排序的「该删清单」: 哪些抽象层、配置项、没人调用的代码可以整体删掉
- input: 输入 /ponytail-debt, output: 把代码里留的 ponytail: 快捷备注汇总成一张待办清单, 标明每处在哪个文件哪一行
- input: 输入 stop ponytail 或 normal mode, output: 恢复普通模式; 之后随时说 /ponytail 可再打开
