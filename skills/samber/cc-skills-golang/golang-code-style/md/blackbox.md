# golang-code-style (`samber/cc-skills-golang/golang-code-style`)

## blackbox

**function**: 把 Go 代码改写得清晰易读——嵌套打平、分支精简、声明规范;也可以按同样标准帮你写新代码,或给整个项目做一次风格体检。

- input: 一个 .go 文件的路径, output: 逐条指出哪里写得绕(嵌套太深、if-else 拖沓、变量声明随意),并给出改好后的代码
- input: 整个项目的目录(里面有很多 Go 文件), output: 一份风格体检报告:按问题类型分门别类,每条附上具体文件位置和修改建议
- input: 「帮我写一个读取配置文件的 Go 函数」这类需求, output: 直接给出符合 Go 惯用写法的代码——错误处理前置、循环用 range、函数参数克制,拿来即用
