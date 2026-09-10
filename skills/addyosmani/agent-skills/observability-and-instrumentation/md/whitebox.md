# observability-and-instrumentation (`addyosmani/agent-skills/observability-and-instrumentation`)

## whitebox

- 先写下 2~4 个值班工程师会问的问题——没有问题定义就不埋点, 否则全是噪音
- 按每个问题选信号: 具体个案用结构化日志, 聚合频率/延迟用指标, 跨服务耗时用链路追踪
- 落地埋点: JSON 结构化日志 + 关联 ID 传播, 端点与外部依赖加 RED 指标, OpenTelemetry 自动插桩
- 添加基于症状的告警规则 (仅 page/ticket 两级), 每条挂最小 runbook
- 验证遥测本身: staging 强制触发错误用 requestId 定位, 试触发每条告警, 在追踪 UI 跟完一条请求无断链

- 结构化日志: 每行是带固定事件名的 JSON (如 payment_failed + errorCode 字段), 系统边界生成 request ID 并随每条日志/下游调用传播; 多入口共用一个日志源时打 entryPoint 字段; 字段走允许清单, 禁记密钥/token/完整 PII
- 指标: 每个端点和外部依赖上 RED (Rate/Errors/Duration), 延迟用直方图读 p95/p99 不看平均值; 标签只取小而固定集合 (route 模板、status_class、provider 名), 禁用 user_id/原始 URL/错误文本防基数爆炸; 示例用 prom-client, 供应商中立路径是 OpenTelemetry metrics API
- 分布式追踪: OpenTelemetry NodeSDK + getNodeAutoInstrumentations 自动覆盖 HTTP/gRPC/常见 DB 客户端 (近零代码, 需最先 import); 手动 span 只包内部工作单元 (如 chargeProvider), 上下文跨 HTTP 头/队列元数据传播; 默认低采样率, 错误尽量 100% 保留
