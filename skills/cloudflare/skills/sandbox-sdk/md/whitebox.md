# sandbox-sdk (`cloudflare/skills/sandbox-sdk`)

## whitebox

- 任务命中技能场景 (AI 代码执行 / 代码解释器 / CI/CD / 运行不可信代码) 时被加载, 先执行 `npm install @cloudflare/sandbox` 和 `docker info` 验证安装与本地环境。
- 遵循「检索优先于记忆」: 实现任何功能前, 先 fetch 官方文档页或 GitHub 示例, 确认 API 现状。
- 按固定模板生成配置: wrangler.jsonc 三段结构 (containers / durable_objects / migrations) + Worker 入口再导出 Sandbox 类。
- 按 API 速查表写功能代码: getSandbox() 获取实例, exec() 跑命令, runCode() 跑 LLM 生成代码, readFile/writeFile 处理文件, exposePort() 暴露预览地址。
- 收尾对照反模式清单自检: 不漏 Sandbox 导出、不用内部客户端、不给多用户硬编码 sandbox ID、临时沙箱调用 destroy()。

- 检索偏置机制: 技能内置文档 URL 表 (docs / API Reference / Get Started / examples), 动手前先抓取对应页面而非凭预训练知识作答 — 外部依赖: Cloudflare 官方文档站与 github.com/cloudflare/sandbox-sdk 示例仓库。
- 精确配置契约: wrangler.jsonc 的 containers / durable_objects / migrations 三段是固定结构不可修改; Sandbox 本质是 Cloudflare Durable Object (同 ID 永远返回同一实例, 首次操作才惰性启动, 闲置 10 分钟休眠), Worker 缺少 `export { Sandbox }` 则部署失败。
- 执行双轨 + 容器底座: `exec()` 面向 shell/构建管线 (返回 stdout/stderr/exitCode), `runCode()` 面向 LLM 生成代码 (富输出, 同一 context 内状态延续, 支持 python/js/ts) — 代码运行在 Docker 镜像 docker.io/cloudflare/sandbox 内 (预装 Python 3.11 + Node.js 20), 本地开发硬依赖 Docker。
