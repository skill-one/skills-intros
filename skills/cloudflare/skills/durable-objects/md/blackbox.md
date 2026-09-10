# durable-objects (`cloudflare/skills/durable-objects`)

## blackbox

**function**: 帮你写出、修复或审查能在 Cloudflare 边缘上"记住状态、多人协同"的后端代码 (Durable Objects), 交付可直接部署的代码和配置。

- input: 一句需求描述, 如「做一个聊天室, 每个房间各自记住历史消息和在线的人」, output: 可直接部署的 TypeScript 代码 (Worker + Durable Object 类) + wrangler 配置文件, 复制进项目就能跑
- input: 一份你已写好的 Durable Object 代码或 wrangler 配置, output: 一份审查报告: 指出性能瓶颈、数据丢失风险等问题, 并给出修正后的代码
- input: 一段报错信息, 或「部署后状态总是丢/请求排队变慢」之类的现象描述, output: 定位到具体原因 (哪几行写法有问题) + 修好的代码
- input: 一个定时需求, 如「每个用户试用到期前 1 天自动发通知」, output: 基于闹钟 (alarm) 的实现代码: 到点自动触发, 重启也不会丢
