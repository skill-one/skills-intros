# slides (`nextlevelbuilder/ui-ux-pro-max-skill/slides`)

## whitebox

- 解析 $ARGUMENTS, 取第一个词作为子命令 (目前仅支持 create)
- 加载对应知识库 references/{subcommand}.md, 即 references/create.md
- 用剩余参数执行, 参照 layout-patterns / html-template / copywriting-formulas / slide-strategies 四份参考文档
- 产出带数据可视化 (Chart.js)、设计令牌、响应式布局的策略型 HTML 演示文稿

- 路由分发: 子命令 = 参数第一个词, 一对一映射到 references/ 下的参考文档, 文档即执行指南, 无额外校验逻辑
- 知识库驱动生成: 版式、HTML 模板、文案公式、分页策略均来自参考文档; 图表依赖外部 JS 图表库 Chart.js 渲染
- 路径解析规则: 脚本路径以技能自身目录为基准 (同级技能用 ../<skill>/scripts/), 工作目录保持项目根; 脚本按项目根读写 docs/brand-guidelines.md、assets/design-tokens.json、src/ 等项目文件
