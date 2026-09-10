# ai-video-generation (`prime-skills/runcomfy-agent-skills/ai-video-generation`)

## whitebox

- 解析用户意图: 判断是文生视频 (t2v)、图生视频 (i2v) 还是续写已有视频 (extend), 以及对音质/口型/物理精度/成本/时长的要求
- 按意图在 RunComfy 模型目录中路由到具体 endpoint (如口型同步→Wan 2-7, 物理旋转→Veo 3-1, 一般默认→HappyHorse 1.0)
- 按该模型的文档化模式构造 prompt (动词优先的运动描述、内联 'Audio: …'、镜头语言) 并填参数 (duration/aspect_ratio/resolution/image_url/audio_url 等)
- 通过 Bash 工具执行 runcomfy run <vendor>/<model>/<endpoint> --input '{JSON}' --output-dir ./out 发起生成
- 视频落盘到 output-dir; 若要超过单次时长上限, 换 Veo 3-1 extend-video 端点链式续写

- 意图→模型路由: skill 内置 'Pick the right model' 决策矩阵, 每个模型标注 Pick for / Avoid for (如 HappyHorse=默认+画面内生成音频、Wan 2-7=audio_url 驱动口型、Veo=物理精确、Seedance v2=多参考+电影感、Fast/Standard 档=省成本迭代), 据此把意图映射到唯一 endpoint
- schema 透传 + prompt 模式库: 每个模型的字段集原样写入 --input JSON ('pass field set through the CLI verbatim'), prompt 文本则套用该模型文档化写法 (主体+动作先行、运动动词>形容词、多镜头显式写切镜、Veo 写 'no other motion' 锁定其他元素)
- 外部依赖: runcomfy CLI (npm i -g @runcomfy/cli 安装, runcomfy login 或 RUNCOMFY_TOKEN 鉴权) 作为智能路由器对接 RunComfy 全量视频模型 API; 本 skill 唯一被授权的执行通道是 Bash(runcomfy *)
