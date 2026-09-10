# seam-craft (`heygen-com/hyperframes/seam-craft`)

## whitebox

- 触发: 组装 master timeline / index.html, 或场景切换缝隙出现白闪 (尤其暗色影片)、需要核对转场渲染机制时进入本技能。
- 涂底色: 确认 #root 有不透明背景 var(--canvas-deep, var(--canvas, #000)), 挡住渲染器默认白底, 防止转场中透明度总和 < 1 的窗口露出白闪。
- 造重叠: 在 break 边界, 把出场场景 #el-<from> 的 data-duration 延长 duration_s (定格末帧), 把入场 #el-<to> 的 data-start 提前 duration_s (形成重叠窗口)。
- 错轨道: 所有 clip 的 data-track-index 重排为 0/1 乒乓, 保证两个重叠 wrapper 不共享轨道 (同轨重叠非法), 高轨道在上层合成。
- 盖章: 把 gsap_template 中 __OLD__/__T__/__DUR__ 等占位符替换后, 写入 window.__timelines["main"] 的 T = 重叠起点处。

- 模板占位符替换: 注入器对每行 gsap_template 做字符串令牌替换 (__OLD__/__NEW__/__T__/__DUR__/__DX__/__DY__/__ORIGIN_OUT__/__ORIGIN_IN__), 纯填充、无动态计算。
- Lint 规则约束正确性: 同轨重叠由 core/src/lint/rules/composition.ts 判为非法 (故需 0/1 乒乓); core/src/lint/rules/gsap.ts 无逐属性白名单且只按 data-composition-id 范围检查, 所以 filter/scaleX/transformOrigin 在 master timeline 上可用 (白名单只是场景 worker 的 prompt 规则)。
- 外部依赖 GSAP (网页动画时间轴库) + HyperFrames core 运行时: 转场以 GSAP 模板盖进主时间轴, 运行时 (core/src/runtime/init.ts 外部 slot 分支) 驱动 seek/渲染, 与子组件自身暂停的时间轴互不双 seek——已由 2026-05-31 原型渲染验证。
