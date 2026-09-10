# seedance-2-5-reference-to-video (`genmedia-labs/skills/seedance-2-5-reference-to-video`)

## whitebox

- 组装 JSON body: prompt + 参考素材 (images ≤9 锁角色/风格, videos ≤3 提供镜头运动, audios ≤3 提供节奏) + aspect_ratio / duration (4-30s) / generate_audio
- 执行 `runcomfy run bytedance/seedance-2.5/reference-to-video/1080p --input '{...}' --output-dir ./out` (CLI 经 npm 安装, 靠 runcomfy login 设备码或 RUNCOMFY_TOKEN 鉴权)
- CLI 把请求 POST 到 model-api.runcomfy.net, 轮询任务状态直到完成
- 从返回结果中抓取 *.runcomfy.net / *.runcomfy.com 的输出 URL, 下载到 --output-dir; Ctrl-C 可在退出前取消远端任务

- 参数转换/校验靠 schema 对齐: 2.0 的 image_url/video_url/audio_url 在 2.5 已改名为 images/videos/audios, 字段名错 → exit 65; duration 出界、aspect_ratio 非法同样报 65; 鉴权失败 77、429/超时 75 可重试、上游 5xx 69。输出分辨率固定 1080p, 无 resolution 字段; videos 虽在 schema 标 required, 实际可省略
- 参考条件生成由 Seedance 2.5 模型完成 (经 RunComfy Model API): 稳定项 (人脸/服装/产品/风格) 走 images, 变化项 (动作/镜头/光线) 走 prompt, 参考视频只传递镜头运动与节奏、不迁移主体; generate_audio=true 时同一次生成原生同步的语音/音效/音乐
- 计费与降级策略: 计费秒 = 参考视频时长 + 输出时长, $0.53/秒 (480p 草稿档仅 $0.12/秒) → 先在 480p 用 3-5 个变体验证参考组合, 胜出的 body 原样重跑 1080p
