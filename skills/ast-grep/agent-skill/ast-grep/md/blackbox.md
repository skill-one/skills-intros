# ast-grep (`ast-grep/agent-skill/ast-grep`)

## blackbox

**function**: 你用大白话描述想找的代码长什么样, 我在代码库里精确找出所有符合的位置——能按代码结构查找, 所以连纯文字搜索找不到的规律 (比如「用了 await 却没套 try-catch 的函数」) 也能定位。

- input: 一句话描述 + 项目文件夹: 「找出这个项目里所有调用 console.log 的地方」, output: 一份匹配清单: 每条包含文件路径、行号和那行代码本身
- input: 描述一个结构规律: 「找出所有 async 函数中, 函数体内没有 try-catch 的」, output: 符合条件函数的列表, 带文件位置和函数代码片段
- input: 更挑剔的条件: 「找到所有调用了 fetch、但没检查返回结果的地方」, output: 逐条列出的匹配位置 (文件 + 代码行), 可直接逐个排查
