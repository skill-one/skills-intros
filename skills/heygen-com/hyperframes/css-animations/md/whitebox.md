# css-animations (`heygen-com/hyperframes/css-animations`)

## whitebox

- 按契约编写: 动画元素在运行时初始化前进入 DOM, 标注 data-start/data-duration, CSS 用有限 animation-duration + iteration-count 和 animation-fill-mode: both 写 keyframes
- HyperFrames 启动, css 适配器按 computed animation-name 发现所有 CSS 动画元素
- 预览/渲染逐帧 seek: 优先 seek 浏览器 WAAPI 的 Animation 句柄, 环境不支持则 pause + 负 animation-delay 兜底
- 收尾: 跑 npx hyperframes lint 和 npx hyperframes validate 校验

- 时间对齐: data-start 让元素局部动画时间匹配 clip 时间轴; fill-mode: both 保证 seek 到动画开始前/结束后的状态稳定保持
- 确定性 seek: 依赖浏览器 WAAPI (Web Animations API) 暴露的可 seek Animation 句柄, 不可用时退化为暂停 + 负 animation-delay 重建时间点; 因此必须用有限 iteration-count (负 delay 兜底表达不了无限动画)
- 校验与红线: npx hyperframes lint / validate; 禁止墙钟 JS、hover/事件触发、动画后改 class; 布局属性 (top/left/width/height) 改用 transform; 复杂场景编排建议改用 GSAP 时间线而非 CSS
