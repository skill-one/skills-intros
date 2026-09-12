# fireworks-tech-graph (`yizhiyanhua-ai/fireworks-tech-graph/fireworks-tech-graph`)

## whitebox

- 解析需求: 定位 SKILL_ROOT, 从需求确定图表类型与风格 (未指定则默认风格 1 扁平图标), 只加载命中的风格参考文件
- 生成输入: 写出声明式 input.json, 选 text_policy (strict=标签逐字可见 / report=允许元数据兜底), 先跑 validate 校验输入
- 渲染检查: render 产出 SVG + 布局报告, 再跑 check 验 SVG 身份、箭头标记引用、语义几何与构图
- 导出成品: 按需 export-png (命令回读 PNG 尺寸自证) / export-html / animate 出 GIF
- 人工验收: 按阅读尺寸看最终 PNG 的文字完整性、对比度、箭头方向、裁切; 有缺陷按 check 报告的元素 ID 定点修复, 最后交付路径+尺寸+残留限制

- JSON→SVG 确定性生成: 风格 1–7、9–12 走自带 python3 CLI fireworks.py 的 JSON 生成器 (声明式输入, 语义约束如 C4/云/事件/可观测性); 风格 8 无生成器, 由 AI 直接写 SVG 但仍过同一套校验/导出门禁。适当场景可直接改已有 SVG, 不必每次走 JSON
- 三层闸门防翻车: validate 查输入 → render 附 layout.json 报告 (完整标签保存在 SVG 元数据, 报告可见截断, 需先解决再宣称文本精确) → check 查语义与构图; 文本宽度是启发式估算, 不能替代查看实际渲染字体, check 连挂两次须换思路而非反复缩字
- 多路输出同一画布: PNG=export-png (读根画布、限尺寸、原子写入、回读尺寸); HTML=export-html (单文件离线、可缩放/复制源码/下载图); GIF=animate (语义 SVG 驱动, 默认 960px/20fps/5.75s, +2s-settled-flow 预设, 产出 .motion.json); 缺渲染器/字体时跑 doctor 诊断
