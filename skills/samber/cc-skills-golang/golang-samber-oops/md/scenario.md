# golang-samber-oops (`samber/cc-skills-golang/golang-samber-oops`)

## scenario

凌晨3点告警响起, 日志里只有一句"connection failed"——哪个用户? 哪个接口? 一无所知, 只能逐层翻代码. 我用 samber/oops 给 Go 错误加上下文: 用户ID、调用栈、错误码、给用户看的提示, 一条错误日志即可定位, 无需再问开发.
