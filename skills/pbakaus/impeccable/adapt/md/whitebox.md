# adapt (`pbakaus/impeccable/adapt`)

## whitebox

- 强制前置: 先调用 /impeccable 技能, 按其 Context Gathering Protocol 收集设计上下文; 若无设计上下文, 必须先执行 /impeccable teach
- 评估适配挑战: 对比源上下文与目标上下文 (设备、输入方式、屏幕约束、网络、使用场景、用户预期), 找出装不下 / 用不了 / 不合适的部分
- 选取策略模板: 按目标上下文 (mobile / tablet / desktop / print / email) 套用对应的布局、交互、内容、导航四维策略, 核心原则是重构体验而非等比缩放
- 系统性实现: 用断点、clamp()、Grid/Flexbox、容器查询改布局, 触控目标放大到 ≥44px, 改造导航并做响应式图片 / 懒加载
- 跨上下文验证: 真机实测 (不只靠浏览器 DevTools), 覆盖横竖屏、多浏览器 / OS / 输入方式、320px 与 4K 极端尺寸、限速网络

- 外部依赖仅一项: /impeccable 技能 (提供设计原则、反模式与上下文收集协议), 是强制第一步; 不依赖任何外部库或模型 API
- 转换机制是查表式策略匹配: 内置 mobile / tablet / desktop / print / email 五套策略模板, 每套含布局 / 交互 / 内容 / 导航四维方案; 并有硬性约束清单 (如各端保持同一信息架构、移动端不隐藏核心功能)
- 实现层全部走原生 CSS/HTML 原语: media queries 按上下文切换样式, clamp() 做流式尺寸, Grid/Flexbox 自动重排, container queries 按容器适配, srcset/picture 响应式图片
