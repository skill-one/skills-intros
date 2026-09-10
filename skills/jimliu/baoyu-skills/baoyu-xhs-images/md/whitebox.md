# baoyu-xhs-images (`jimliu/baoyu-skills/baoyu-xhs-images`)

## whitebox

- Step 0 (阻塞): 按固定顺序查找并加载 EXTEND.md 用户偏好 (项目 → XDG → 用户目录), 首次运行且交互模式则先走一次性初始化设置
- Step 1: 保存源内容并深度分析 → 写 analysis.md, 检测语言、推荐图片数 (2-10), 并按内容信号→推荐表自动选定大纲策略 + 风格/版式/配色
- Step 2 (硬性关卡): Smart Confirm — 必须等用户确认推荐方案才进入生成, 仅 --yes / "直接生成" 等显式措辞可跳过
- Step 3: 先把每张图的完整最终 prompt 落盘到 prompts/NN-{type}-{slug}.md, 再解析图像后端, 按锚点链分批生成 (先出图 1, 再以其为参考批量出图 2+)
- Step 4: 输出完成报告

- 三维独立组合 + 信号自动选型: 风格 (12 种) × 版式 (8 种) × 可选调色板 (macaron/warm/neon) 自由搭配, preset 只是快捷组合; 源内容关键词命中信号表首行即胜, 无命中回落 cute-share; 用户 --ref 参考图与内部"图 1 锚点链"分层叠加
- 图像后端解析链: 当前消息指定 > EXTEND.md 偏好 > 自动选择 (优先运行时原生工具如 Codex imagegen / Cursor GenerateImage, 其次 codex CLI 经 baoyu-image-gen 路由, 均无则询问用户); 两条硬规则: 只出位图、严禁用 SVG/HTML/代码渲染替代, 严禁事后用 ImageMagick/Pillow 等修图覆盖已生成文字 — 文字有错只能改 prompt 重生成
- 锚点链 + 批量调度 + 备份: prompt 文件全部落盘并校验后才开批; 图 1 先生成作全系列视觉锚点, 图 2+ 引用图 1 分批并行 (batch_size 默认 4, 钳制 1-8), 失败项重试一次、成功项不重做; 任何文件覆盖前先重命名为 -backup-时间戳
