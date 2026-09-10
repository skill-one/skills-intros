# ckm:banner-design (`nextlevelbuilder/ui-ux-pro-max-skill/ckm:banner-design`)

## whitebox

- 通过 AskUserQuestion 收集需求: 用途/平台尺寸/文案/品牌素材/风格/数量 (默认 3 个方案)
- 读取内置参考文件 references/banner-sizes-and-styles.md, 确定精确尺寸、安全区与适配风格, 选定 2~3 个艺术方向
- 逐个方向用 HTML/CSS 在精确平台尺寸上构建 banner, 叠加文案/CTA/logo (素材优先用用户提供的, 否则 CSS 自绘, 可选 AI 生图)
- 浏览器按目标 viewport 预览, 截取 banner 元素为 PNG, 校验像素尺寸/安全区/字体加载, 超平台大小限制则压缩优化
- 按 assets/banners/{campaign}/{style}-{width}x{height}.png 落盘, 并排展示方案+设计理由+文件路径, 按反馈迭代至通过

- HTML/CSS 是唯一渲染载体: banner 本体、文案、CTA、logo 全部在 HTML 层叠加, 视觉元素用 CSS (渐变/几何/字体) 构建以零依赖出图; 生成式图像提示词刻意不含文字, 保证文案始终可编辑
- 硬性校验规则内置: 关键内容限制在画布中央 70~80% 安全区, 文字对比度 ≥4.5:1, 最多 2 种字体 + 单一 CTA, 广告类文字占比 <20%; 尺寸和风格数据全部来自 bundled 参考文件, 不臆造
- 导出依赖运行时能力且带降级路径: PNG 截图走运行时标准浏览器/截图工具 (按精确 viewport 截取元素); 截图不可用时降级交付 HTML/CSS 源码并明确标记 PNG pending; 文件超限时用可用图像优化器压缩
