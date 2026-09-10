# convex-crons (`get-convex/agent-skills/convex-crons`)

## whitebox

- 在 convex/crons.ts 中调用 cronJobs() 创建调度器 (Convex 自带 API)。
- 按业务需要的间隔, 把定时任务指向 internal.* 内部函数, 绝不指向公开的 api.*。
- 编写任务处理器时保证幂等 (重复执行也安全), 且每次运行的工作量保持小。
- 到 Convex dashboard 的 schedule 页面确认任务已出现, 完成验证。

- 平台依赖: 完全构建在 Convex 平台上——用其 cronJobs() API 定义调度, 用其 dashboard 做最终校验, 不引入额外第三方库或外部模型 API。
- 安全边界机制: 强制只调度 internal.* 函数而非公开的 api.*, 使定时任务入口不暴露为可被外部调用的接口; 这是硬性规则, 不可协商。
- 可靠性设计机制: 幂等处理器 + 小批量单次运行来容忍重复触发; 频率上遵循『能用订阅推送的就不用紧凑轮询』, 避免无意义的密集轮询。
