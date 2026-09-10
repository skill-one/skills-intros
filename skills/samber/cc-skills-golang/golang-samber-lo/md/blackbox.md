# golang-samber-lo (`samber/cc-skills-golang/golang-samber-lo`)

## blackbox

**function**: 一个 Go 代码改写助手: 把你项目里冗长的循环代码改写成简洁、不容易出错的写法 (基于 samber/lo 工具库), 并帮你检查和修正这类代码的常见错误。

- input: 一个用多层 for 循环做筛选、分组、去重、汇总的 .go 文件路径, output: 逻辑完全不变的同一个文件, 循环被替换成一行行的简洁调用, 可直接编译通过
- input: 一个已经引入 samber/lo 的 Go 项目路径, output: 一份问题清单 + 修改后的代码, 比如「这处该用语言自带的标准库」「这里用并发版反而更慢」「生产代码里这个写法会崩溃」
- input: 一句话需求, 如「把订单列表按状态分组, 再算出每组总金额」, output: 可直接粘贴进项目的 Go 代码片段
