# golang-samber-oops (`samber/cc-skills-golang/golang-samber-oops`)

## blackbox

**function**: 把 Go 项目里"connection failed"这种没头没尾的报错, 升级为带上下文的结构化报错——出问题时能看到是哪层出错、哪个用户触发、完整调用栈, 不用再追问写代码的人。

- input: 一个 Go 源码文件路径, 比如 services/order.go, output: 改写后的同文件: 里面所有裸的 return err 都换成了带服务名、错误码、关键变量的报错, 可直接编译运行
- input: 一段代码或一句报错日志, 如「线上报 connection failed, 查不出是谁触发的」, output: 改好的代码 + 简短说明: 新报错会自动附带用户 ID、正在执行的 SQL、完整调用栈, 日志系统里能按类型归组
- input: 一个问题, 如「Go 程序 panic 了怎么不让整个进程崩掉?」, output: 可直接粘贴进项目的示例代码: panic 被自动转成带调用栈的普通报错, 程序继续跑
