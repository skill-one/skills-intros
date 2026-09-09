# video-edit (`genmedia-labs/skills/video-edit`)

## whitebox

- 解析用户意图, 按 SKILL.md 的意图→模型对照表归类 (重绘/运动迁移/换装换背景等), 每次调用只选一条路线
- 按所选路线的 schema 组装 JSON 输入: prompt 遵循『先保真、后改写』模板, 填入 video URL 及可选 reference_image / audio_setting 等字段
- 通过本地 RunComfy CLI 执行 runcomfy run <vendor>/<model>/<endpoint> 提交请求
- CLI 将 JSON 体经 HTTPS 直接 POST 到 Model API (model-api.runcomfy.net), 轮询请求直至完成
- 拉取结果, 把 *.runcomfy.net / *.runcomfy.com 的产出下载到 --output-dir; Ctrl-C 会在退出前取消远端请求

- 意图路由: 核心是一张静态对照表 — 通用重绘/背景/包装替换→Wan 2.7 Edit-Video (身份+运动保持, 1080p 上限, 默认选项); 参考视频运动迁移→Kling 2.6 Pro Motion Control (character_orientation 为 image 上限 10s, video 上限 30s); 轻量换装/氛围重绘→Lucy Edit Restyle (仅 720p)。不做多路线混合。
- Schema 对齐即校验: 各路线的必填字段、枚举、素材硬约束 (Wan: MP4/MOV 2–10s ≤100MB; Kling: 参考图中主体需 >5% 画面) 均来自 SKILL.md 表格, 输入不符会触发 exit code 65 (bad input JSON / schema mismatch)。
- 外部依赖与安全边界: RunComfy CLI (npm i -g @runcomfy/cli, 需 runcomfy login 或 CI 下 RUNCOMFY_TOKEN) + 三个模型 endpoint; prompt 以 JSON 字符串经 --input 直传, CLI 不做 shell 展开 (无注入面); 令牌存于 ~/.config/runcomfy/token.json (0600); 单文件下载 >2GiB 自动中止。
