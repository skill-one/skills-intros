# golang-samber-slog (`samber/cc-skills-golang/golang-samber-slog`)

## blackbox

**function**: 帮 Go 项目搭好"日志流水线": 给我你的代码或需求, 我直接改好/写好日志相关代码——日志太多会自动抽样、用户隐私会自动打码、错误自动发到告警平台、每条 HTTP 请求自动记录。

- input: 一个 Go 项目的仓库路径, 里面日志代码写得到处都是、又乱又费钱, output: 改好的代码: 日志收敛成一条流水线——先抽样砍掉 90% 重复日志, 再抹掉用户手机号/IP 等隐私, 最后按级别分发
- input: 一句话需求: 「报错发到 Sentry 告警, 普通日志存到 Loki, 别让用户邮箱出现在日志里」, output: 一段可以直接跑的 Go 代码: 按「错误→Sentry、其余→Loki、邮箱字段自动掩码」接好的日志初始化 + 优雅关闭(防止最后一批日志丢失)
- input: 一个 Gin/Echo/Fiber 的 Web 服务路径, 说「线上日志被打爆了, /health 探活请求别记」, output: HTTP 中间件配置代码: 每个请求自动记录耗时/状态码, /health、/metrics 自动跳过, 4xx 记警告、5xx 记错误
