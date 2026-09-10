# ai-music (`prime-skills/runcomfy-agent-skills/ai-music`)

## whitebox

- 识别用户意图: 生成还是剪辑现有音频、追求品质还是控制成本、是否多语言、有无现成音频文件。
- 按内置决策流程选定唯一路由: 生成→ElevenLabs Music (Route 1) 或 ACE Step / 1.5 (Route 2); 剪辑→audio-inpaint (Route 3) 或 audio-outpaint (Route 4)。
- 按所选模型的参数规范组装 JSON 输入: ElevenLabs 用单个 prompt 携带风格+歌词+段落标记; ACE Step 拆成 tags + lyrics + duration; inpaint 给 start_time/end_time, outpaint 给 extend_before/after_duration。
- 执行 `runcomfy run <vendor>/<model>/<endpoint> --input '{...}' --output-dir ./out`。
- CLI 把请求 POST 到 RunComfy Model API, 轮询任务状态直至完成, 把生成的音频文件下载到 --output-dir 交付。

- 意图→模型路由: skill 维护模型目录表 + 决策流程 (生成 vs 剪辑 → 品质 vs 成本 → 多语言 → 单条 vs 批量), 每个模型配固定的提示词模式 — ElevenLabs 单 prompt 含 [Intro]/[Verse]/[Chorus] 段落标记, ACE Step 风格进 tags、歌词进 lyrics (支持 [inst] 标记纯器乐)。
- 唯一执行通道是 runcomfy CLI (allowed-tools 仅 Bash(runcomfy *)): 认证靠 runcomfy login 写入的 token 或 RUNCOMFY_TOKEN 环境变量; --input JSON 直接经 HTTPS 发往 model-api.runcomfy.net, 不经 shell 展开 (提示词无注入面); 单文件下载上限 2 GiB; 靠退出码判错 (65=输入 JSON 不合法, 69=上游 5xx, 75=超时/429 可重试, 77=未登录)。
- 底层模型 API: elevenlabs/elevenlabs/music-generation (44.1 kHz 立体声人声, 5s–5min, $0.0083/s); acestep-ai/ace-step 与 ace-step-1.5 的 text-to-audio (开源权重, $0.0002–0.0003/s, 1.5 支持 50+ 语言); acestep 的 audio-inpaint (按时间范围重生成段落) 与 audio-outpaint (双向延展, 总长上限 4 min)。
