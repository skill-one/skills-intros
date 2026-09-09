# video-edit (`prime-skills/runcomfy-agent-skills/video-edit`)

## whitebox

- 解析用户意图, 查路由表选定唯一模型: 通用重绘/换背景/换包装 → Wan 2.7 Edit-Video; 参考视频动作迁移 → Kling 2.6 Pro Motion Control; 轻量换装/身份稳定重绘 → Lucy Edit Restyle (默认不明确时选 Wan 2.7)
- 按所选模型的 schema 组装 JSON input: prompt 走 "先写保留目标、单次单一编辑" 模式, 源视频 URL 需满足该模型的时长/大小限制
- 调用本地 CLI: runcomfy run <vendor>/<model>/<endpoint> --input '<json>' --output-dir <绝对路径>
- CLI 把 JSON body 直接 POST 到 model-api.runcomfy.net, 轮询请求直到生成完成
- 从 *.runcomfy.net / *.runcomfy.com 白名单下载结果到 --output-dir; Ctrl-C 会在退出前取消远端请求

- 意图路由: 静态查表分类 (intent → model), 每次调用只选一个模型、不做多路混合; 若用户点名具体模型, 则转交对应的品牌 skill (如 wan-2-7) 做更完整处理
- Schema 驱动的输入构造与校验: 三套独立 schema (必填 prompt/video, 可选 reference_image/resolution/audio_setting 等) + 源视频硬约束 (Wan 2.7: 2–10s、≤100MB、1080p 上限; Kling: 10–30s、image 导向输出限 10s; Lucy: 仅 720p、无画幅控制); prompt 按各模型文档化模式生成 —— preserve-first、单次单一编辑方向、reference_image 仅用于包装/服装等有依据的迁移 (Kling 要求主体占画面 >5%)
- 外部依赖与执行通道: RunComfy CLI (npm 包 @runcomfy/cli, 需 runcomfy login 或 RUNCOMFY_TOKEN 环境变量) 调三个模型 API (wan-ai/wan-2-7/edit-video、kling/kling-2-6/motion-control-pro、decart/lucy-edit/restyle); prompt 经 --input 以 JSON 字符串传输, CLI 不做 shell 展开、无 shell 注入面; 下载仅限 *.runcomfy.net/.com 白名单, 单个文件 >2GiB 中止下载
