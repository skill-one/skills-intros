# baoyu-slide-deck (`jimliu/baoyu-skills/baoyu-slide-deck`)

## whitebox

- ① 分析输入：对内容分类、检测语言、按长度估算页数，并扫描信号关键词匹配 17 个风格预设之一（未命中则回退 blueprint）
- ② 强制确认门槛：批量向用户确认风格/受众/页数/是否逐级审阅，未确认（或未明确说"直接生成"）绝不进入后续步骤
- ③ 生成大纲 outline.md，再为每张幻灯片把最终图像 prompt 落盘为独立文件 prompts/NN-slide-*.md
- ④ 调用图像后端分批生成幻灯片 PNG（默认每批 4 张，原生批量接口 > 并行工具调用 > 串行）
- ⑤ 用 bun/npx 运行合并脚本，把 PNG 合成 PPTX 和 PDF，输出总结

- 风格四维系统：每个预设 = 纹理/情绪/字体/密度四个维度的组合，按源内容信号词自动选择（如 tutorial→sketch-notes、architecture→blueprint）；若用户选自定义，再逐维四问替换预设。这是内容到视觉规范的解析与转换层
- Prompt 文件先行（硬性要求）：任何后端调用前，每张图的完整最终 prompt 必须写入 prompts/ 文件——作为可复现记录，换后端无需重写；已有文件写入前自动备份改名，保护用户编辑
- 图像后端解析链 + 两条硬约束：优先后端为运行时原生工具（Codex imagegen → Cursor GenerateImage → codex CLI → baoyu-image-gen 等），都不可用则询问用户；①严禁用 SVG/HTML/代码渲染替代位图生成，②严禁用 ImageMagick/Pillow 等在成品图上修图改字，文字有错只能改 prompt 重生成
- 外部依赖：bun 或 npx（用于运行 merge-to-pptx.ts / merge-to-pdf.ts 合并脚本）；各图像后端背后的位图生成模型 API
