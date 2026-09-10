# hyperframes-audio (`heygen-com/hyperframes/hyperframes-audio`)

## whitebox

- 按症状定位问题 (如 '人声和音乐打架'/'发闷'), 先查 references/presets.md 的预设与命名任务表, 命中就不手搓链。
- 在音频元素上写属性: data-fx-chain 按信号顺序串效果, data-automation 写包络; 人声下方的音乐床再写 data-fx-carve。
- 做 carve 时, Studio 面板或 scripts/carve.mjs 调 core/audioCarve.ts 分析人声频段与动态, 把 peaking 挖槽 + level-match gain + 自动化 lane 写回音乐床元素。
- 预览: 同一套 builder (buildFxChain / scheduleChainAutomation) 在实时 AudioContext 里搭图; MutationObserver 监听属性中途改动并即时生效。
- 渲染: 无头浏览器内用 OfflineAudioContext 跑同一张图, 输出处理后 WAV (+chainTailSeconds 让尾音通过), 引擎 audioMixer 把音量 lane 烘进 PCM。

- 属性即中间表示: data-fx-chain / data-automation / data-fx-carve 三个属性承载全部混音逻辑, 链为串行 (修正滤波在前、角色化居中、limiter 收尾); data-fx-carve 本身不参与播放, 播放的永远是它生成的链与 lane, 该属性只存设置以便改 strength 时重新推导。
- 一份实现、两个运行时: audioFxGraph.buildFxChain 与 audioFxAutomation.scheduleChainAutomation 同时被预览 (live AudioContext) 和渲染 (headless 浏览器内的 OfflineAudioContext) 读取, 故试听即成片、不用调两遍。依赖: 浏览器原生 Web Audio API + 无头浏览器, 无外部模型或服务 API。
- 校验分两层: lint 规则 (audio_carve_ungrouped_sources 要求 sources 用 group 而非逐个 clip id; audio_group_carve_attr 抓写上总线的 carve) 在编排层指出问题; carve.mjs 遇到非法 group 组成 (床在自己组里/组里混入 SFX) 会拒写并在 stderr 报出阻塞成员。
