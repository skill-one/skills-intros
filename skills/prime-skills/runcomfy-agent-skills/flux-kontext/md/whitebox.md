# flux-kontext (`prime-skills/runcomfy-agent-skills/flux-kontext`)

## whitebox

- 触发: 用户明确要求用 Flux Kontext 编辑单张图 (命中 "flux kontext" / "kontext" / "BFL kontext" 等关键词)
- 前置检查: 本地已装 RunComfy CLI (npm @runcomfy/cli), 且有凭证 (runcomfy login 写入的 token 或 RUNCOMFY_TOKEN 环境变量)
- 组装输入: 按最小 schema 构造 JSON — 一条声明式编辑指令 + 一个公开可访问的源图 URL, 可选 aspect_ratio / seed
- 执行: 调 runcomfy run blackforestlabs/flux-1-kontext/pro/edit --input '<JSON>' --output-dir <绝对路径>
- 取回: CLI POST 到 Model API 并轮询至完成, 把生成图下载进 --output-dir; 中途 Ctrl-C 会先取消远端请求再退出

- 最小 schema + 服务端校验: 仅 prompt 和 image 两个必填字段; aspect_ratio 必须取自模型页支持的枚举, 越界会得到 422 或被裁切; seed 固定可复现做变体对比. 外部依赖: RunComfy CLI 与其 Model API (托管 Black Forest Labs 的 Flux 1 Kontext Pro 模型)
- 提示词模式包 (Pro Pack 核心): 不做裸调用, 而是把 Kontext 文档化套路编入 prompt — 单条声明式指令、开头加 "Keep ... unchanged" 保留条款、复合改动拆成多次串行单指令 pass. 这是同一模型下输出更稳的来源
- 传输与安全边界: prompt 经 --input 以 JSON 字符串直传 HTTPS 到 https://model-api.runcomfy.net/v1/models/... , CLI 不做 shell 展开 (无 shell 注入面); 出站仅限 model-api.runcomfy.net, 下载白名单 *.runcomfy.net / *.runcomfy.com 且单文件上限 2 GiB; token 存于 ~/.config/runcomfy/token.json (mode 0600), CI 场景改走 RUNCOMFY_TOKEN 环境变量
