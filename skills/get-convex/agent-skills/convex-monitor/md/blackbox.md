# convex-monitor (`get-convex/agent-skills/convex-monitor`)

## blackbox

**function**: 盯着你的 Convex 应用 (一个后端云平台), 下一个报错、线上事故或功能需求一出现就立刻响应——修好它、排查它或把它做出来。

- input: 我的 Convex 项目文件夹路径, output: 开发中一出现新报错, 立刻收到: 报错的具体原因 + 已经修好的代码
- input: 已上线的云端应用 (需配置 Sentinel 监控), output: 生产环境一报错, 立刻收到: 这事严不严重的判断 + 修复方案
- input: 一句功能需求, 如「帮用户加导出 CSV」, output: 需求一出现, 直接交付做好的功能代码
- input: 设一个监听超时时长, 如 30 分钟, output: 期间什么都没发生时, 定时收到一声「一切安静」的汇报
