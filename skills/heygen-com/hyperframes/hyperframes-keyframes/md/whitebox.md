# hyperframes-keyframes (`heygen-com/hyperframes/hyperframes-keyframes`)

## whitebox

- 识别动画主体、可见状态、最终态和时长，并点名要证明的运动。
- 选最小能证明意图的机制 (需要时才查 references/keyframe-patterns.md)。
- 在声明的运行时里同步构建 seek-safe 关键帧并注册运行时实例 (如 GSAP paused 时间线挂到 window.__timelines)。
- 用 hyperframes lint / check / keyframes 加一个聚焦 --shot 和各证明时刻的快照验证。
- 验证不过就改源头关键帧，重跑最小失败诊断。

- 关键帧即'姿态契约'：显式中间姿态 + 主体身份连续 + 最终态。运行时必须确定性可 seek——GSAP 同步构建 paused 时间线并按 data-composition-id 注册；Anime.js autoplay:false 入 window.__hfAnime；WAAPI fill:'both'；禁止 Date.now/random/timers/hover 触发等非确定性来源。
- 分层归责：hyperframes-core 掌管时间线与片源区间 (trim/splice)，本技能只对 clip 内 wrapper 上的可见通道 (transform/opacity/clip-path/mask) 做动画；跨'画面+声音'的成品交给 core 和 hyperframes-audio。
- 像素级校验依赖 HyperFrames CLI：keyframes --shot (ghost 轨迹/3D 投影)、--ghost (canvas/WebGL)、snapshot --at (首帧/证明姿态/末帧)；日志与实际像素冲突时以像素为准。外部库可选 GSAP (含 DrawSVG/MorphSVG 插件)、Anime.js、WAAPI、CSS keyframes、Three.js/WebGL。
