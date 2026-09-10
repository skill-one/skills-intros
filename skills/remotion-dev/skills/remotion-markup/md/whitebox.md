# remotion-markup (`remotion-dev/skills/remotion-markup`)

## whitebox

- 接到任务后先判断是否是 Remotion (用 React 写视频的框架) 标注/动画需求, 并按主题加载对应子文档 (转场、字幕、地图、配音、GIF 等)
- 用 React 组件写画面, 所有动画由 useCurrentFrame() 取当前帧 + interpolate() 逐帧算出, 明确不用 CSS transition/animation (无法逐帧正确渲染)
- 素材放 public/ 目录用 staticFile() 引用; 视频/音频用 @remotion/media, 图片用 CanvasImage, 动图用 AnimatedImage
- 需要新能力时先加载对应子文档, 缺包则用 npx remotion add 装匹配版本
- 起 npx remotion studio --no-open 预览, 必要时用 npx remotion still 渲染单帧抽查布局/配色/时机

- 帧驱动动画机制: interpolate() 必须内联在 style 里, 靠 extrapolate clamp 防止越界, 用 Easing.bezier()/Easing.spring() 调节奏; 变换优先写 scale/translate/rotate 简写而非 transform 字符串, scale 加 output: 'perceptual-scale'
- 特效分层选型: 优先纯 HTML+CSS; 像素级特效则包在 <HtmlInCanvas> 里套 effects 预设或 createEffect() 自定义; FFmpeg 负责裁剪、静音检测等视频操作 (经 Chrome 逐帧渲染出片)
- 可插拔子能力 (均由子文档定义, 按需加载): 配音走 ElevenLabs TTS API, 地图走 Mapbox/MapLibre/MapTiler, 参数化视频用 Zod schema + calculate-metadata 动态定时长尺寸
