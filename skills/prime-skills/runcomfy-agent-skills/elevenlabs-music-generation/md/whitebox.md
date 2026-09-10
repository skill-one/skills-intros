# elevenlabs-music-generation (`prime-skills/runcomfy-agent-skills/elevenlabs-music-generation`)

## whitebox

- 触发匹配: 用户明确要求生成音乐/歌曲 ("generate music"、背景音乐、jingle、主题曲等) → 提取需求: 风格、歌词、时长、是否人声
- 组装唯一输入 prompt 字段: 风格简述在前 (genre/BPM/乐器/人声类型), 歌词接在后并加 [Intro]/[Verse]/[Chorus] 等段落标记; 同时定 music_length_ms (5000–300000) 与 force_instrumental
- 执行 runcomfy run elevenlabs/elevenlabs/music-generation --input '{...}' --output-dir ./out (skill 的命令面仅限 runcomfy 子命令)
- CLI 将 JSON body 经 HTTPS POST 到 model-api.runcomfy.net, 轮询请求状态直至完成
- CLI 拉取结果中的音频 URL, 下载 44.1 kHz 立体声文件到 --output-dir; 计费按时长 (~$0.0083/s)

- 单 prompt 封装: 端点无独立 lyrics 参数, 风格 + 歌词全在一个字符串; 写法约束 = 段落标记 + 大致拍数 (如 [Verse 16 bars]), 保持每行音节数对齐; 纯器乐 = force_instrumental: true 且 prompt 内再写 "no vocals" 双保险; 多语言 = 直接用目标语言写词, 需要时行内标注语种
- 外部依赖 runcomfy CLI: skill 自身不做 HTTP — 提交/轮询/下载全由 CLI 完成; 前置条件是 runcomfy login (token 写入 ~/.config/runcomfy/token.json, mode 0600) 或 CI 中 export RUNCOMFY_TOKEN; 另一个可选外部模型/库均无, 这是唯一依赖链
- 校验与边界: prompt 以 JSON 字符串经 --input 传入, CLI 不做 shell 展开 → 无 shell 注入面; schema 失败 (music_length_ms 超界/类型错) exit 65, 429/超时 exit 75 可重试, 未登录 exit 77; 成本与时长线性相关, 节费策略: 先 35 s draft 锁风格/结构, 再付全长 render
