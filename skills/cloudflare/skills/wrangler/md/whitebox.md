# wrangler (`cloudflare/skills/wrangler`)

## whitebox

- 先查项目: 找出包管理器、本地 Wrangler 版本、package scripts、框架和当前使用的 Wrangler 配置文件
- 再取文档: 按任务抓取对应的 Cloudflare 官方文档页, 并用本地 wrangler --help 和 config-schema 核对语法——不凭记忆写命令
- 定目标: 改动前锁定账号、Worker、环境、资源; 数据操作先分清本地还是远程
- 应用变更: 优先编辑 wrangler.jsonc 源配置, 命令一律经项目 scripts/包管理器执行
- 验证并汇报: 用 wrangler types 重新生成类型、跑既有 typecheck/测试、deploy --dry-run; 最后报告改了什么、目标环境、已做检查和未解决缺口

- 本地版本优先: 所有命令通过项目 scripts 或包管理器执行, 绑定项目内已安装的 Wrangler; 需要新特性时明确指出必须升级, 不静默升级以迁就最新文档 (依赖: 项目内 wrangler 包)
- 语法现取现用: 命令/flag 查本地 wrangler --help 和官方命令参考, 配置字段查 node_modules 里的 wrangler/config-schema.json, 文档优先用 Cloudflare MCP docs 工具、否则直接抓官方链接页; 取不到文档就声明缺口, 不编造语法 (依赖: Cloudflare MCP docs 工具、wrangler 自带 help 与 schema)
- 变更安全阀: 加绑定前检查环境继承 (部分字段须逐环境单独声明); secret 值只走交互输入/文件/stdin, 不进命令参数、源码和日志; secret put/delete 视为立即部署的版本变更, 需分阶段时改用 wrangler versions secret 工作流
