# design (`nextlevelbuilder/ui-ux-pro-max-skill/design`)

## whitebox

- 按任务类型查 Sub-skill Routing 表路由: logo/CIP/slides/banner/social photos/icon (内置) 或 brand/design-system/ui-styling (外部子技能)
- 生成设计简报: 调 scripts/{logo,cip}/search.py 用 BM25 匹配用户描述; banner/social photos 先用 AskUserQuestion 确认用途/平台/尺寸/风格/数量
- 生成资产: logo/CIP 走 Gemini 图像 API, icon 走 Gemini 3.1 Pro 输出 SVG 文本, slides/banner/social photos 直接写 HTML/CSS (Tailwind + 设计 token + Chart.js)
- 精确导出: HTML 经 chrome-devtools/Playwright 按目标平台精确像素截图为 PNG (2x deviceScaleFactor)
- 校验与交付: Chrome MCP 视觉检查导出图, 修复后重导; 侧边并列展示方案, 按反馈迭代, 最后写报告并整理资产

- BM25 本地检索: scripts/{logo,cip}/core.py + search.py 把用户描述匹配到内置数据 (logo 55 风格/30 调色板/25 行业; CIP 50+ 交付物/20 风格/20 行业), 输出设计简报, 纯本地数据匹配
- AI 生成双通道: google-genai 库 + GEMINI_API_KEY, logo/CIP 默认 gemini-2.5-flash-image (Pro 用 gemini-3-pro-image-preview, 4K 文字), 可选 MuAPI 异步任务端点 (nano-banana / nano-banana-pro); icon 用 gemini-3.1-pro-preview 纯文本输出 SVG (SVG 即 XML 文本, 不走图像生成); logo 一律白底输出
- HTML→截图管线 + 设计规则校验: banner/social photos 按平台尺寸表出稿, 约束包括单一 CTA (右下, ≥44px)、广告文字 <20% (超了 Meta 会降权)、最多 2 种字体、正文 ≥16px/标题 ≥32px、安全区 70-80%、印刷 300 DPI CMYK + 出血; 脚本报错时直接修脚本本身而非绕过
