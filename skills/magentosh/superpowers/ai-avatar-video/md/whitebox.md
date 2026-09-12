# ai-avatar-video (`magentosh/superpowers/ai-avatar-video`)

## whitebox

- `belt login` 完成 inference.sh 账号认证
- 准备一张正面人像图 (URL) + 台词文本 (voice_script)
- 执行 `belt app run pruna/p-video-avatar --input '{...}'`, JSON 中传入 image、voice_script、voice
- 内置 TTS 将台词合成语音, 模型据此驱动人像口型与动作
- 返回成品视频 (720p/1080p), 画幅比例跟随输入图片

- 统一调用通道: 所有能力都通过 belt CLI 的 `belt app run <app-id> --input '{JSON}'` 触发, 工具权限限定为 Bash(belt *)
- TTS 内置一步到位: 推荐模型 P-Video-Avatar (30 种声音/10 种语言) 在单次调用内完成 文本→语音→口型视频, voice_prompt 与 video_prompt 分别独立控制语气和画面场景; 输出画幅由输入图决定 (竖屏用 pruna/p-image 生成 9:16 人像)
- 两步式备选链路: 不带 TTS 的模型 (OmniHuman 1.5/Fabric/PixVerse) 需先调 Inworld TTS-2 或 Kokoro 生成音频 URL, 再作为 audio_url 传入; 视频配音流程为 Whisper 转写→翻译→Kokoro TTS→LatentSync 对口型
