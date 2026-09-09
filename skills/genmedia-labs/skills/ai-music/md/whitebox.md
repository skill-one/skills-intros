# ai-music (`genmedia-labs/skills/ai-music`)

## whitebox

- 解析用户请求, 按决策流分类到 4 条路由之一: 生成 (premium → ElevenLabs; 便宜/多语言 → ACE Step) vs 编辑 (时间段重写 → audio-inpaint; 前后延展 → audio-outpaint)
- 按所选模型套用其文档化提示词模式: ElevenLabs 用单个 prompt (风格+歌词+段落标记); ACE Step 拆成 tags (风格) + lyrics (人声, 含 [Verse]/[Chorus]/[inst] 标记)
- 执行 runcomfy run <vendor>/<model>/<endpoint> --input '<JSON体>' --output-dir ./out
- CLI 将 JSON body 经 HTTPS POST 到 RunComfy Model API, 并轮询请求状态
- 成功 (退出码 0) 后把生成的音频文件下载到 --output-dir

- 意图路由: 请求被分类为 generate vs edit · premium vs cost-sensitive · multilingual · vocal vs instrumental, 直接决定模型 ID (elevenlabs/elevenlabs/music-generation 或 acestep-ai/ace-step[-1.5] 的 text-to-audio / audio-inpaint / audio-outpaint 共 5 个端点); 两个模型提示词 schema 不同 — ElevenLabs 单 prompt 带 [Intro]/[Verse]/[Chorus] 段落标记, ACE Step 强制 tags/lyrics 二分
- 唯一执行面是 runcomfy CLI (allowed-tools 限定为 Bash(runcomfy *)): 提示词/歌词/音频 URL 全部作为 --input 的 JSON 字符串传递, CLI 不做 shell 展开 (无 shell 注入面), 仅出站到 model-api.runcomfy.net 及 *.runcomfy.net 白名单; 单文件下载上限 2 GiB; Ctrl-C 会在退出前取消远端请求
- 校验与错误信号靠退出码: 输入 JSON/schema 不符 → 65, 未登录或 token 被拒 → 77, 超时/429 → 75 (可重试), 上游 5xx → 69, 参数错误 → 64
