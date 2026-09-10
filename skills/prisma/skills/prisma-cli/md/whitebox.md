# prisma-cli (`prisma/skills/prisma-cli`)

## whitebox

- 触发匹配: 用户消息命中 Prisma CLI 命令触发词 (prisma init / generate / migrate / db / studio / validate / format / debug / complete / mcp 等)
- 查表定位: 按命令类别表 (Setup / Generation / Database / Migrations / Utility) 找到对应分类, 从 Quick Reference 拿到命令用法
- 深入参考: 打开对应的 references/*.md 详细文档 (如 migrate-dev.md、agent-safety.md) 获取完整选项与最佳实践
- 给出命令: 输出正确命令与选项, 并附最新行为要点 (用 prisma.config.ts 配置、Bun 下加 --bun、schema 同步后需显式 prisma generate / db seed)
- 安全检查点: 涉及破坏性命令时, 先向用户说明确切的数据丢失影响并取得明确同意, 再读取 references/agent-safety.md 后执行

- 纯检索式参考系统: skill.md 本身是索引 + 快速参考表, 细节按需加载 Rule Files (references/*.md); 不依赖任何模型 API, 实际执行依赖本机安装的 Prisma CLI (v7.9.1)
- 边界消歧: 区分稳定的 ORM 命令 `prisma` 与公测的 Platform 包 `@prisma/cli` (二进制名为 prisma-cli), Compute/平台类需求分流到 prisma-compute 和 prisma-postgres, 避免用错命令
- AI 安全机制: 检测到 AI agent 时, 阻断 migrate reset、db push --force-reset、db push --accept-data-loss 等破坏性命令, 直到获得用户明确同意 (同意文本必须是用户原话, 经 PRISMA_USER_CONSENT_FOR_DANGEROUS_AI_ACTION 传入, 不得编造); 配置侧依赖 TypeScript 配置文件 prisma.config.ts + dotenv 显式加载环境变量
