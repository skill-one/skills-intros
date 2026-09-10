# hyperframes-animation (`heygen-com/hyperframes/hyperframes-animation`)

## whitebox

- 按需求路由: 查 rules-index.md / blueprints-index.md / transitions / adapters 等索引, 按需只读对应的知识文件
- 默认路径: 从规则索引挑 2~4 条原子动效规则, 用一条暂停状态的 GSAP timeline 串联成完整编排 (优先于加载 blueprint)
- 套上硬约束: 遵守核心契约 (单一暂停 timeline、data-duration 定长、禁 Math.random/Date.now、禁 tween 时测量 DOM、空间位移只用 x/y/scale/rotation 别名)
- 按场景选运行时适配器: 默认 GSAP, 资产自带时间线用 Lottie, 3D 用 Three.js, 轻量补间用 Anime.js, 装饰循环用 CSS, 原生 keyframes 用 WAAPI, GPU 着色器用 TypeGPU
- 可选审计: 运行 scripts/animation-map.mjs, 读取 window.__timelines 上的所有 timeline, 输出 animation-map.json 检查死区/stagger 一致性/生命周期警告

- 知识库路由 + 惰性加载: 动效知识拆成 rules (原子配方) / blueprints (多阶段场景模板) / transitions / techniques / adapters (各运行时 API) 的 Markdown 索引, 只在确定需要时才读对应条目, 不预读
- 确定性渲染契约: 整个合成是单条暂停 timeline, 播放靠 seek 驱动, 因此禁止 Math.random / Date.now / repeat: -1 / async 中建 timeline; 布局坐标在合成初始化时一次性算好, 不在 tween 时刻调 getBoundingClientRect
- 多运行时共存 + 统一寻道: GSAP (默认) / Lottie (window.__hfLottie) / Anime.js (window.__hfAnime) / Three.js 等各自把实例注册到 window.__timelines 等运行时专属全局变量, HyperFrames 渲染时一次 seek 同步所有运行时; 审计脚本 animation-map.mjs (Node) 从这些全局枚举 tween、采样 bbox 并输出 JSON
