# image-to-video (`prime-skills/runcomfy-agent-skills/image-to-video`)

## whitebox

- 1. 解析用户意图（人像/产品动画、带配音对口型、图+参考视频/音频多模态），对照路由表选定唯一一个 i2v 模型
- 2. 按该模型的 schema 构造 JSON 输入体（image_url、prompt、duration、resolution、seed 等），prompt 按『运动动词前置、不重复描述图片、单拍一镜』模式写
- 3. 调本地 RunComfy CLI：runcomfy run <vendor>/<model> --input '<JSON>' --output-dir <路径>
- 4. CLI 向 Model API 提交请求并轮询直至任务完成
- 5. CLI 把返回的生成视频 URL 下载到 --output-dir

- 意图路由：三条 route 映射三个模型 API——HappyHorse 1.0 I2V（默认，人像/产品/原生音频，Arena #1）、Wan 2.7 t2v 端点 + audio_url（自定义配音对口型，换 audio_url 即多语言变体）、Seedance 2.0 Pro（图+参考视频+参考音频，最多 9 图/3 视频/3 音频）。每次调用只选一个模型，不做跨路由混合
- Schema 构造与校验：按所选模型约束填字段并校验——图片 ≥300px/≤10MB、宽高比 1:2.5–2.5:1（HappyHorse）、时长 3–15s、音频 3–30s/≤15MB、prompt ≤5000 非中日韩字符、分辨率/宽高比为枚举；参数错误/不合规分别对应 CLI exit code 64/65
- 执行链路依赖 RunComfy CLI（@runcomfy/cli，npm 全局安装）：HTTPS 直连 model-api.runcomfy.net，无 shell 注入面（JSON 体直传）；认证走 runcomfy login 设备码流程（token 存 ~/.config/runcomfy/token.json，权限 0600）或 CI 用 RUNCOMFY_TOKEN 环境变量；下载仅白名单 *.runcomfy.net/.com，单文件 >2GiB 中止
