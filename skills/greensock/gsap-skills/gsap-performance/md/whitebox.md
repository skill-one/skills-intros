# gsap-performance (`greensock/gsap-skills/gsap-performance`)

## whitebox

- 识别触发：用户在问 GSAP 动画性能、卡顿 (jank) 或如何跑满 60fps。
- 扫描并改写属性：把 width/height/top/left/margin/padding 这类触发布局重算的属性，换成 transform (x/y/scale/rotation) 和 opacity。
- 按场景套用规则：长列表用 stagger 替代大量手动 delay 的 tween；高频更新 (如鼠标跟随) 用 quickTo；ScrollTrigger 只 pin 必要元素、scrub 设小值、refresh 只在布局变化时调用并做防抖。
- 收尾加固：仅对真正在动画的元素加 will-change；与直接 DOM 读写混用时先读后写，避免布局抖动 (layout thrashing)；离屏或不可见的动画暂停/kill 掉。

- 合成器优先：GSAP 的 x/y 本质是 translate 变换，动画走 transform/opacity 时浏览器只做合成 (compositor)，跳过 layout 和大部分 paint——这是所有属性改写的唯一依据。
- 按更新频率选 API：quickTo() 复用单个 tween 处理每帧都变的属性，避免反复新建 tween；能复用 timeline 就不每帧新建，减少同时运行的工作量。
- 依赖极简：只用 GSAP 本体 (gsap-core 的 transforms/autoAlpha、timeline、ScrollTrigger 插件) 加原生 CSS will-change；不调用任何模型 API 或外部服务，全部判断来自 skill 里的检查清单 (Best practices / Do Not)。
