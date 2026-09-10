# durable-objects (`cloudflare/skills/durable-objects`)

## whitebox

- 识别任务类型: 新建 DO 类 / RPC、alarm、WebSocket 处理 / 代码审查 / wrangler 配置 / 测试 / 分片设计
- 抓取 Cloudflare 官方文档 (docs、API 参考、best practices、examples) —— 因为内置 API 知识可能过期, 检索优先于记忆
- 按协调原子建模: 每个聊天室/游戏/用户一个 DO 实例, 用 getByName() 做确定性路由
- 按核心规则实现: SQLite 存储 + RPC 方法 + 先写存储再更新内存, 构造器中仅用 blockConcurrencyWhile() 建表
- 对照反模式黑名单自查 (如禁止单一全局 DO); 若涉及测试, 先读 testing 参考再写用例

- 检索优先: 实现 API 前先 fetch developers.cloudflare.com 对应页面, 按关键词搜索 (blockConcurrencyWhile, idFromName, getByName, setAlarm, sql.exec); 内部参考文件 references/rules.md、workers.md 补充规则与 Worker 配置知识
- 协调原子建模: 单实例 = 单线程强一致, 拒绝全局单例 DO (瓶颈); 存储用 SQLite 同步 sql.exec (迁移中配置 new_sqlite_classes), 调度用每实例仅一个的 alarm (setAlarm 会覆盖旧闹钟)
- 规则门禁 + 测试前置: 产出代码须通过 Critical Rules / Anti-Patterns 清单 (不在相关写入间 await 以保原子性, 不跨外部 I/O 持有 blockConcurrencyWhile); 测试基于 Cloudflare 官方 Vitest 集成, 写之前强制先查 references/testing.md 确定当前配置方式
