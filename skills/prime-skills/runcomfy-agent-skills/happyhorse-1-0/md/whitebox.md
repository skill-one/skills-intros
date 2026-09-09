# happyhorse-1-0 (`prime-skills/runcomfy-agent-skills/happyhorse-1-0`)

## whitebox

- 触发匹配: 用户提到 "HappyHorse" 或明确要求用该模型生成视频 → 路由到 happyhorse/happyhorse-1-0/text-to-video 端点
- 构造 JSON 输入: 按 schema 填 prompt (必填, ≤2500 字符) 及可选 aspect_ratio / resolution / duration / seed / watermark
- 调用本地 RunComfy CLI: runcomfy run happyhorse/happyhorse-1-0/text-to-video --input '<JSON>' --output-dir <path>
- CLI 带 bearer token POST 到 model-api.runcomfy.net 拿到 request_id, 之后每 2 秒轮询 GET /requests/<id>/status 直到终态
- 终态后拉取 /result, 将 *.runcomfy.net / *.runcomfy.com 域名下的文件下载到 --output-dir, stdout 输出结果 JSON

- 认证与输入传递: 依赖 RunComfy CLI (npm i -g @runcomfy/cli); token 来自 runcomfy login 设备码流程 (写入 ~/.config/runcomfy/token.json, mode 0600) 或 RUNCOMFY_TOKEN 环境变量 (CI/容器场景); prompt 以 JSON 字符串经 --input 传入, CLI 不做 shell 展开, 无注入面
- 校验与错误映射: 服务端按 schema 强校验 (aspect_ratio 仅 5 个枚举值, duration 3–15s, seed 0..2^31-1, 超 2500 字符 prompt 会降质), 违规返回 422; CLI 映射为 sysexits 退出码 — 65 输入/schema 错误, 69 上游 5xx, 75 超时/429 可重试, 77 未登录/token 被拒
- 轮询与下载防护: 每 2s 轮询一次状态; 结果下载仅限 *.runcomfy.net / *.runcomfy.com 白名单域名, 单文件 > 2 GiB 中止防止磁盘写满; 轮询期间 Ctrl-C 会发送 POST .../requests/<id>/cancel 取消请求, 避免为已停止的 GPU 付费
