# rust-best-practices (`apollographql/skills/rust-best-practices`)

## blackbox

**function**: 帮你写出地道、安全、高效的 Rust 代码：可以替你写新代码、检查和改进你已有的 Rust 代码，并解答相关编码问题。

- input: 贴一段能跑但写法笨重的 Rust 代码（比如到处 .clone()、用 unwrap()）, output: 改写后的代码 + 逐条说明哪里改了、为什么改
- input: 一个 Rust 项目的文件夹路径, output: 一份代码评审报告：按严重程度列出问题（错误处理、性能隐患、缺测试等）并附修改建议
- input: 一条编码问题，如「这个函数出错时该返回 Result 还是直接崩溃？」, output: 明确的建议 + 可直接粘贴使用的示例代码
