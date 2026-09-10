# ai-video-generation (`prime-skills/runcomfy-agent-skills/ai-video-generation`)

## blackbox

**function**: 你给我一句话、一张图或一段配音, 我还你一段成品 AI 视频 (最长约 15 秒, 带画面和声音)。

- input: 一段文字描述, 如「海边日落, 一只红风筝在风中翻滚, 孩子们笑着追它, 有海浪声」, output: 一条带同步音效的 MP4 视频 (1080p, 横屏/竖屏可选, 最长约 15 秒)
- input: 一张静态图片 + 一句动作指令, 如「她缓缓转头看向镜头并微笑」, output: 这张图被"演活"的短视频: 人物长相保持原样, 只有你指定的动作和镜头运动发生
- input: 一张人物照片 + 一段配音 MP3 (如产品介绍录音), output: 照片里的人物开口"说话"、口型与配音逐字对齐的视频
