# talking-head-recut (`heygen-com/hyperframes/talking-head-recut`)

## whitebox

- 环境自检: npx hyperframes doctor 确认 ffmpeg/ffprobe、无头浏览器和捆绑资产 (字体 + gsap.min.js) 就绪
- 预处理: ffmpeg 抽取 audio.mp3, ffprobe 读出时长/宽高/fps 写入 metadata.json
- 转写: hyperframes transcribe 调本地 Whisper 生成逐词 transcript.json (含 start/end 时间戳), 人工修正 ASR 错误并按标点自行切句
- 设计卡片: 读转写稿起草 storyboard.json (卡片 id/时间区间/zone/内容), 每张卡片手写 HTML 片段存入 public/cards/
- 组装渲染: 把视频轨 + 卡片 + GSAP 时间轴合成 public/index.html, hyperframes render 输出 output.mp4

- 时间轴全靠逐词转写驱动: Whisper (本地运行, 无 API key) 输出词级 {text, start, end}, 卡片时间戳据此设定, 并一律 clamp 到视频真实时长, 避免渲染出黑尾
- 卡片即手写 HTML 片段: zone (fullscreen/lower-third/side-panel 等 5 种) 按表解析成画布像素坐标, 视频轨 bounds 在合成层只设一次, 视频移动感靠 GSAP 对 #video-wrap 的 tween 实现; 每卡片时长由 视频时长 ÷ (基础节奏 × 密度系数) 推导, 下限 5 张
- 外部依赖: hyperframes CLI (transcribe=本地 Whisper, render=无头浏览器+ffmpeg 合成 MP4)、系统 ffmpeg/ffprobe、技能内捆绑的 GSAP 与 woff2 字体
