# brand (`nextlevelbuilder/ui-ux-pro-max-skill/brand`)

## whitebox

- 解析参数：从 $ARGUMENTS 取第一个词作为子命令 (update|review|create)，其余作为该子命令的参数。
- 按 Routing 规则加载对应的 references/{子命令}.md，作为本次任务的执行指南。
- 执行任务：调用 scripts/ 下的 .cjs 脚本，路径以 SKILL.md 所在目录为基准拼接，工作目录保持在项目根。
- 脚本以项目相对路径读写项目文件（如 docs/brand-guidelines.md、assets/design-tokens.json、src/）。
- update 流程末尾走同步链，并用 inject-brand-context.cjs --json 抽查前 20 行验证同步结果。

- 文件即真相 + 单向同步链：docs/brand-guidelines.md 是唯一 source of truth，sync-brand-to-tokens.cjs 把它转换为 assets/design-tokens.json（token 定义），再产出 design-tokens.css（CSS 变量），实现一次编辑、设计系统多端生效。
- 脚本化校验而非人工审查：validate-asset.cjs 检查资产的命名/尺寸/格式；extract-colors.cjs 从图片提取颜色并与品牌调色板比对（也可用 --palette 直接输出调色板）。
- 外部依赖：Node.js 运行时——所有工具脚本均为 .cjs，以 node 命令执行；inject-brand-context.cjs 提供 --json 输出，用于把品牌上下文注入 prompt 及同步后验证。文档本身不含任何模型 API 调用。
