# relight (`prime-skills/runcomfy-agent-skills/relight`)

## whitebox

- 触发: 用户请求命中 relight 关键词 ("relight"/"golden hour"/"studio lighting"/改光方向/色温等) 或明确要求改变静图打光。
- 路由: 判断是纯打光改动还是复合编辑 — 默认走 Qwen Edit 2509 relight LoRA; 复合编辑或需参考图匹配时回退到 Nano Banana 2 Edit / GPT Image 2 Edit / FLUX Kontext Pro。
- 构造输入: 按 "光源类型 → 量化参数 (色温/方向/强度) → 显式保留声明" 写 prompt, 连同图片 URL 组装成 JSON。
- 执行: 唯一工具 Bash(runcomfy *), 调 `runcomfy run <model> --input '<JSON>' --output-dir ./out` (前置条件: runcomfy login 或 RUNCOMFY_TOKEN)。
- 取回结果: CLI POST 到 RunComfy Model API, 轮询请求状态, 成功后把生成图下载到 --output-dir, 退出码 0。

- 模型路由机制: 按任务性质分流 — 打光专属改动选专用 relight LoRA (qwen/qwen-edit-2509/lora/relight); 打光只是复合编辑一部分选 Nano Banana 2 Edit; "匹配参考图光线" 选 GPT Image 2 Edit; 单条指令高保真微调选 FLUX Kontext Pro。
- Prompt 工程约束: 光源类型优先并量化 (色温 warm 3200K/neutral 5500K/cool 6500K, 方向 camera-left 45°/top-down/rim, 强度 soft/hard/flat), 且必须显式写 "preserve subject pose, framing, and color identity" 防止主体漂移; 时间短语 (golden hour/blue hour) 自动解析为色温+柔硬度。
- 执行与安全边界: 输入以 JSON 字符串经 --input 传入, CLI 不做 shell 展开 (无注入面); token 存于 ~/.config/runcomfy/token.json (0600) 或 RUNCOMFY_TOKEN; 出站仅限 *.runcomfy.net / *.runcomfy.com; 单文件下载上限 2 GiB; 依赖外部组件: runcomfy CLI (npm @runcomfy/cli) 与 RunComfy Model API (model-api.runcomfy.net)。
