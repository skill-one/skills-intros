# image (`coreyhaines31/marketingskills/image`)

## whitebox

- 读上下文: 先查找并读取 product-marketing.md 类上下文文件, 再只追问缺失信息 (图片类型、投放平台与尺寸、品牌资产、是否有图像工具 API key)
- 路由选型: 按决策表将任务归入五种路径之一 (AI 生成 / AI 编辑 / 设计工具 / 真实截图+叠加 / 图库), 再用决策树定具体模型
- 生成制作: 按「主体+场景+风格+光线+构图+技术参数」公式写提示词, 并强制指定平台规格尺寸 (如博客头图/OG 用 1200x630)
- 优化交付: 压缩转 WebP (目标 <200KB、质量 75-85%), 设置显式宽高防布局抖动, 补齐 OG meta 标签与 alt 文本

- 上下文优先解析: 启动时先读 .agents/product-marketing.md (或 .claude/ 及旧版文件名), 已覆盖的信息不再向用户重复提问
- 决策表路由与禁用规则: 图内有文字→Ideogram; 品牌一致性→Flux 多参考图/Recraft; 图像编辑→Gemini/Flux Kontext; 产品 UI 展示→强制走真实截图+设备框, 禁止用 AI 生成 (模型会幻觉出假界面); Logo 等矢量资产→设计工具而非 AI
- 外部依赖: 模型侧 Gemini API (Nano Banana)、BFL Flux API/Replicate/fal.ai、Ideogram API、GPT Image、Recraft API; 工具侧 Canva/Figma 模板、浏览器截图工具; 优化侧 cwebp/ImageMagick/jpegoptim 命令、动态 OG 用 Vercel OG/Satori
