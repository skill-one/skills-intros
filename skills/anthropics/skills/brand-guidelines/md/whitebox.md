# brand-guidelines (`anthropics/skills/brand-guidelines`)

## whitebox

- 触发: 当任务涉及品牌配色、字体排版、视觉风格 (如做 PPT/文档要 Anthropic 风格) 时被启用
- 加载规范: 从技能内置的 brand guidelines 读取 4 个主色 + 3 个强调色的 RGB 色值及字体规则
- 应用字体: 标题 (≥24pt) 套 Poppins, 正文套 Lora; 未安装时自动降级为 Arial / Georgia
- 应用颜色: 文字颜色根据背景智能选取深/浅色, 非文字形状按橙→蓝→绿轮换强调色
- 输出: 输出完成品牌化的产物, 原有的文本层级与格式保持不变

- 字体管理: 优先用系统已安装的 Poppins/Lora, 检测不到就自动回退 Arial (标题) / Georgia (正文), 免安装、跨系统可读
- 精确着色: 硬编码品牌 RGB 色值, 通过 python-pptx 的 RGBColor 类写入 (核心外部依赖是 python-pptx 库)
- 层级与 accent 规则: 靠字号阈值 (24pt) 区分标题与正文, 只换字体和颜色不改内容; 非文字形状轮换橙 (#d97757)、蓝 (#6a9bcc)、绿 (#788c5d) 保持视觉节奏
