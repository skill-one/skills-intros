# golang-design-patterns (`samber/cc-skills-golang/golang-design-patterns`)

## blackbox

**function**: 帮你把 Go 代码写得地道、健壮: 从 API/构造函数设计、架构选型, 到超时、重试、优雅退出这类生产级问题, 直接给出能用的代码或指出问题所在的审查报告。🏗

- input: 「我的 Server 结构体构造函数参数越来越多, 每加一个配置都要改所有调用方, 怎么设计?」, output: 改写后的 Go 代码: 一个 NewServer 加若干 WithXxx 配置函数, 新增配置不破坏旧代码, 默认值清晰可见, 附简短使用示例
- input: 一个 Go 项目的目录路径, output: 一份设计审查报告: 逐条列出隐患的具体文件和行号, 如藏在 init() 里的数据库连接、没设超时的外部调用、无上限的队列, 每条附改法
- input: 「我的 Go 服务按 Ctrl+C 后直接被强杀, 正在处理的请求全断了, 帮我修一下」, output: 修改后的代码: 收到退出信号后先停止接新请求、等在处理的请求做完、关闭数据库连接, 再正常退出
