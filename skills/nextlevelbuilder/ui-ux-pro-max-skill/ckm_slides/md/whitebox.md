# ckm:slides (`nextlevelbuilder/ui-ux-pro-max-skill/ckm:slides`)

## whitebox

- 从 $ARGUMENTS 的第一个词解析出子命令 (如 `create`)
- 按路由规则加载对应的 references/{子命令}.md 指南文件
- 带着剩余参数 (主题、页数) 执行该指南, 执行中查阅知识库参考文件 (布局模式、HTML 模板、文案公式、幻灯片策略)
- 产出战略型 HTML 演示文稿, 数据类幻灯片用 Chart.js 做可视化

- 路由分发: 子命令取自参数第一个词, 直接映射到 references/{subcommand}.md 文件, 其余参数传给执行环节; 路由是纯文件映射, 无代码逻辑
- 知识库按需加载: references/ 目录下四份 Markdown (layout-patterns / html-template / copywriting-formulas / slide-strategies) 分别承载布局模式、HTML 模板、文案公式、情境化幻灯片策略, 执行子命令时载入对应指南而非全部预载
- 输出技术栈: 产物为 HTML 演示文稿, 图表依赖外部库 Chart.js (JavaScript 图表库); 设计上声明使用 design tokens (设计令牌) 与响应式布局
