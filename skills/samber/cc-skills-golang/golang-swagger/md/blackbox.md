# golang-swagger (`samber/cc-skills-golang/golang-swagger`)

## blackbox

**function**: 给 Go 语言的 Web 项目补上并自动生成 API 文档：打开浏览器就能看到所有接口的参数、返回值，还能直接在网页上试调接口。

- input: 一个 Go Web 项目的文件夹路径, output: 项目里的接口被补全了文档说明，并生成一份浏览器可打开的 API 文档页面（如 /swagger/index.html），能在页面上直接发请求调试
- input: 一段写好的 Go 接口处理函数代码, output: 同一段代码，上方加好了完整的文档注释：接口用途、每个参数的含义和类型、各种返回结果、是否需要登录
- input: 一个已有文档的 Go 项目 + 「帮我检查文档」, output: 一份问题清单：哪些接口没写文档、参数描述缺失、返回值没标、需要登录的接口没加锁等
