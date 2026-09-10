# hyperframes-animation (`heygen-com/hyperframes/hyperframes-animation`)

## comments

- user: 第一次做动效的新手, category: 坑, comment: 粒子散布用了 Math.random, 预览没事, 重渲一遍位置全变。改成 setup 时算好的固定数组就稳了——时间轴必须可复现。
- user: 写了五年页面的前端, category: 坑, comment: 卡片展开我 tween 了 width/height, 渲染时布局错位。位移缩放只能走 x/y/scale/rotation, 换成 transform 立刻正常。
- user: 后端转全栈, category: 妙用, comment: 写完别肉眼 scrub, 直接跑 animation-map.mjs, 死区和 stagger 不一致都列进 json, 我靠它删掉三条看不见的 tween。
- user: AE 出身的动效师, category: 注意, comment: AE 导出的 lottie 别用 GSAP 硬仿, 挂到 __hfLottie 就进同一条时间轴被统一 seek, 手动同步的坑完全绕开。
- user: 接动画外包的老手, category: 注意, comment: tween 回调里现量 getBoundingClientRect 会和渲染的并行采样错位, 坐标要在 setup 阶段算好存常量, 我为此返工过一次。
- user: 独立产品开发者, category: 启发, comment: 它把我从'加个动画'掰成拆规则: 入场+stagger+退场各选一条 rule 拼一条 timeline, 比整套抄蓝图少一半代码。
