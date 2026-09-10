# ckm:design (`nextlevelbuilder/ui-ux-pro-max-skill/ckm:design`)

## whitebox

- 解析用户任务, 按路由表 (references/design-routing.md) 分发到子技能: Logo / CIP / Slides / Banner / Social Photos / Icon, 或外部 brand / design-system / ui-styling
- 跑 Python 检索脚本 (scripts/logo|cip/search.py) 在本地风格/色板/行业/交付物库中匹配, 产出设计 brief (--design-brief / --cip-brief)
- 调用生成后端: Logo/CIP 走 Gemini 图像 API; Icon 由文本模型直接输出 SVG; Banner/社交图先写 HTML/CSS 再截图
- 渲染呈现: CIP mockup 转 HTML 展示页 (render-html.py), Slides 生成含 Chart.js 的 HTML 演示, Banner 按目标平台精确像素截图导出 PNG
- 视觉检查导出结果, 有问题修复后重导, 最后整理产物并向用户汇报 (Logo 生成后还会询问是否要 HTML 预览画廊)

- 两段式确定性检索: 先按任务关键词路由子技能, 再用 scripts/*/core.py 的 BM25 引擎在本地数据里匹配风格/颜色/行业/交付物并生成 prompt/brief —— 这一步纯文本匹配, 不调 AI
- 双轨生成后端: (a) 图像轨道 —— google-genai SDK 调 Gemini (需 GEMINI_API_KEY, pip install google-genai pillow): CIP 默认 gemini-2.5-flash-image, --model pro 用 gemini-3-pro-image-preview 换取 4K 文字清晰度; (b) 代码轨道 —— Icon 用 gemini-3.1-pro-preview 纯文本输出 SVG (SVG 本质是 XML 文本, 无需图像 API), Banner/社交图用 HTML+CSS 经 chrome-devtools/Playwright 截图 (2x deviceScaleFactor) 得到位图
- 硬规则 + 视觉复检闭环: Logo 强制白底输出; Banner 遵守安全区/文字占比 <20% (广告)/最少 2 字体/最小字号等规则, 印刷件 300 DPI+CMYK+出血; 导出图须用 Chrome MCP 目检, 布局问题修复后重导, 产物经 assets-organizing 技能归档
