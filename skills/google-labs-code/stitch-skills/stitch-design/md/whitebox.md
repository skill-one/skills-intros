# stitch-design (`google-labs-code/stitch-skills/stitch-design`)

## whitebox

- 解析用户意图, 按工作流表路由到三条主路径之一: 新建设计 (text-to-design) / 编辑屏幕 (edit-design) / 生成 DESIGN.md (generate-design-md)
- 分析上下文: 确认当前 projectId (未知则调 list_projects), 并检查 .stitch/DESIGN.md 设计系统文档是否存在
- 增强提示词 (强制前置步骤): 查 references/design-mappings.md 将模糊表述替换为专业 UI/UX 术语, 再套入固定模板 (DESIGN SYSTEM: 平台/色板 hex/风格 + PAGE STRUCTURE: 页头/Hero/主内容/页脚)
- 调用 Stitch MCP 执行: 新建走 generate_screen_from_text, 编辑走 edit_screens, 提取走 get_screen
- 下载生成的 HTML 与截图到 .stitch/designs 目录, 并向用户呈现 outputComponents (AI 文字描述与建议)

- 提示词增强管线: 任何 Stitch 工具调用前必须执行的两步转换 — ①术语替换: 按映射表把 'Make a nice header' 这类模糊措辞改成 'Sticky navigation bar with glassmorphism' 级别的专业术语; ②结构化模板: 强制补齐设计系统字段 (平台/命名色板带 hex 值/圆角与阴影风格) 和编号页面结构, 缺一项都算不合规
- 设计系统一致性校验: 以 .stitch/DESIGN.md 作为 'source of truth', 其色彩/字体 tokens 被注入每次增强后的提示词, 确保新屏幕沿用既有视觉语言; 若该文件不存在则建议走 generate-design-md 工作流先补齐
- 外部依赖: 生成/编辑能力全部来自 Stitch MCP server (generate_screen_from_text / edit_screens / get_screen / list_projects / Download); 本地文件读写用 Read/Write 维护 .stitch/DESIGN.md; 迭代优化时优先用 edit_screens 做局部修改而非整屏重新生成
