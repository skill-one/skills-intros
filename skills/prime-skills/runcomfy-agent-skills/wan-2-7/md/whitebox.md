# wan-2-7 (`prime-skills/runcomfy-agent-skills/wan-2-7`)

## whitebox

- 触发判定: 用户显式点名 "Wan / Wan 2.7 / wan-ai / alibaba video" 直达本模型; 若是泛需求则按路由表匹配 (音频对口型 / 多参考运动控制 / 平滑转场 → Wan 2.7, 否则分流到 HappyHorse / Seedance / Kling / LTX)
- 环境检查: 确认已装 RunComfy CLI (`npm i -g @runcomfy/cli`), 认证走 `runcomfy login` 设备码流程, CI/容器用 `RUNCOMFY_TOKEN` 环境变量
- 组装输入 JSON: 必填 `prompt`, 可选 `audio_url` / `aspect_ratio` / `resolution` / `duration` / `negative_prompt` / `enable_prompt_expansion` / `seed`, 缺省值 5s / 1080p / 16:9
- 执行 `runcomfy run wan-ai/wan-2-7/text-to-video --input '<JSON>' --output-dir <绝对路径>`
- CLI 向 model-api.runcomfy.net 提交请求 → 轮询至完成 → 拉取结果并把 .runcomfy.net/.runcomfy.com 的产物 URL 下载进 --output-dir, 退出码 0 即成功

- 输入校验 (对应 exit 65): prompt ≤5000 字符 (~1500 tokens); audio_url 限 WAV/MP3、3–30s、≤15MB, 超规格直接拒绝; duration 2–15 整数秒; aspect_ratio 仅 5 个枚举值; negative_prompt ≤500 字符; JSON/schema 不符 → exit 65, 超时/429 → 75 (可重试), 上游 5xx → 69
- Prompt 扩展开关: `enable_prompt_expansion` 默认 true, 短 prompt 由模型自动改写扩写; 需要逐字控制 (如品牌严格的广告文案) 时显式设 false, 配合 negative_prompt 排除具体问题 (泛化的负面词会被忽略)
- 传输与安全边界: prompt 以 JSON 字符串经 `--input` 传给 CLI, 不做 shell 展开 → 无 shell 注入面; 仅出站到 model-api.runcomfy.net, 下载白名单限 *.runcomfy.net / *.runcomfy.com, 单文件 >2 GiB 中止; token 存于 ~/.config/runcomfy/token.json (mode 0600) 或走 RUNCOMFY_TOKEN 环境变量; Ctrl-C 退出前会取消远端请求; 外部图片/音频 URL 由 RunComfy 服务端而非本机拉取
