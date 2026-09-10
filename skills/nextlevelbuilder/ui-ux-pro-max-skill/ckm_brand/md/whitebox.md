# ckm:brand (`nextlevelbuilder/ui-ux-pro-max-skill/ckm:brand`)

## whitebox

- 解析 $ARGUMENTS 的第一个词作为 subcommand (如 update)
- 加载对应的 references/{subcommand}.md 作为本次执行的指南
- 带剩余参数执行: 按需调用 scripts/ 下的 node 脚本 (注入品牌上下文、同步 design tokens、校验资产、提取/比对颜色)
- update 主路径: 编辑 docs/brand-guidelines.md → sync-brand-to-tokens.cjs 同步到 assets/design-tokens.json 与 .css → 用 inject-brand-context.cjs --json 验证同步结果

- 字符串路由: $ARGUMENTS 首词 → references/{subcommand}.md 一对一映射, 首词之外的词作为参数透传; 参考文档 (references/) 与执行器 (scripts/) 解耦
- 单一事实源同步: docs/brand-guidelines.md (人可编辑的 Markdown) 经 sync-brand-to-tokens.cjs 生成 assets/design-tokens.json (token 定义) 和 design-tokens.css (CSS 变量), 并以 --json 注入输出做验证回路
- 外部依赖: 执行器全部是本地 Node.js (.cjs) 脚本, 经 node 运行 — inject-brand-context.cjs (提取品牌上下文供提示词注入)、validate-asset.cjs (校验资产命名/尺寸/格式)、extract-colors.cjs (从图片提取颜色并与色板比对); 全流程不涉及任何模型 API
