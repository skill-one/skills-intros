# golang-samber-do (`samber/cc-skills-golang/golang-samber-do`)

## blackbox

**function**: 帮你把 Go 项目里「手工 new + 层层传参」的服务装配代码, 改造成用 samber/do 容器统一管理的写法 (注册、取用、启动/关闭、测试替身), 输出能直接编译运行的代码。

- input: 一个 Go 项目路径, main.go 里手工构造数据库、缓存、HTTP 服务再互相传递, output: 重构后的 Go 代码: 各服务注册进容器、按需取用, 可直接 go build 通过
- input: 提问:「三个服务要共用同一个数据库连接和日志器, 该怎么写?」, output: 一段可直接粘贴的 Go 示例: 注册一次、处处取用, 含必要的错误处理
- input: 代码或描述:「程序收到 Ctrl+C 退出时, 数据库连接和后台任务没被关闭」, output: 修正后的代码: 优雅关闭 (退出前逐个释放资源) 与健康检查
- input: 还在用旧版 samber/do (v1) 的代码, output: 迁移到 v2 的改写代码, 附新旧写法对照
