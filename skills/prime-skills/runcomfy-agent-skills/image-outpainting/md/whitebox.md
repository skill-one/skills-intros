# image-outpainting (`prime-skills/runcomfy-agent-skills/image-outpainting`)

## whitebox

- 意图分类: 按任务类型路由到 edit 端点 — 纯 prompt 扩图默认走 Nano Banana 2 Edit, 需参考图匹配走 GPT Image 2 Edit, 品牌风格延续走 Seedream/Dreamina/Qwen/FLUX 2 等品牌 edit 端点
- 构造 outpaint 形状的 JSON: prompt 按三段式书写 (先画布变化 → 再描述延伸内容/光照/风格 → 结尾加 "keep original exactly" 保留语句), 显式传 aspect_ratio 锁定输出画布
- 通过 Bash 调用 `runcomfy run <model>/edit --input '<json>' --output-dir ./out`
- CLI 向 Model API 发 POST, 并轮询请求状态
- 下载生成结果到 --output-dir

- 路由 + 降级机制: 三类意图 (prose 驱动 / reference 驱动 / brand 锁定) 映射到不同端点; 当输出出现接缝或光照不匹配时, 降级到 Route 2 — GPT Image 2 Edit (最多 10 张参考图) 或 FLUX Kontext Pro (单指令最大保留); 若仍不够, 指向 ComfyUI 云端工作流 (GUI 工作流, CLI 触达不了)
- 保留约束: prompt 尾部必须带保留原区域的语句, 否则 Nano Banana 2 可能轻微重绘原图; aspect_ratio 作为显式参数而非让模型从 prompt 猜; 多步扩图靠链式调用, 每次只扩 30–50%
- 外部依赖全部走 `runcomfy` CLI: npm 全局安装 @runcomfy/cli, 认证用 runcomfy login 或 RUNCOMFY_TOKEN; 仅访问 *.runcomfy.net, 单文件下载上限 2 GiB; 结构化退出码 (65=输入 JSON/schema 校验失败, 69=上游 5xx, 75=可重试超时/429, 77=未登录或 token 被拒)
