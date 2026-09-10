# design-doc-mermaid (`spillwavesolutions/design-doc-mermaid/design-doc-mermaid`)

## whitebox

- 解析用户请求, 按决策树判定图表/文档类型 (activity, sequence, deployment, architecture, ER 等)
- 按需只加载匹配的专业指南与框架示例 (Spring Boot/FastAPI/React 等), 其余不读以省 token
- 基于指南模板生成 Mermaid 代码, 附 Unicode 语义符号与高对比度 classDef (必须带 color:)
- 执行 Resilient Workflow: 先存 .mmd 文件, 用 mmdc 校验, 通过后才写入 Markdown (未验证的图绝不进文档)
- 按目标平台交付: GitHub/GFM 用 fenced mermaid 代码块; Confluence/Notion/Word/PDF 额外渲染 PNG/SVG 并上传图片

- 意图路由: 关键词→指南映射表决定加载哪个 guide; GitHub wiki/GFM 下 classDiagram/erDiagram/stateDiagram-v2/C4 默认由本技能出图, 不转 PlantUML; PlantUML 仅对 Salt/use case/timing/ArchiMate/nwdiag/WBS 可选启用
- 校验与错误恢复: mmdc 验证失败时按优先级排查——references/guides/troubleshooting.md (28 类已知错误) → perplexity_ask MCP → brave_web_search MCP → gemini 技能 → WebSearch, 修复后重试
- Python 脚本工具链: resilient_diagram.py (存 .mmd+出图+校验+恢复 一条龙), extract_mermaid.py (从 Markdown 提取/校验图表, 或替换为图片引用), mermaid_to_image.py (mmd→PNG/SVG, 支持批量与自定义主题); 底层渲染依赖 mmdc (Mermaid CLI)
