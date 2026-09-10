# image-inpainting (`prime-skills/runcomfy-agent-skills/image-inpainting`)

## whitebox

- 解析请求, 判断是否提供 mask (灰度二值掩码: 白=重绘区, 黑=保留区)
- 有 mask → 路由到 Z-Image Turbo Inpainting; 无 mask → 降级到 Nano Banana 2 Edit, 用空间语言在 prompt 里描述目标区域
- 按意图构造 JSON 输入: prompt 写明 mask 外区域的保留约束, strength 按任务分层取值, 可选 control_scale / seed / aspect_ratio
- 执行 `runcomfy run <model> --input '<JSON>' --output-dir ./out`
- CLI 向 Model API 发请求并轮询状态, 成功后下载结果到 --output-dir, 退出码 0

- 路由机制: 以「是否有 mask」为核心分流依据; mask 缺失时走描述式编辑兜底 (Nano Banana 2 Edit / GPT Image 2 Edit / FLUX Kontext Pro)
- 参数映射: strength 按意图分层 — 0.3–0.5 修瑕 / 0.6–0.7 带风格替换 / 0.8–1.0 整区替换; control_scale 典型 0.6–0.9; prompt 中显式命名 mask 外要保留的内容
- 传输层: 依赖 runcomfy CLI (npm i -g @runcomfy/cli); prompt 与图片/mask URL 以 JSON 字符串经 --input 传入, CLI 不做 shell 展开 (无 shell 注入面); 鉴权读 ~/.config/runcomfy/token.json (0600) 或 RUNCOMFY_TOKEN 环境变量; 出站仅限 *.runcomfy.net / *.runcomfy.com, 错误映射为退出码 64/65/69/75/77
