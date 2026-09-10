# video (`coreyhaines31/marketingskills/video`)

## whitebox

- 先静默读取产品上下文 (`.agents/product-marketing.md` 等), 只对未覆盖的信息向用户提问 (视频类型/平台/时长、是否真人出镜、已有素材、预算)。
- 查「需求→工具」决策表选技术路线: 程序化视频 (Remotion/Hyperframes) / AI 生成镜头 (Veo 3、Sora 2、Runway、Kling 等) / AI 数字人 (HeyGen/Synthesia) / 长视频剪短再分发 (Descript/Opus Clip/CapCut)。
- 按所选路线执行对应工作流, 如产品演示 = 写脚本 → 录屏 → 程序化叠加标题/标注 → AI B-roll → 配音 → 导出。
- 产出素材并组装成片: Hyperframes/Remotion 渲染 MP4, HeyGen 走 MCP 服务器直接生成数字人视频, 生成类模型走标准 HTTP API。
- 按平台规格导出成品 (9:16 社交竖屏 / 16:9 横屏), 强制配字幕。

- 上下文优先解析: 启动即读取 product-marketing.md (兼容 `.claude/` 路径和 legacy 文件名), 从已有上下文推导答案, 只追问缺口 — 减少来回提问。
- 决策表路由 + 工具转换: 程序化视频里每帧是一个 HTML 文档 (Hyperframes, 时间线合成后渲染 MP4, 确定性渲染: 同输入必同输出; Remotion 则以 React 组件为帧, 支持 Lambda 批量渲染); 原创镜头交给生成模型 API, 提示词按「主体+动作+镜头+风格+情绪」公式构造; 说话人像交给 HeyGen (官方 MCP server, agent 可直接调用)。
- 校验兜底: 常见错误清单把关 — AI 模型渲染不了可读文字, 文案一律走程序化叠加; 必须加字幕 (85% 社交视频静音观看); 宽高比匹配平台; 避免过度制作。复刻爆款剪辑时, 先用 watch-video/social-fetch 拉取参考, 拆成 beat sheet (逐拍分镜表), 人工确认后才执行。
