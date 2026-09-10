# gsap (`heygen-com/hyperframes/gsap`)

## whitebox

- 在页面通过 CDN 加载 GSAP 库 (gsap.min.js), 同步创建一个 paused 状态的 timeline
- 用 gsap.to/from/fromTo 等方法编排动画, 靠位置参数和标签控制各段动画在时间轴上的落点
- 把 timeline 注册到 window.__timelines, key 必须与合成根节点的 data-composition-id 完全一致
- 自己不调用 tl.play(), 交由 HyperFrames 对这条时间轴做 seek (按指定时间点定位) 来逐帧渲染
- 循环保持有限 (repeat 不用 -1), 按可见时长计算重复次数, 渲染结束后清理

- 注册表契约: HyperFrames 通过 gsap 运行时适配器接管播放 — timeline 必须同步创建、禁止建在异步代码/定时器/事件回调里; 渲染关键动画不许用 tl.play(), 只能被 seek 驱动
- 性能机制: 优先动画 transform 别名 (x/y/scale/rotation) 和 autoAlpha, 让动画走浏览器合成器路径; 配合 will-change, 用 stagger 批量错开替代多条手动 delay 的小 tween
- 外部依赖: GSAP 3.x 动画引擎 (示例版本 3.14.2, 从 jsDelivr CDN 加载), 提供核心能力: to/from/fromTo/set 四种补间、timeline 位置参数与标签、power/back/elastic 等缓动函数族
