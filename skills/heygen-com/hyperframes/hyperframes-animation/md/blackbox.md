# hyperframes-animation (`heygen-com/hyperframes/hyperframes-animation`)

## blackbox

**function**: 把动效点子直接变成能跑的动画网页代码:你说想要什么效果,我给你一段可播放、可逐帧对齐的动画成品;也能给已写好的动画做"体检",找出节奏毛病。

- input: 「做一个 5 秒片头:logo 缩放登场,然后标语逐字升起」, output: 一个能直接在浏览器打开播放的动画页面 (HTML),节奏和效果与描述一致,并可渲染成视频
- input: 一个已写好的动画作品目录路径 (如 ./intro-scene), output: 一份动画体检报告 (JSON 文件):列出哪里有 3 秒以上的呆滞空档、哪些元素出现后立刻消失等具体警告
- input: 一段文案 + 「用打字机效果」, output: 带打字机动效的代码片段,替换原来的静态文字即可播放
- input: 一个动画素材文件 (如 After Effects 导出的 JSON), output: 把该素材嵌入作品、并与场景其他动画同步播放的完整代码
