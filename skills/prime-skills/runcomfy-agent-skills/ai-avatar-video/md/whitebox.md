# ai-avatar-video (`prime-skills/runcomfy-agent-skills/ai-avatar-video`)

## whitebox

- 对请求做意图分类: 是否已有音频文件、人物是写实还是风格化、单镜头还是电影级
- 按分类命中 5 条路由之一 (OmniHuman 为默认), 每条路由绑定固定的模型 endpoint 与输入 schema
- 拼装该路由的 JSON 输入体 (prompt / image_url / audio_url 等), 以 `runcomfy run <vendor>/<model>/<endpoint> --input '{...}'` 发起
- runcomfy CLI 将请求 POST 到 Model API, 轮询任务状态直至完成
- 取回结果, 把返回的产物 URL 下载到 `--output-dir`

- 路由是静态映射而非推理: skill 内置 5 条 route, 每条规定模型 ID + 输入字段 + 适用/不适用条件 (如 OmniHuman 只吃 image_url+audio_url 无 prompt; HappyHorse 把台词以 `says clearly: "…"` 字面量嵌进 prompt; Wan 2-7 用 audio_url 字段驱动口型, prompt 只描述场景)
- 执行面收口在 runcomfy CLI (allowed-tools 仅 `Bash(runcomfy *)`): 输入统一为 `--input` 单个 JSON 字符串, CLI 不做 shell 展开, 无 shell 注入面; 错误用 exit code 区分 (65 schema 不匹配 / 75 429·超时可重试 / 77 未登录), 供重试与校验循环使用
- 前置校验与安全闸: token 来自 `runcomfy login` (0600) 或 RUNCOMFY_TOKEN; 用户提供人像+音频时校验肖像与声音权利, 拒绝未经同意克隆真人; 参考素材 URL 视为不可信、仅接受用户显式提供; 出网端点白名单 *.runcomfy.net/.com, 单文件下载上限 2 GiB
