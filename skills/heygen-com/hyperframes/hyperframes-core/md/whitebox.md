# hyperframes-core (`heygen-com/hyperframes/hyperframes-core`)

## whitebox

- 任务契合技能后, 以 skill.md 为技术契约开工; 细节按需读 references/ 对应文档 (最小骨架、data-* 属性、确定性规则等)。
- 写一个可渲染组合: 根 div 显式 px 尺寸 + data-* 属性声明时序, 媒体播放权完全交给框架。
- 构建完成后, 向 window.__timelines["<composition-id>"] 注册唯一一个 gsap.timeline({ paused: true })。
- 校验: npx hyperframes check 要求 lint/runtime/layout/motion/contrast 全 0 findings; 有子组合时 snapshot --at 抽帧目检, preview --background 供审阅。
- 用户批准后才执行 npx hyperframes render 出片。

- 时序即 DOM: 用 data-start/data-duration 等属性 + class="clip" 声明时间窗口; 渲染时长取根节点 data-duration, 与 timeline 长度解耦——timeline 超出被截断, 提前结束则停在末帧。
- 确定性可 seek: 媒体由框架平铺查询接管, 任意嵌套深度都能逐帧定位解码; 禁渲染时钟、未播种 Math.random、网络、repeat:-1, 保证任意帧可复现。
- 外部依赖: GSAP 动画运行时 (Lottie/Three.js 等走 hyperframes-animation 的 adapters), HyperFrames CLI (check/snapshot/preview/render); 已知 lint 陷阱 (CSS transform 与 GSAP 冲突、video/audio 加 crossorigin、audio 缺 id 导致静音) 由 check 事后拦截, 依赖一次写对。
