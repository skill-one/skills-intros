# lipsync (`prime-skills/runcomfy-agent-skills/lipsync`)

## blackbox

**function**: 让视频里的人嘴型对上声音：把一段音频配到一段视频或一张人像照片上，生成开口说话、口型同步的视频。

- input: 一段原始视频的链接 + 一段配音音频的链接, output: 一条新视频：画面原样保留（镜头、背景、动作不变），只有嘴型被替换成跟着配音说的样子
- input: 一张人像照片 + 一段语音音频, output: 一段照片里的人开口说话的短视频，像真人在播报
- input: 一段写好的台词文本（没有现成音频）, output: 一段直接照台词说话的口播视频，语音和嘴型都是现成的
