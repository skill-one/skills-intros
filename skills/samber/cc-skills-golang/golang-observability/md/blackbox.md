# golang-observability (`samber/cc-skills-golang/golang-observability`)

## blackbox

**function**: 给你的 Go 服务补齐生产必备的观测能力——结构化日志、延迟/错误指标、分布式链路追踪、性能剖析、告警规则——让线上服务出问题时能看到、能定位。

- input: 一个没有任何监控的 Go HTTP 服务源码文件, output: 改好的同款 Go 代码:每个接口带 JSON 结构化日志、延迟和错误率指标、请求链路追踪
- input: 一个还在用 zap/logrus 打日志的 Go 项目目录, output: 一批迁移后的 .go 文件:旧日志全部换成标准库 slog,附迁移检查清单
- input: 一个完整的 Go 仓库 + 一句「帮我看看监控覆盖够不够」, output: 一份观测覆盖报告:哪些模块缺日志、缺指标、缺链路,各该补什么
