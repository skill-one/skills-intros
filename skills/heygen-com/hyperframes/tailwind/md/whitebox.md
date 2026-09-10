# tailwind (`heygen-com/hyperframes/tailwind`)

## whitebox

- 确认项目由 `hyperframes init --tailwind` 脚手架创建, 脚本钉在 @tailwindcss/browser@4.2.4, 不替换为 cdn.tailwindcss.com
- 在 composition HTML 写完整的静态 utility class 负责布局和视觉, 动画时序留给 GSAP 等可 seek 的适配器
- 主题 token 和自定义 utility 写进 text/tailwindcss style 块的 @theme / @utility, 不用 v3 的 @tailwind 指令或 tailwind.config.js
- 确保所有渲染关键类名是完整静态 token (数据属性/显式 CSS 兜底), 不在 seek 时动态拼类名
- 跑 npx hyperframes lint / validate / inspect 校验, 再渲染 draft 证明第 0 帧无样式缺失

- 解析与生成: 钉死的 @tailwindcss/browser@4.2.4 运行时在浏览器内扫描当前文档, 对它能看到的类名生成 CSS; Tailwind v4 是 CSS-first (@theme/@utility), 不依赖 JS 配置文件
- 确定性渲染契约: HyperFrames 等 window.__tailwindReady resolve 后才开始截帧; 就绪 shim 必须确定性——无渲染循环轮询、无时钟重试、除钉死的 Tailwind 脚本外无运行时网络请求; 离线/生产稳定场景改为把 Tailwind 编译成 CSS 直接内联
- 校验回路: npx hyperframes validate + render (draft 质量证明片), 判据是第 0 帧无样式闪烁; 若预览有样式渲染没有, 优先检查 __tailwindReady 是否在截帧前就绪
