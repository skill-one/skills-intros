# graphic-overlays (`heygen-com/hyperframes/graphic-overlays`)

## whitebox

- 环境自检 (npx hyperframes doctor 确认 ffmpeg/无头浏览器/渲染依赖), ffprobe 读出视频时长/分辨率/fps 写入 metadata.json, ffmpeg 抽出 audio.mp3
- hyperframes transcribe 调本地 Whisper 把音频转成词级 transcript.json (每词带 start/end 时间戳), agent 通读并修正识别错误后自己按标点/停顿归组成句
- agent 依据转写内容与密度公式 max(5, round(时长 ÷ (基础节奏 × 密度系数))) 推断卡片数量与时间轴, 写 storyboard.json; 先向用户确认输出比例/布局/视觉风格/卡片数再动手
- agent 在对话中逐张手写卡片 HTML (public/cards/card-XX.html), 按 zone 解析成画布像素边界, 组装成单一 composition (public/index.html), 动画用内置 GSAP 时间轴
- hyperframes render 用无头浏览器逐帧渲染该 composition, 输出 output.mp4 (源视频全程完整播放, 卡片作为图形层叠加其上)

- 词级时间戳驱动卡片时序: transcript.json 是扁平词数组 {text,start,end} (无 segments 封装), agent 自行分组; 所有 endSec 与 composition.durationSeconds 会被 clamp 到 ffprobe 读出的媒体时长, 防止渲染尾部黑屏
- zone → 像素边界解析: 5 种区域 (fullscreen / whiteboard-area / lower-third / side-panel / video-overlay) 按画布坐标系解析成 bounds; videoTrack.bounds 在 composition 层只设一次, 想让视频'在卡片间移动'靠 GSAP 对 #video-wrap 补间实现; 可选转场 (cut/fade/slide/wipe) 是声明式声明, 由 composition 脚本落地
- 全本地工具链, 无第三方 API key: 依赖系统 ffmpeg/ffprobe (抽音频+元数据), hyperframes CLI (内置 Whisper 转写 + 无头浏览器渲染), 以及 skill 自带 assets (woff2 字体 + gsap.min.js); storyboard.json 仅是 agent 内部规划产物, 没有 CLI 消费它
