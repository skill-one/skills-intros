# golang-uber-fx (`samber/cc-skills-golang/golang-uber-fx`)

## scenario

你的 Go 服务越写越大:main 塞满初始化,启动顺序靠猜,停机时连接没关、请求被硬掐,一重启就出事。🏭 我用 uber-go/fx(依赖装配框架)把「谁先启动、如何干净退出」统一交给框架管理,服务稳了。
