# apple-design (`emilkowalski/skills/apple-design`)

## whitebox

- 接收与技能契合的任务: 构建或评审手势驱动 UI、弹性动画、拖拽/滑动/抽屉交互、半透明材质、排版等
- 从 skill.md 匹配对应章节的原则 (可中断性、速度传递、动量投影、橡皮筋、材质层次等)
- 把原则翻译为 Web 实现: CSS + Pointer Events + requestAnimationFrame + 弹簧库 (Motion/Framer Motion)
- 套用内置默认值: 阻尼 1.0 起步、动量手势才加 bounce、具体参数查表 (抽屉 0.8/0.3 等), 并做 reduced-motion 等降级处理
- 输出可直接落地的代码片段或评审结论

- 知识源: 全部规则蒸馏自 Apple WWDC 设计讲稿 (核心是 Designing Fluid Interfaces 2018, 辅以排版/音频触感/设计原则等讲稿), 每条建议都能溯源到讲稿, 不调用外部模型或工具
- 转换机制: 把 iOS 物理概念映射到 Web — Pointer Events + setPointerCapture 实现 1:1 拖拽跟踪, requestAnimationFrame 驱动逐帧更新, 只动画 transform/opacity; 依赖弹簧库 Motion (Framer Motion), 其 bounce/duration API 映射 Apple 的阻尼/响应参数, 松手速度直接作为弹簧初速度 (velocity), 动量投影用 Apple 官方指数衰减公式 (decelerationRate≈0.998) 而非教科书公式
- 校验机制: 按检查清单收尾 — 动画必须从当前呈现值起跳且可随时抓取反转; 反馈在 pointer-down 瞬间给出; 手势反向时速度平滑混合不硬切; 材质半透明层不叠放; 最后用 prefers-reduced-motion / prefers-reduced-transparency / prefers-contrast 三条媒体查询做降级
