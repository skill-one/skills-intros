# golang-spf13-cobra (`samber/cc-skills-golang/golang-spf13-cobra`)

## blackbox

**function**: 🐍 用 Go 语言帮你开发命令行工具 (在终端敲命令运行的程序)——从零搭一个, 或给现有的加功能、修毛病。

- input: 一句话需求: "做一个 Go 命令行工具, 能 serve 启动服务、config 管理配置", output: 可直接 go build 运行的 Go 源码: 子命令、参数校验、清晰的报错和 --help 帮助信息齐全
- input: 一个已有的 Go CLI 项目目录, output: 增量代码修改: 新增的子命令/命令行选项/shell 自动补全/帮助文档, 风格与现有代码一致
- input: 一段行为不对的 Go CLI 代码 (如报错信息混乱、参数不检查、日志无法测试), output: 改好的代码 + 每处问题的一行说明 (按行业惯例逐条修正)
