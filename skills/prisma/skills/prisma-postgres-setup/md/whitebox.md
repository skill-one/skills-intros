# prisma-postgres-setup (`prisma/skills/prisma-postgres-setup`)

## whitebox

- 认证: 依次从用户消息、环境变量/.env 找服务令牌, 都没有就引导用户去 Prisma Console 创建并粘贴回来。
- 调 Management API 拉取可用区域, 交互菜单让用户选部署地, 随后创建项目并同时开通数据库, 若状态为 provisioning 就轮询直至 ready。
- 配置本地工程: 安装 5 个依赖包, 把直连连接串追加写入 .env, 校正 .gitignore、schema.prisma 与 prisma.config.ts。
- 交互菜单让用户选定 schema 来源 (手写 / 博客示例 / 自然语言描述), 确认后运行 npx prisma migrate dev --name init, 一步生成迁移文件与客户端。
- 运行 test-connection.ts 做端到端连通验证, 成功后删除该脚本, 交付 Prisma Studio 与 Console 链接。

- REST 对接 Prisma Management API (https://api.prisma.io/v1/*): 全程 curl + Bearer 令牌, 解析 { data: {...} } 响应信封, 提取 proj_/db_ 前缀 ID 与 direct 连接串; 按错误码自纠 — 401 换令牌、404 查 ID 前缀、422 查请求体、429 退避重试。
- Prisma 7 约定强制落地: 连接 URL 只写 prisma.config.ts (经 dotenv 加载), schema.prisma 的 provider 必须是 "postgresql" 且不得含 url/directUrl; 客户端从 ./generated/prisma/client.js 导入, 用 pg.Pool + PrismaPg 适配器实例化, 禁用 datasourceUrl。
- 依赖与安全校验: 固定安装 prisma、@prisma/client、@prisma/adapter-pg、pg、dotenv 五个包 (缺一不可); .env 只追加不覆盖, 校验 .gitignore 已忽略 .env; 运行环境要求 Node.js 18+。
