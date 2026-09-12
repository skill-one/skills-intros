# dotnet-best-practices (`github/awesome-copilot/dotnet-best-practices`)

## blackbox

**function**: 检查并改进你的 C# (.NET 项目常用的编程语言) 代码, 让它符合规范: 加注释、修隐患、补测试, 交付可直接使用的代码和检查报告。

- input: 一个 .cs 代码文件的路径 (如 UserService.cs), output: 改进后的同名代码文件: 公开方法都带说明注释、错误处理更严谨、资源正确释放, 并附一段「改了什么、为什么改」的说明
- input: 整个 C# 项目的文件夹路径, output: 一份体检报告: 按条列出哪里不符合规范 (如缺少参数校验、异步用法不当、日志混乱), 每条附修改建议和示例代码
- input: 粘贴在对话里的一段 C# 代码, output: 逐条点评: 指出问题 → 给出改好的代码片段 → 说明改动理由, 可直接复制替换
