# nano-banana-2 (`prime-skills/runcomfy-agent-skills/nano-banana-2`)

## whitebox

- 触发: 用户提到 "nano banana" / "nano-banana-2" / "gemini image" 等关键词, 或明确要求用该模型生图 → 路由到本 skill
- 构造输入: 把用户描述整理成 subject-first 的 prompt, 按 schema 填 JSON (prompt 必填; num_images/aspect_ratio/resolution/seed 等未指定则用默认值), 枚举越界会在上游被 422 拒绝
- 鉴权并调用: runcomfy login (浏览器设备码流程) 或 RUNCOMFY_TOKEN 环境变量完成认证, 执行 runcomfy run google/nano-banana-2/text-to-image --input '<json>' --output-dir <绝对路径>
- 远程生成: CLI 把 JSON body POST 到 https://model-api.runcomfy.net/v1/models/google/nano-banana-2/text-to-image, 轮询请求直至 Google Nano Banana 2 (Gemini 系 flash 档文生图模型) 完成
- 取回结果: 轮询到结果后把返回 URL 的图片下载进 --output-dir, 退出码 0; Ctrl-C 会在退出前取消远程请求

- 输入校验: aspect_ratio 仅限 11 个枚举值, resolution 仅 0.5K/1K/2K/4K 四档, 越界 → 上游 422 / 退出码 65 (schema 不匹配); 图内文字必须在 prompt 中用引号写出字面字符, 否则渲染不可预测
- 无 shell 注入面: prompt 经 --input 以 JSON 字符串直传, CLI 不做 shell 展开, 直接经 HTTPS 发给 model-api.runcomfy.net; token 写入 ~/.config/runcomfy/token.json (mode 0600), CI 场景用 RUNCOMFY_TOKEN 环境变量绕过文件
- 下载白名单 + 限额: 仅允许从 *.runcomfy.net / *.runcomfy.com 下载产物, 单个文件 > 2 GiB 即中止; 外部依赖: RunComfy CLI (npm i -g @runcomfy/cli) 与 RunComfy Model API 托管的 Google Nano Banana 2 模型
