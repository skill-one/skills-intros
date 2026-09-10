# wan-3-0-prime-reference-to-video (`genmedia-labs/skills/wan-3-0-prime-reference-to-video`)

## whitebox

- 命中触发词 (如 "wan 3.0 prime" / "reference to video" / "ref2v" / "从参考图生成视频") → 路由到本 skill
- 收集输入: prompt (≤20k 字符, 用 "Image 1" 等称呼参考) + 至少一个公开可访问的参考 URL (图/视频/音频)
- 校验 schema: 参考硬上限 (10 图 / 5 视频各 1–15s 且合计 ≤15s / 5 音频合计 ≤15s)、时长 2–30 整秒、分辨率与宽高比枚举; 用户无任何参考素材 → 改路由到 text-to-video 兄弟端点
- 通过 Bash 工具执行 `runcomfy run wan-ai/wan-3.0-prime/reference-to-video --input '{JSON}' --output-dir <path>`, 按"计费秒"(成片时长 + 参考视频总时长) 估算成本
- CLI POST 到 RunComfy Model API → 拿 request id → 轮询至终态 → 把 *.runcomfy.net/.com 结果文件下载进 --output-dir (Ctrl-C 可在计费前取消)

- 编号参考绑定 (本端点存在的核心): 参考按传入数组顺序编为 "Image 1" / "Video 1" / "Audio 1", 在 prompt 里点名调用 — 稳定身份 (人脸/产品/场景) 放参考, 运动/镜头/光线放 prompt; `prompt_extend` 默认 true 会自动扩写短 prompt, 需要逐字保真或提速时关掉
- 提交前校验 + 计费模型: 至少一项参考是硬性要求, prompt-only 请求直接被拒; 计费秒 = 输出时长 + 参考视频时长之和 (参考图和音频不计入), 乘以分辨率单价 ($0.0624 / $0.124 / $0.249 每秒); 提交前数字是估算, 参考视频时长跑完实测后结算
- 执行链依赖 RunComfy CLI: allowed-tools 仅放行 `runcomfy` 命令; 认证走 `runcomfy login` 设备码流程或 RUNCOMFY_TOKEN 环境变量 (CI 场景); CLI 负责向 model-api.runcomfy.net 提交请求、轮询到终态、把 *.runcomfy.net/.com 白名单内的结果 URL 下载到 --output-dir; 底层是 RunComfy Model API 托管的 Wan-AI Wan 3.0 Prime Reference to Video 模型
