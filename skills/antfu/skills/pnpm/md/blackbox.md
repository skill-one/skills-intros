# pnpm (`antfu/skills/pnpm`)

## blackbox

**function**: 帮你解决 pnpm (Node.js 项目装包/管依赖的工具) 相关的一切问题:写命令、配 monorepo、修报错、迁移。

- input: 一段报错,如 pnpm install 后提示 ERR_PNPM_NO_MATCHING_VERSION, output: 原因说明 + 可直接复制执行的解决命令
- input: 「我有 3 个子项目放在一个仓库里,想用 pnpm 统一管理」, output: 写好的 pnpm-workspace.yaml 配置 + 要执行的命令,可直接放进项目用
- input: 「我的项目原来用 npm,想换 pnpm,装包后有些包找不到怎么办」, output: 逐步迁移清单:该删的文件、命令对照表、以及「幽灵依赖」问题的修复写法
